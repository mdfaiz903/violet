from django.urls import path
from. views import loginuser,logoutUser,signup,pass_change
urlpatterns = [
    path('login/',loginuser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('signup/',signup,name='signup'),
    path('pass_change/',pass_change,name='pass_change'),
]
