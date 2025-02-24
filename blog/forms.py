from django import forms
from .models import Post
from django.contrib.auth.models import User




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['img','title','content']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']










