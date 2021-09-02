import datetime
from django.db import models
from django.shortcuts import reverse
from accounts.models import NewUser


# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=60, verbose_name="Usługa")
    price = models.IntegerField(verbose_name="Cena [zł]")
    time_of_service = models.IntegerField(verbose_name="Czas [min]")

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return reverse('website:services')


class Reservation(models.Model):
    user_id = models.OneToOneField(NewUser, on_delete=models.CASCADE, verbose_name="Klient")
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Usługa")
    visit_date = models.DateField(verbose_name="Data wizyty")
    start_time_visit = models.TimeField(verbose_name="Godzina wizyty")

    def __str__(self):
        return f"{self.user_id} {self.visit_date} na {self.service_id}"



