# Generated by Django 3.1.5 on 2021-04-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0005_auto_20210416_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='vol_ID',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Volunteer ID'),
        ),
    ]
