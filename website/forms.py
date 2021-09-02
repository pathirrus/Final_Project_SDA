from django.contrib.auth.forms import UserCreationForm
from accounts.models import NewUser
from website.models import Reservation
from django import forms


class NewUserForm(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'first_name', 'password1', 'password2')

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('Musisz wprowadzić adres email'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = [
            'service_id',
            'visit_date',
            'start_time_visit',

        ]

