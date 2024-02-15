from django.urls import path
from. views import loginuser
urlpatterns = [
    path('login/',loginuser,name='login')
]
