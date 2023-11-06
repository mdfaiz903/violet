from django.urls import path
from.views import index,ProductDetails

urlpatterns = [
    
    path('',index.as_view(),name='home'),
    path('product-detail/<str:slug>/',ProductDetails.as_view(),name='ProductDetails'),
]
