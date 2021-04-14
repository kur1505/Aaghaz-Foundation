from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django import template
from django.template import loader
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages
from .models import *

# Create your views here.
@csrf_protect
def volunteer_master(request):
    query = VolunteerMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('vol_type')
            pk = request.POST.get('pk')
            print('Volunteer id is PK',pk)
            if pk =='':
                create_query = VolunteerMaster.objects.create(volunteer_type=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                vol = VolunteerMaster.objects.all().filter(pk=pk)
                print('Delete pk is', vol)
                vol.delete()
                msg = 'Data is deleted successfully'
        
            else:
                vol = VolunteerMaster.objects.all().filter(pk=pk)
                vol.update(volunteer_type=data_type)
                msg = 'Data is updated successfully'
                print('Volunteer is', vol)
            context = {'msg': msg,'success':True,'url':'/master/volunteer_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/volunteer_master.html')
    return HttpResponse(html_template.render(context, request))


def country_master(request):
    query = CountryMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Country id is PK',pk)
            if pk =='':
                create_query = CountryMaster.objects.create(country_name=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                con = CountryMaster.objects.all().filter(pk=pk)
                print('Delete pk is', con)
                con.delete()
                msg = 'Data is deleted successfully'
        
            else:
                con = CountryMaster.objects.all().filter(pk=pk)
                con.update(country_name=data_type)
                print('Country is', con)
                msg = 'Data is updated successfully'
            context = {'msg': 'msg','success':True,'url':'/master/country_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/country_master.html')
    return HttpResponse(html_template.render(context, request))


def beneficiary_master(request):
    query = BeneficiaryMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('ben_type')
            pk = request.POST.get('pk')
            print('Beneficiary is PK',pk)
            if pk =='':
                create_query = BeneficiaryMaster.objects.create(beneficiary_type=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                ben = BeneficiaryMaster.objects.all().filter(pk=pk)
                print('Delete pk is', ben)
                ben.delete()
                msg = 'Data is deleted successfully'
        
            else:
                ben = BeneficiaryMaster.objects.all().filter(pk=pk)
                ben.update(beneficiary_type=data_type)
                print('Beneficiary is updated', ben)
                msg = 'Data is updated successfully'
            context = {'msg': msg,'success':True,'url':'/master/beneficiary_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/beneficiary_master.html')
    return HttpResponse(html_template.render(context, request))


def donor_master(request):
    query = DonorMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Donor id is PK',pk)
            if pk =='':
                create_query = DonorMaster.objects.create(donor_type=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                donor = DonorMaster.objects.all().filter(pk=pk)
                print('Delete pk is', donor)
                donor.delete()
                msg = 'Data is deleted successfully'
        
            else:
                donor = DonorMaster.objects.all().filter(pk=pk)
                donor.update(donor_type=data_type)
                print('Donor is', donor)
                msg = 'Data is updated successfully'
            context = {'msg': msg,'success':True,'url':'/master/donor_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/donor_master.html')
    return HttpResponse(html_template.render(context, request))


def expense_master(request):
    query = ExpenseMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Expense id is PK',pk)
            if pk =='':
                create_query = ExpenseMaster.objects.create(expense_type=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                expense = ExpenseMaster.objects.all().filter(pk=pk)
                print('Delete pk is', expense)
                expense.delete()
                msg = 'Data is deleted successfully'
        
            else:
                expense = ExpenseMaster.objects.all().filter(pk=pk)
                expense.update(expense_type=data_type)
                print('Expense is', expense)
                msg = 'Data is updated successfully'
            context = {'msg': msg,'success':True,'url':'/master/expense_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/expense_master.html')
    return HttpResponse(html_template.render(context, request))


def grade_master(request):
    query = GradeMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Grade master id is PK',pk)
            if pk =='':
                create_query = GradeMaster.objects.create(grade_type=data_type)
                msg =  'Your data is saved successfully'
            elif pk != '' and data_type == '':
                grdm = GradeMaster.objects.all().filter(pk=pk)
                print('Delete pk is', grdm)
                grdm.delete()
                msg = 'Data is deleted successfully'
            else:
                grdm = GradeMaster.objects.all().filter(pk=pk)
                grdm.update(grade_type=data_type)
                msg =  'Your data is updated successfully'
                print('Grade master is', grdm)
            context = {'msg': msg,'success':True,'url':'/master/grade_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/grade_master.html')
    return HttpResponse(html_template.render(context, request))


def income_master(request):
    query = IncomeMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Income master id is PK',pk)
            if pk =='':
                create_query = IncomeMaster.objects.create(income_type=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                income = IncomeMaster.objects.all().filter(pk=pk)
                print('Delete pk is', ben)
                income.delete()
                msg = 'Data is deleted successfully'
        
            else:
                income = IncomeMaster.objects.all().filter(pk=pk)
                income.update(income_type=data_type)
                print('Income master is', income)
                msg = 'Data is updated successfully'
            context = {'msg': msg,'success':True,'url':'/master/income_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/income_master.html')
    return HttpResponse(html_template.render(context, request))


def profession_master(request):
    query = ProfessionMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Profession master id is PK',pk)
            if pk =='':
                create_query = ProfessionMaster.objects.create(profession_type=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                prof = ProfessionMaster.objects.all().filter(pk=pk)
                print('Delete pk is', prof)
                prof.delete()
                msg = 'Data is deleted successfully'
        
            else:
                prof = ProfessionMaster.objects.all().filter(pk=pk)
                prof.update(profession_type=data_type)
                print('Profession master is', prof)
                msg = 'Data is updated successfully'
            context = {'msg': msg,'success':True,'url':'/master/profession_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/profession_master.html')
    return HttpResponse(html_template.render(context, request))


def zone_master(request):
    query = ZoneMaster.objects.all()
    msg = None
    try:
        if request.method == 'POST':
            data_type = request.POST.get('data_type')
            pk = request.POST.get('pk')
            print('Zone master id is PK',pk)
            if pk =='':
                create_query = ZoneMaster.objects.create(zone_name=data_type)
                msg = 'Data is created successfully'
            elif pk != '' and data_type == '':
                zone = ZoneMaster.objects.all().filter(pk=pk)
                print('Delete pk is', zone)
                zone.delete()
                msg = 'Data is deleted successfully'
        
            else:
                zone = ZoneMaster.objects.all().filter(pk=pk)
                zone.update(zone_name=data_type)
                print('Zone master is', zone)
                msg = 'Data is updated successfully'
            context = {'msg': msg,'success':True,'url':'/master/zone_master/'}
            html_template = loader.get_template('includes/alert.html')
            return HttpResponse(html_template.render(context, request))
        else:
            print('Error')
    except Exception as e:
        print(e)

    context = {'query': query }
    html_template = loader.get_template('master/zone_master.html')
    return HttpResponse(html_template.render(context, request))