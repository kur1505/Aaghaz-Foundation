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
from django.template import loader
User = get_user_model()
from Authenticate.models import *
from Authenticate.forms import *
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
    sform = SignUpForm()
    form = VolunteerForm()
    vol = Volunteer.objects.all()
    try:
        if request.method == 'POST':
            print('Request is ', request.POST)
            form = VolunteerForm(request.POST)
            if form.is_valid():
                # email = sform.cleaned_data.get("email")
                print('Form is ', sform)
                sform.save()
                email = request.POST.get('email')
                vol_type = request.POST.get('vol_type')
                highest_eduction = request.POST.get('highest_eduction')
                educational_institution = request.POST.get('educational_institution')
                linkedIn_profile = request.POST.get('linkedIn_profile')
                facebook_profile = request.POST.get('facebook_profile')
                aadhar_card = request.POST.get('aadhar_card')
                current_occupation = request.POST.get('current_occupation')
                office_address = request.POST.get('office_address')
                print('Working till here')
                check_profile = User.objects.filter(email=email).first()
                if check_profile:
                    context = {'message': 'User already exists',
                               'class': 'danger'}
                    return render(request, 'volunteer/volunteer_create.html', context)
                else:
                    with transaction.atomic():
                        print('Working till here 1')
                        user = User.objects.all().filter(email=email)
                        svol = Volunteer(user=user[0], vol_type=vol_type, highest_eduction=highest_eduction, educational_institution=educational_institution, linkedIn_profile=linkedIn_profile, facebook_profile=facebook_profile, aadhar_card=aadhar_card, current_occupation=current_occupation, office_address=office_address)
                        print('Working till here 2')
                        svol.save()
                        print('Working till here 3')
                        return redirect ('volunteer')
    except Exception as e:
        error = AaghazErrors.objects.create(functionName=volunteer_create, msg=e)
        pass
    context = { 'sform': sform, 'form': form, 'vol': vol }

    logger.info("This logs an info message.")
    # return render(request, "volunteer/volunteer_create.html")
    html_template = loader.get_template('volunteer/volunteer_create.html')
    return HttpResponse(html_template.render(context, request))
    



# <---------------------------------------- Beneficiary Views --------------------------------------------->
def beneficiarys_list(request):

    logger.info("This logs an info message.")
    return render(request, "beneficiary/beneficiary_list.html")


def beneficiary_create(request):

    logger.info("This logs an info message.")
    return render(request, "beneficiary/beneficiary_create.html")
    