# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime, date


import random


class UserManager(BaseUserManager):
   
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)

gender_choices=(
    ("0","Male"),
    ("1","Female"),
    ("2","Transgender"),
    ("3","Other"),
)

class User(AbstractUser):  
    username = None
    email = models.EmailField(_('email address'), null=True, blank=True, unique=True)
    phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
    phone       = models.CharField('Phone',validators =[phone_regex], max_length=10, null=True, unique=True)
    birth_date = models.DateTimeField(_("DOB"), auto_now=False, auto_now_add=False, null=True)
    gender = models.CharField(_('Gender'), choices=gender_choices, max_length=50, null=True)
    addressline1 = models.CharField(max_length=50, null=True)
    addressline2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(_("City"), max_length=50, null=True)
    pincode = models.CharField(_("Pincode"),max_length=6, null=True)
    user_creation_date= models.DateTimeField(_("Date & Time"),default=timezone.now)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone