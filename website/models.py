import copy
import datetime

from django.db import models
from django.shortcuts import reverse

from accounts.models import NewUser


OPEN_HOUR, OPEN_MINUTE, CLOSE_HOUR, CLOSE_MINUTE = 9, 0, 18, 0
TIME_INTERVAL = 30


class Service(models.Model):
    service_name = models.CharField(max_length=60, verbose_name="Usługa")
    price = models.IntegerField(verbose_name="Cena [zł]")
    time_of_service = models.IntegerField(verbose_name="Czas [min]")

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return reverse('website:services')


class Reservation(models.Model):
    user_id = models.ForeignKey(NewUser, on_delete=models.CASCADE, verbose_name="Klient")
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Usługa")
    visit_date = models.DateField(verbose_name="Data wizyty")
    start_time_visit = models.TimeField(verbose_name="Godzina wizyty")

    def get_available_hours(self, service_id, visit_date):
        """
            Returns list of available hours. Takes into account opening and
            closing hours, saturdays and sundays as well as time of request.
                Parameters:
                    service_id (int): Id of the service
                    visit_date (str): Requested visit day
                Returns:
                    available_hours (List[Tuple]): List of available hours in format
                                                    suitable for select html element.
        """

        service_time = Service.objects.get(id=service_id).time_of_service
        visit_date = datetime.datetime.strptime(visit_date, '%Y-%m-%d').date()

        now = datetime.datetime.now()

        all_dates = []
        available_dates = []

        if (
                visit_date >= now.date() and
                visit_date.weekday() != 5 and
                visit_date.weekday() != 6
        ):

            if visit_date == now.date():
                open_date = now + datetime.timedelta(hours=1)
                open_date = self.round_date_time(open_date, datetime.timedelta(minutes=TIME_INTERVAL))

            else:
                open_date = datetime.datetime(
                    year=visit_date.year,
                    month=visit_date.month,
                    day=visit_date.day,
                    hour=OPEN_HOUR,
                    minute=OPEN_MINUTE
                )

            close_date = datetime.datetime(
                year=visit_date.year,
                month=visit_date.month,
                day=visit_date.day,
                hour=CLOSE_HOUR,
                minute=CLOSE_MINUTE
            ) - datetime.timedelta(minutes=service_time)

            tmp_date = open_date
            while tmp_date <= close_date:
                all_dates.append(tmp_date)
                tmp_date += datetime.timedelta(minutes=TIME_INTERVAL)

            booked_hours = Reservation.objects.filter(
                service_id=service_id,
                visit_date=visit_date
            ).values_list('start_time_visit', flat=True)

            booked_dates = [
                datetime.datetime(
                    year=visit_date.year,
                    month=visit_date.month,
                    day=visit_date.day,
                    hour=item.hour,
                    minute=item.minute,
                )
                for item in booked_hours
            ]

            available_dates = copy.deepcopy(all_dates)

            for booked_date in booked_dates:
                for date in all_dates:

                    if (
                            booked_date - datetime.timedelta(minutes=service_time)
                            < date <
                            booked_date + datetime.timedelta(minutes=service_time)
                    ):
                        available_dates.remove(date)

        available_hours = [
            (
                '{:02d}:{:02d}:00'.format(item.hour, item.minute),
                '{:02d}:{:02d}'.format(item.hour, item.minute)
            ) for item in available_dates
        ]

        return available_hours

    @staticmethod
    def round_date_time(date_time, delta):
        return date_time + (date_time.min - date_time) % delta