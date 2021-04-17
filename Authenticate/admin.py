# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
# from django.contrib.auth.admin import UserAdmin
User = get_user_model()

from .forms import SignUpForm
# from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin
# from .forms import UserAdminCreationForm, UserAdminChangeForm

from .models import AaghazErrors, Volunteer



class CustomUserAdmin(BaseUserAdmin):

    add_form = SignUpForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('email','first_name', 'last_name','phone', 'is_staff', 'is_active','user_creation_date',)
    list_filter = ('email','first_name', 'last_name','phone','is_staff', 'is_active','user_creation_date',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'password', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Address', {'fields': ('addressline1', 'addressline2', 'country', 'city', 'pincode')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','phone',)
    ordering = ('email','phone',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



admin.site.register(User, CustomUserAdmin)
admin.site.register(Volunteer)

@admin.register(AaghazErrors)
class AaghazErrorsAdmin(admin.ModelAdmin):
    list_display = ('functionName','msg','timeStamp',)

# @admin.register(Volunteer)
# class ViewAdmin(ImportExportModelAdmin):
#     pass