from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import *

# Import logging from Python's standard library
import logging

# Create a logger for this file
logger = logging.getLogger(__file__)

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None and user.is_staff is True:
                login(request, user)
                return redirect("/index/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    
    logger.info("This logs an info message.")
    # return render(request, "accounts/login.html")
    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

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

def test(request):
    form = SignUpForm()
    context = {'form':form}
    return render(request, "test.html", context)

# def volunteers(request):
#     vol = Volunteer.objects.all()
#     context = {'vol': vol}
#     return render(request, "volunteer/volunteers_list", context)

# def volRegister(request):
    sform = SignUpForm()
    form = VolunteerForm()
    vol = Volunteer.objects.all()
    try:
        if request.method == 'POST':
            form = VolunteerForm(request.POST)
            if form.is_valid():
                email = sform.cleaned_data.get("email")
                vol_type = request.POST.get('vol_type')
                highest_eduction = request.POST.get('highest_eduction')
                educational_institution = request.POST.get('educational_institution')
                linkedIn_profile = request.POST.get('linkedIn_profile')
                facebook_profile = request.POST.get('facebook_profile')
                aadhar_card = request.POST.get('aadhar_card')
                current_occupation = request.POST.get('current_occupation')
                office_address = request.POST.get('office_address')
                check_profile = User.objects.filter(email=email).first()
                if check_profile:
                    context = {'message': 'User already exists',
                               'class': 'danger'}
                    return render(request, 'accounts/volunteer/volunteer_create.html', context)
                else:
                    with transaction.atomic():
                        sform.save()
                        user = User.objects.all().filter(email=email)
                        svol = Volunteer(user=user[0], vol_type=vol_type, highest_eduction=highest_eduction, educational_institution=educational_institution, linkedIn_profile=linkedIn_profile, facebook_profile=facebook_profile, aadhar_card=aadhar_card, current_occupation=current_occupation, office_address=office_address)
                        svol.save()
                        return redirect ('volunteer')
    except Exception as e:
        error = AaghazErrors.objects.create(functionName=volRegister, msg=e)
        pass
    context = { 'sform': sform, 'form': form, 'vol': vol }
    html_template = loader.get_template('volunteer/volunteer_create.html')
    return HttpResponse(html_template.render(context, request))