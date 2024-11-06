from tkinter import Image
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *

from content.forms import LoginForm, PostForm, RegisterForm
from content.models import Post

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('loginUser')
    else:
        posts = Post.objects.order_by('-id')
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.cleaned_data['post']
                image = request.FILES.getlist('image')

                new_post = Post(post=post)
                new_post.save()
                for imageitem in image:
                    new_image = Image(post=new_post, image=imageitem)
                    new_image.save()
        else:
            form = PostForm()
        context = {
            'form': form,
            'posts': posts
        }
        return render(request, 'index.html', context)
    
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error('username', 'Invalid username or password.')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def RegisterUser(request):
    if request.user.is_authenticated:
        return redirect('index')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error('username', 'Error while registering.')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')