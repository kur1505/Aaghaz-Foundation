from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib import messages
from .models import *
# Import logging from Python's standard library
import logging
# Create a logger for this file
logger = logging.getLogger(__file__)


def index(request):

    logger.info("This logs an info message.")
    return render(request, "website/index.html")

# <---------------------------------------- Donor Views ------------------------------------------------->
def donor_list(request):

    logger.info("This logs an info message.")
    return render(request, "donor/donor_list.html")


def donor_create(request):

    logger.info("This logs an info message.")
    return render(request, "donor/donor_create.html")



# <---------------------------------------- Volunteer Views --------------------------------------------->
def volunteers_list(request):

    logger.info("This logs an info message.")
    return render(request, "volunteer/volunteers_list.html")


def volunteer_create(request):

    logger.info("This logs an info message.")
    return render(request, "volunteer/volunteer_create.html")
    



# <---------------------------------------- Beneficiary Views --------------------------------------------->
def beneficiarys_list(request):

    logger.info("This logs an info message.")
    return render(request, "beneficiary/beneficiary_list.html")


def beneficiary_create(request):

    logger.info("This logs an info message.")
    return render(request, "beneficiary/beneficiary_create.html")
    