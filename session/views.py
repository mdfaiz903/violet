import  copy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,get_user_model
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from .forms import CustomSignupForm
from cart . cart import Cart

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

User_model = get_user_model()
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
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Active your Account"
            message = render_to_string('session/account.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            messages.info(request,'Successfully created account, Please check your Mail box')
            return  redirect('login')
    else:
        form = CustomSignupForm()
    return  render(request,'session/signup.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User_model._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User_model.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Your account is activate now,you cant now login')
        return redirect('login')
    else:
        messages.warning(request,'Activation link is Invalid')
        return redirect('signup')

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
