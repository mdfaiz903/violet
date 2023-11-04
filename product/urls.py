from django.urls import path
from.views import index,ProductDetails

urlpatterns = [
    
    path('',index.as_view(),name='home'),
    path('product-detail/',ProductDetails.as_view(),name='ProductDetails'),
]
