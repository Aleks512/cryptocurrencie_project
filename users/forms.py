from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(label=_("Date de naissance"), widget=forms.DateInput(attrs={'type': 'date'}))

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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']