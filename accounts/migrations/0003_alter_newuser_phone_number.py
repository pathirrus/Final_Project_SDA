# Generated by Django 3.2.6 on 2021-08-28 09:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210826_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(message='Wprowadź prawidłowy numer telefonu', regex='^[0-9]{9}$')], verbose_name='Numer telefonu'),
        ),
    ]
