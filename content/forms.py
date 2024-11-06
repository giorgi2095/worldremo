import re
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

class PostForm(forms.Form):
    post = forms.CharField(required=True)
    image = forms.ImageField(required=True)