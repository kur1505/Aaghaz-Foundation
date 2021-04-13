# from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from django.utils import timezone
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save
# from .utils import generate_ref_code, generate_sr_code, generate_emp_code
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

# Create your models here.

