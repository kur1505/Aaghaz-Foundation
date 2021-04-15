from django.urls import path, re_path
from Master import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('volunteer_master/', views.volunteer_master, name='volunteer_master'),
    path('beneficiary_master/', views.beneficiary_master, name='beneficiary_master'),
    path('country_master/', views.country_master, name='country_master'),
    path('donor_master/', views.donor_master, name='donor_master'),
    path('expense_master/', views.expense_master, name='expense_master'),
    path('grade_master/', views.grade_master, name='grade_master'),
    path('income_master/', views.income_master, name='income_master'),
    path('profession_master/', views.profession_master, name='profession_master'),
    path('zone_master/', views.zone_master, name='zone_master'),
]