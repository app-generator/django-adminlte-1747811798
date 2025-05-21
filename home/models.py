# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Auftragsstatus(models.Model):

    #__Auftragsstatus_FIELDS__
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)

    #__Auftragsstatus_FIELDS__END

    class Meta:
        verbose_name        = _("Auftragsstatus")
        verbose_name_plural = _("Auftragsstatus")


class Kontaktdatenbank(models.Model):

    #__Kontaktdatenbank_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Kontaktdatenbank_FIELDS__END

    class Meta:
        verbose_name        = _("Kontaktdatenbank")
        verbose_name_plural = _("Kontaktdatenbank")


class Auftragsdatenbank(models.Model):

    #__Auftragsdatenbank_FIELDS__
    status = models.ForeignKey(Auftragsstatus, on_delete=models.CASCADE)
    kunde = models.ForeignKey(Kontaktdatenbank, on_delete=models.CASCADE)

    #__Auftragsdatenbank_FIELDS__END

    class Meta:
        verbose_name        = _("Auftragsdatenbank")
        verbose_name_plural = _("Auftragsdatenbank")



#__MODELS__END
