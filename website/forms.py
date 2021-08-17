from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator



class NewUserForm(UserCreationForm):
    name = forms.CharField(max_length=20, required=True)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=9, validators=[
        RegexValidator(
            r'^[0-9]{9}',
            message='Podaj 9 cyfr swojego numeru telefonu')])

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user