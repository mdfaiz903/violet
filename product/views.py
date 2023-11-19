from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView,ListView
from . models import *
from django.core.paginator import(
     PageNotAnInteger,
     EmptyPage,
     InvalidPage,
     Paginator,
)
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
          context['products'] = self.get_object().products.all()
          return context
class customPaginator:
     def __init__(self,request,queryset,paginated_by) -> None:
          self.paginator = Paginator(queryset,paginated_by)
          self.paginated_by = paginated_by
          self.queryset = queryset
          self.page = request.GET.get('page', 1)

     def  get_queryset(self):
          try:
               queryset = self.paginator.page(self.page)
          except PageNotAnInteger:
               queryset = self.paginator.page(1) # when pageNotAnInteger defaulting to 1 if not present
          except EmptyPage:
               queryset = self.paginator.page(1)
          except InvalidPage:
               queryset = self.paginator.page(1)

          return queryset
          


class ProductList(ListView):
     model = Product
     template_name='product/product_list.html'
     context_object_name = 'object_list'
     paginate_by = 4 # How many item want to show
     def get_context_data(self, **kwargs):
          
          context =  super().get_context_data(**kwargs)
          page_obj = customPaginator(self.request,self.get_queryset(),self.paginate_by)
          queryset = page_obj.get_queryset()
          Paginator = page_obj.paginator
          context['object_list'] = queryset
          context['paginator'] = Paginator
          return context 