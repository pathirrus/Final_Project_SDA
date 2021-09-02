# Generated by Django 3.2.6 on 2021-09-02 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=60, verbose_name='Usługa')),
                ('price', models.IntegerField(verbose_name='Cena [zł]')),
                ('time_of_service', models.IntegerField(verbose_name='Czas [min]')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField(verbose_name='Data wizyty')),
                ('start_time_visit', models.TimeField(verbose_name='Godzina wizyty')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.service', verbose_name='Usługa')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Klient')),
            ],
        ),
    ]
