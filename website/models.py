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
    user_id = models.OneToOneField(NewUser, on_delete=models.CASCADE, verbose_name="Klient")
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Usługa")
    visit_date = models.DateField(verbose_name="Data wizyty")
    start_time_visit = models.TimeField(verbose_name="Godzina wizyty")

    def __str__(self):
        return f"{self.user_id} {self.visit_date} na {self.service_id}"

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

        # Wyciągamy z bazy czas trwania wybranej przez użytkownika usługi
        service_time = Service.objects.get(id=service_id).time_of_service
        # Konwertujemy wybraną przez użytkownika datę do obiektu date
        visit_date = datetime.datetime.strptime(visit_date, '%Y-%m-%d').date()

        # Aktualny czas i data
        now = datetime.datetime.now()

        all_dates = []
        available_dates = []

        # Przetwarzam dalej tylko jeżeli data, wybrana przez użytkownika jest większa
        # lub równa dniu dzisiejszemu i wskazana data to nie jest sobota lub niedziela.
        # Czyli jeżeli użytkownik zaznaczył datę przeszłą, sobotę lub niedzielę
        # to przechodzimy na sam koniec metody i tam zwracamy pustą listę available_hours
        if (
                visit_date >= now.date()
                and
                (visit_date.weekday != 6 or visit_date.weekday != 7)
        ):

            # Krok 1 - generujemy listę wszystkich terminów

            # Najperw tworzę listę wszystkich dostępnych godzin.
            # Filtrować ją (tzn. usuwać z tej listy zabukowane terminy będziemy
            # w drugim kroku

            # jeżeli zaznaczona data to dzień dzisiejszy, to uwzględniamy aktualną
            # godziną. Pierwsza dostępna godzina rezerwacji to godzina po aktualnej
            # godzinie (zakładamy, że użytkownik może rezerwować wizytę z conajmniej
            # godzinnym wyprzedzeniem)
            if visit_date == now.date():
                open_date = now + datetime.timedelta(hours=1)
                open_date = self.round_date_time(open_date, datetime.timedelta(minutes=TIME_INTERVAL))
            # w przeciwnym razie pierwsza dostępna godzina rezerwacji to godzina
            # otwarcia
            else:
                open_date = datetime.datetime(
                    year=visit_date.year,
                    month=visit_date.month,
                    day=visit_date.day,
                    hour=OPEN_HOUR,
                    minute=OPEN_MINUTE
                )

            # Ostatnia godzina rezerwacji to godzina zamknięcia minus czas trwania
            # wybranego zabiegu.
            close_date = datetime.datetime(
                year=visit_date.year,
                month=visit_date.month,
                day=visit_date.day,
                hour=CLOSE_HOUR,
                minute=CLOSE_MINUTE
            ) - datetime.timedelta(minutes=service_time)

            # Wypełniamy listę all_dates datami z zakresu open_date
            # close_date z krokiem TIME_INTERVAL
            tmp_date = open_date
            while tmp_date <= close_date:
                all_dates.append(tmp_date)
                tmp_date += datetime.timedelta(minutes=TIME_INTERVAL)

            # Krok 2 - przefiltrowanie wszystkich terminów, wyrzucenie tych
            # już zarezerwowanych.

            # Wyciągamy z bazy zarezerwowane we wskazanym dniu terminy.
            booked_hours = Reservation.objects.filter(
                service_id=service_id,
                visit_date=visit_date
            ).values_list('start_time_visit', flat=True)

            # Konwertujemy wyciągnięte z bazy informacje do obiektów datatime
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

            # Kopiuję wszystkie terminy (z kopii będę wyrzucał już zarezerwowane)
            available_dates = copy.deepcopy(all_dates)

            # Iterujemy po zarezerowanych terminach
            for booked_date in booked_dates:
                for date in all_dates:
                    # Dla każdego zarezerowanego terminy kopii wyrzucamy wszystkie
                    # terminy z przedziału (zarezerwowany termin - czas usługi,
                    # zarezerowowany + czas usługi)
                    if (
                            booked_date - datetime.timedelta(minutes=service_time)
                            < date <
                            booked_date + datetime.timedelta(minutes=service_time)
                    ):
                        available_dates.remove(date)

        # Otrzymaną w ten sposób (poprzez wyrzucenie zarezerwowanych terminów)
        # listę dostępnych terminów - available_dates
        # konwertuję do formatu odpowiadającego tagowi option (html), tj.
        # <select>
        #   <option value=pierwsza_wartość_z_tupli>druga_wartość_z_tupli</option>
        #    ...
        #<select>
        # Jeżeli available_dates puste to available_hours też będzie puste.
        available_hours = [
            (
                '{:02d}:{:02d}:00'.format(item.hour, item.minute),
                '{:02d}:{:02d}'.format(item.hour, item.minute)
            ) for item in available_dates
        ]

        # listę zwracamy (będziemy dalej wykorzystywali ją w widoku)
        return available_hours

    # Metoda statyczna oznacza tylko tyle, że nie wykorzystujemy w niej
    # w żaden sposób instancji klasy (więc nie potrzebujemy self w tej metodzie).
    # Tzn. że ta metoda w żaden sposób nie modyfikuje/wpływa na obiekt klasy.
    # W sumie get_available_hours też może być statyczna.
    @staticmethod
    def round_date_time(date_time, delta):
        return date_time + (date_time.min - date_time) % delta
