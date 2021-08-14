from django.db import models


# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=9)

    def __str__(self):
        return self.name, self.surname


class Service(models.Model):
    service_name = models.CharField(max_length=120)
    price = models.IntegerField()
    time_of_service = models.FloatField()

    def __str__(self):
        return self.service_name
