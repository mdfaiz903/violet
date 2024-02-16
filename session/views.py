from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
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
    logout(request)
    messages.success(request,"Successfully Loged Out")
    return redirect('login')