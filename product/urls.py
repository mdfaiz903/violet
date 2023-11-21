from django.urls import path
from.views import (
    index,
    ProductDetails,
    CategoryDetails,
    ProductList,
    searchResult,
)

urlpatterns = [
    
    path('',index.as_view(),name='home'),
    path('product-detail/<str:slug>/',ProductDetails.as_view(),name='product-details'),
    path('category-detail/<str:slug>/',CategoryDetails.as_view(),name='category-details'),
    path('Product-list/',ProductList.as_view(),name='product-list'),
    path('search-Result/',searchResult.as_view(),name='search_products'),
]
