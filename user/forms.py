from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

class SingUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')

    class Meta:
        model = User
        fields = ["username",'email','password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Passwords do not match!")
        
        return cleaned_data 




def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # البحث عن المستخدم في قاعدة البيانات
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            # التحقق من كلمة المرور
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # تسجيل الدخول
                return redirect('academy_app')  # استبدلها بالصفحة التي تريد التوجيه إليها
            else:
                error_message = "كلمة المرور غير صحيحة"
        else:
            error_message = "اسم المستخدم غير موجود"
        
        return render(request, "login.html", {"error_message": error_message})
    
    return render(request, "login.html")




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



# user/forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
