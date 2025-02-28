from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login
from user.forms import SingUpForm


# Create your views here.

def signup(request):
    if request.method =='POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('login')
    else:
        form = SingUpForm()
    return render(request,'signup.html',{'form':form})





from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل دخول المستخدم تلقائيًا بعد التسجيل
            return redirect('login')  # إعادة التوجيه إلى الصفحة الرئيسية بعد التسجيل
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})





