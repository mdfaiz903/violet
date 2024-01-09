from django.urls import path
from . views import AddTocart,cartItems,AddCoupon
urlpatterns = [
    path('add-to-cart/<int:product_id>/',AddTocart.as_view(),name='add-to-cart'),
    path('cart/',cartItems.as_view(),name='cart'),
    path('add-coupon/',AddCoupon.as_view(),name='add-coupon'),
    
]
