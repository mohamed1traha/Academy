from django import forms
from .models import Post1
from django.contrib.auth.models import User




class PostForm(forms.ModelForm):
    class Meta:
        model = Post1
        fields = ['img','title','content']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']










