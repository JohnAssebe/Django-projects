from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['user_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'UserName Token.....Try with other User name')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Token........Try with other Email address')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,'Password Mismatched')
            return redirect('register')
    else:  
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"UserName or Password Error")
            return redirect('login')
        
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')