#from django.contrib.auth.forms import UserCreationForm
from accounts.admin import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class RegistrationForm(UserCreationForm):
    class Meta:
        email = forms.EmailField(max_length=255)
        first_name = forms.CharField(max_length=255)
        last_name = forms.CharField(max_length=255)

        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

