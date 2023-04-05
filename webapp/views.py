from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        return redirect("login")
    else:
        return  render(request, 'register.html')


def login(request):
    if request.method == 'POST':

        return redirect('home')
    else:
        return render(request, "login.html")


def home(request):
    return  render(request, 'index.html')

def Gadgets(request):  
    return render(request, 'gadget.html')