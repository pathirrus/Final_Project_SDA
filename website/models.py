from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=9, validators=[RegexValidator(r'^[0-9]{9}', message='Podaj 9 cyfr swojego numeru telefonu')])

    def __str__(self):
        return f"{self.name}, {self.surname}, telefon: {self.phone_number}"


class Service(models.Model):
    service_name = models.CharField(max_length=120)
    price = models.IntegerField()
    time_of_service = models.FloatField()

    def __str__(self):
        return self.service_name
