from  product.models import Product
from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.views import generic
from . cart import Cart # from . file_name import function_name(class Cart)
# Create your views here.

class AddTocart(generic.View):
    def post(self,*args, **kwargs):
        product = get_object_or_404(Product,id=kwargs.get('product_id'))
        cart = Cart(self.request)
        cart.update(product.id,1)
        return redirect('cart')


class cartItems(generic.TemplateView):
    template_name = 'cart/cart.html'

