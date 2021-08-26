from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website.models import Service
from django.core.validators import RegexValidator
# from website.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, label="Imię", help_text='Opcjonalnie.')
    last_name = forms.CharField(max_length=30, required=False, label="Nazwisko", help_text='Opcjonalnie.')
    phone = forms.CharField(max_length=9, validators=[RegexValidator('^[0-9]{9}$', message='Nieprawidłowy numer telefonu')], required=False, label="Telefon", help_text='Opcjonalnie.')

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user





