# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from .models import *
from Master.models import *

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))


phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control",
                "name" : "email"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id" : "password1",
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id" : "password2",
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Phone Number",                
                "class": "form-control",
                "maxlength" : "10"
            }
        ))

    birth_date = forms.DateField(
        widget= forms.DateInput(
            attrs={
                "placeholder" : "Date Of Birth",                
                "class": "form-control js-datepicker"
            }
        )
    )

    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Gender",                
                "class": "form-control"
            }
        ))

    addressline1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Address Line1",                
                "class": "form-control"
            }
        ))
    addressline2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "id" : "add2",
                "placeholder" : "Optional",                
                "class": "form-control"
            }
        ))
    city = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "City",                
                "class": "form-control"
            }
        )
    )
    pincode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Pincode",                
                "class": "form-control",
                "maxlength" : "6"
            }
        ))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'gender', 'birth_date' , 'password1', 'password2', 'phone', 'addressline1', 'addressline2', 'city', 'pincode',)

class VolunteerForm(forms.ModelForm):
    vol_type = forms.ModelChoiceField(
        queryset=VolunteerMaster.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "placeholder" : "Volunteer Type",                
                "class": "form-control",
                "name" : "vol_type"
            }
        ))
    highest_eduction = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Highest Education",                
                "class": "form-control",
                "name" : "highest_eduction"
            }
        ))
    educational_institution = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Educational Institution",                
                "class": "form-control",
                "name" : "educational_institution"
            }
        ))
    linkedIn_profile = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "LinkedIn Profile Url",                
                "class": "form-control",
                "name" : "linkedIn_profile"
            }
        ))
    facebook_profile = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Facebook Profile Url",                
                "class": "form-control",
                "name" : "facebook_profile"
            }
        ))
    aadhar_card = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Aadhar card",                
                "class": "form-control",
                "name" : "aadhar_card",
                "maxlength" : "12"
            }
        ))
    current_occupation = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Current Occupation",                
                "class": "form-control",
                "name" : "current_occupation"
            }
        ))
    office_address = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Office Address",                
                "class": "form-control",
                "name" : "office_address"
            }
        ))
    class Meta:
        model = Volunteer
        fields = ('vol_type', 'highest_eduction', 'educational_institution', 'linkedIn_profile', 'facebook_profile', 'aadhar_card', 'current_occupation', 'office_address',)

