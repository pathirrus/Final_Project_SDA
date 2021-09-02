from .models import NewUser
from django.forms import ModelForm


class ProfileEditForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ('user_name',
                  'first_name',
                  'last_name',
                  'phone_number',
                  )
