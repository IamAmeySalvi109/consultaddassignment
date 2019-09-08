from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    index_var = {'index_temp_var': ''}
    return render(request, 'Home/index.html', context = index_var)

def about(request):
    about_var = {'about_temp_var': ''}
    return render(request, 'About/about.html', context = about_var)

def gallery(request):
    gallery_var = {'gallery_temp_var': ''}
    return render(request, 'Gallery/gallery.html', context = gallery_var)

def login(request):
    login_var = {'login_temp_var': ''}
    return render(request, 'Login/login.html', context = login_var)

def signup(request):
    signup_var = {'signup_temp_var': ''}
    return render(request, 'Signup/signup.html', context = signup_var)
