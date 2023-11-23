from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name=_("Prénom"))
    last_name = models.CharField(max_length=30, verbose_name=_("Nom"))
    birth_date = models.DateField(null=True, blank=True, verbose_name=_("Date de Naissance"))
    email = models.EmailField(unique=True, verbose_name=_("Adresse E-mail"))
    image = models.ImageField(_("Image"), upload_to='products/', null=True, blank=True)

