from django.utils import timezone
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class VolunteerMaster(models.Model):
    volunteer_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.volunteer_type}'

class BeneficiaryMaster(models.Model):
    beneficiary_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.beneficiary_type}'

class DonorMaster(models.Model):
    donor_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.donor_type}'

class CountryMaster(models.Model):
    country_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.country_name}'

class ZoneMaster(models.Model):
    zone_name = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.zone_name}'

class ExpenseMaster(models.Model):
    expense_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.expense_type}'

class IncomeMaster(models.Model):
    income_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.income_type}'

class GradeMaster(models.Model):
    grade_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.grade_type}'

class ProfessionMaster(models.Model):
    profession_type = models.CharField(max_length=100)
    create_date = models.DateTimeField(_("Date and Time"),default=timezone.now)

    def __str__(self):
        return f'{self.profession_type}'

