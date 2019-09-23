from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    elif request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        auth.login(request,user)
        return render(request,"login.html")

def signup(request):
    if request.method=="GET":
        return render(request, "signup.html")
    elif request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        pwcheck = request.POST["pwcheck"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        if User.objects.filter(username=username).exists():
            return render(request, "signup.html",{"user_overlap":"이미 존재하는 아이디 입니다."})
        if password != pwcheck:
            return render(request, "signup.html",{"pw_msg":"비밀번호가 일치하지 않습니다"})
        # if User.objects.filter(email=email).exists():
        #     return render(request, "signup.html", {"email_overlap":"이미 가입된 이메일 입니다"})
        user = User.objects.create_user(username=username, password=password, name=name, email=email,phone=phone)
        auth.login(request, user)
    return redirect('index')

def signout(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            auth.logout(request)
    return redirect('index')