from datetime import datetime
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404,redirect


# Create your views here.
from . cart import Cart # from . file_name import function_name(class Cart)
from . models import Coupon
from  product.models import Product
class AddTocart(generic.View):
    def post(self,*args, **kwargs):
        product = get_object_or_404(Product,id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id,1)
        return redirect('cart')


class cartItems(generic.TemplateView):
    template_name = 'cart/cart.html'

    def get(self, request, *args,**kwargs):
        product_id = request.GET.get('product_id',None)# if product_id is hold otherwise None, product_id from cart.html
        quantity = request.GET.get('quantity',None)# if quantity is hold otherwise None
        clear = request.GET.get('clear',False)# if clear is hold otherwise False
        cart = Cart(request)
        if clear:
            cart.clear()
            return redirect('cart')
        if product_id and quantity :
            cart.update(int(product_id),int(quantity))
            return redirect('cart')
        return super().get(request, *args, **kwargs)

# class for add coupon functionality
class AddCoupon(generic.View):
    def post(self,*args, **kwargs):
        code = self.request.POST.get('coupon','')
        coupon = Coupon.objects.filter(code__iexact=code,active=True)
        cart = Cart(self.request)
        if coupon.exists():
            coupon = coupon.first()
            current_date = datetime.date(timezone.now())
            print("current_date: ",current_date)
            active_date = coupon.active_date
            expiry_date = coupon.expiry_date

            if current_date > expiry_date:
                messages.warning(self.request, "The coupon expired")
                return redirect('cart')   
            if current_date < active_date:
                messages.warning(self.request, "The coupon is not yet available")
                return redirect('cart')
            cart.add_coupon(coupon.id)
            messages.success(self.request, "The coupon was added successfully")
            return redirect('cart')
        else:
            messages.warning(self.request,"Invalid coupon code")
            return redirect('cart')