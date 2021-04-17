# Generated by Django 3.1.5 on 2021-04-16 07:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AaghazErrors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('functionName', models.CharField(blank=True, max_length=100, null=True)),
                ('msg', models.TextField(blank=True, max_length=10000, null=True)),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date & Time')),
            ],
        ),
    ]
