# Generated by Django 3.1.5 on 2021-04-12 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficiarymaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='countrymaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='donormaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='expensemaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='grademaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='incomemaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='professionmaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='volunteermaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
        migrations.AddField(
            model_name='zonemaster',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date and Time'),
        ),
    ]
