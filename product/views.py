from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from . models import *
# Create your views here.
class index(TemplateView):
     template_name = "index.html"

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context.update(
               {
                    'featured_categories':Category.objects.filter(featured=True),
                    'featured_products':Product.objects.filter(featured=True),
                    'slider':slider.objects.filter(show=True),
               }
          )
          return context

class ProductDetails(DetailView):
    model = Product
    template_name = "product/product-details.html"
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
         context= super().get_context_data(**kwargs)
         context['related_product']=self.get_object().related
         return context



class CategoryDetails(DetailView):
     model = Category
     template_name = 'product/category-details.html'
     slug_url_kwarg = 'slug'

     def get_context_data(self, **kwargs):
          context= super().get_context_data(**kwargs)
          context['product'] = self.get_object().products.all()
          return context
     