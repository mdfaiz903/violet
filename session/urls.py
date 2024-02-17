from django.urls import path
from. views import loginuser,logoutUser,signup
urlpatterns = [
    path('login/',loginuser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('signup/',signup,name='signup'),
]
