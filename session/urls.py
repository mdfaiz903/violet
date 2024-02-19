from django.urls import path
from. views import loginuser,logoutUser,signup,pass_change
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    path('login/',loginuser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('signup/',signup,name='signup'),
    path('pass_change/',pass_change,name='pass_change'),
    path('accounts/password_reset/ ',PasswordResetView.as_view(template_name='session/password_reset.html'),name='password_reset'),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(template_name='session/password_reset_done.html'),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='session/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(template_name='session/password_reset_complete.html'),name='password_reset_complete'),
]

"""
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
"""