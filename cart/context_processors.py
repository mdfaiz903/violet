from . cart import Cart
#for global access from cart.py
def cart(request):
    cart = Cart(request)

    if len(list(cart.cart.keys()))<1:
        try:
            del cart.session[cart.coupon_id]
        except:
            ...
    return {"cart":Cart(request)}