from . cart import Cart
#for global access from cart.py
def cart(request):
    return {"cart":Cart(request)}