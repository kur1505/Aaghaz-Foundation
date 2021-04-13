# Generated by Django 3.1.5 on 2021-04-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0002_auto_20210412_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiarymaster',
            name='beneficiary_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='countrymaster',
            name='country_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='donormaster',
            name='donor_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expensemaster',
            name='expense_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='grademaster',
            name='grade_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='incomemaster',
            name='income_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='professionmaster',
            name='profession_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteermaster',
            name='volunteer_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='zonemaster',
            name='zone_name',
            field=models.CharField(max_length=100),
        ),
    ]
