# Dans votre fichier forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(label=_("Date de naissance"))

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2']
        labels = {
            'first_name': _('Nom'),
            'last_name': _('Prénom'),
            'email': _('Adresse e-mail'),
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
