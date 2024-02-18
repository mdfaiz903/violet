import  copy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from .forms import CustomSignupForm
from cart . cart import Cart
# Create your views here.

def loginuser(request):
    if request.method=='POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid Username or Password")
        else:
            messages.error(request,"Invalid Username or Password")
    else:
        form = AuthenticationForm()
    return render(request,'session/login.html',{'form':form})


def logoutUser(request):
    # use for store cart & coupon session data
    cart = Cart(request)
    current_cart = copy.deepcopy(cart.cart)
    coupon = copy.deepcopy(cart.coupon)
    logout(request)
    cart.restore_after_logout(current_cart,coupon)
    messages.success(request,"Successfully Loged Out")
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Success')
            return  redirect('login')
    else:
        form = CustomSignupForm()
    return  render(request,'session/signup.html',{'form':form})


def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST,user = request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,"Password Change Successfully")
                return redirect('login')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'session/change_pass.html',{'form':form})
    else:
        messages.warning(request,"Invalid User")
