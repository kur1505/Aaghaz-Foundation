from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

# Import logging from Python's standard library
import logging

# Create a logger for this file
logger = logging.getLogger(__file__)

def login_view(request):
    # form = LoginForm(request.POST or None)

    # msg = None

    # if request.method == "POST":

    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(username=username, password=password)
    #         if user is not None and user.is_staff is True:
    #             login(request, user)
    #             return redirect("/index/")
    #         else:    
    #             msg = 'Invalid credentials'    
    #     else:
    #         msg = 'Error validating the form'    
    logger.info("This logs an info message.")
    return render(request, "accounts/login.html")

def register_user(request):

    # msg     = None
    # success = False

    # form = SignUpForm()
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         username = form.cleaned_data.get('username')
            
    #         messages.success(request, 'Account is created for ' + username)
    #         return redirect("loginCustomer/")
            
    #     else:
    #         msg = 'Form is not valid'    
    # else:
    #     form = SignUpForm()

    return render(request, "accounts/register.html")

def reset(request):

    return render(request, "accounts/reset.html")