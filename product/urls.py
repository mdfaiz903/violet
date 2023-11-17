from django.urls import path
from.views import index,ProductDetails,CategoryDetails

urlpatterns = [
    
    path('',index.as_view(),name='home'),
    path('product-detail/<str:slug>/',ProductDetails.as_view(),name='ProductDetails'),
    path('category-detail/<str:slug>/',CategoryDetails.as_view(),name='category-details'),
]
