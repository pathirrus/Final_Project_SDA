from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import NewUser
from django.contrib.auth.models import User
from website.models import Service
from django.core.validators import RegexValidator
# from website.models import User


class NewUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField(max_length=30, required=False, label="Imię", help_text='Opcjonalnie.')

    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'first_name', 'password1', 'password2')

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('Musisz wprowadzić adres email'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



