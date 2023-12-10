from typing import Any
from django import http
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

