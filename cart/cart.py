from django.conf import settings
from product.models import Product
from . models import Coupon
class Cart(object):
    def __init__(self,request)->None:
        self.session = request.session # store session initially
        #car_id from settings file
        self.cart_id = settings.CART_ID
        self.coupon_id= settings.COUPON_ID
        cart = self.session.get(self.cart_id) # is cart_id avalable or not in session
        coupon = self.session.get(self.coupon_id)
        self.cart = self.session[self.cart_id] = cart if cart else {} # if cart avalable or not then excute empty dic.
        self.coupon = self.session[self.coupon_id] = coupon if coupon else None 

    def update(self,product_id,quantity=1):
        product = Product.objects.get(id=product_id)
        self.session[self.cart_id].setdefault(str(product_id),{"quantity":0})
        updated_quantity = self.session[self.cart_id][str(product_id)]['quantity'] + quantity
        self.session[self.cart_id][str(product_id)]['quantity']=updated_quantity
        self.session[self.cart_id][str(product_id)]['subtotal']= updated_quantity * float(product.price)

        if updated_quantity < 1:
            del self.session[self.cart_id][str(product_id)]


        self.save()
    def add_coupon(self,coupon_id):
        self.session[self.coupon_id] = coupon_id
        self.save()

    #How many item in cart
    def __iter__(self):
        products = Product.objects.filter(id__in = list(self.cart.keys()))#individual product id as key for filtering
        cart = self.cart.copy() # for copy orginal cart

        for item in products:
            product = Product.objects.get(id=item.id)
            cart[str(item.id)]['product']={
                "id":item.id,
                "title":item.title,
                "category":item.category.title,
                "price":float(item.price),
                "thumbnail":item.thumbnail,
                "slug":item.slug
            }
            yield cart[str(item.id)] # return generator expression

    def save(self):
        self.session.modified = True

    def __len__(self):
        return len(list(self.cart.keys()))
    
    def clear(self):
        try:
            del self.session[self.cart_id]
            del self.session[self.coupon_id]
        except:
            pass
        self.save()
#calculate after added coupon
    def total(self):
        amount = sum(product['subtotal'] for product in self.cart.values())
        if self.coupon:
            coupon = Coupon.objects.get(id=self.coupon)
            amount-=amount * (coupon.discount/100)
        return amount