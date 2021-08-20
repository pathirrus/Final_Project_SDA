from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="Imię")
    surname = models.CharField(max_length=30, verbose_name="Nazwisko")
    email = models.EmailField()
    phone_number = models.CharField(max_length=9, verbose_name="Telefon")

    def __str__(self):
        return f"{self.name}, {self.surname}, telefon: {self.phone_number}"


class Service(models.Model):
    service_name = models.CharField(max_length=120, verbose_name="Usługa")
    price = models.IntegerField(verbose_name="Cena [zł]")
    time_of_service = models.FloatField(verbose_name="Czas [h]")

    def __str__(self):
        return self.service_name


class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Klient")
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Usługa")
    visit_date = models.DateTimeField(verbose_name="Termin wizyty")

    def __str__(self):
        return f"{self.user_id} na {self.service_id}"
