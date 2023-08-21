from django.db import models

# Create your models here.

class Newletter(models.Model):
    pass



class Employe(models.Model):
    nom       = models.CharField(max_length=255, null=True, blank=True)
    prenoms   = models.CharField(max_length=255,  null=True, blank=True)
    fonction  = models.CharField(max_length=255,  null=True, blank=True)
    code      = models.IntegerField(null=True, blank=True, default=0)
    photo     = models.IntegerField(null=True, blank=True, default=0)
    qrcode    = models.IntegerField(null=True, blank=True, default=0)
    started   = models.IntegerField(null=True, blank=True, default=0)
