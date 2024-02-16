from django.urls import path
from. views import loginuser,logoutUser
urlpatterns = [
    path('login/',loginuser,name='login'),
    path('logout/',logoutUser,name='logout'),
]
