import os
import uuid
from django.db import models
import qrcode
from coreApp.models import BaseModel
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from settings.settings import MEDIA_ROOT
# Create your models here.

class Newletter(BaseModel):
    nom       = models.CharField(max_length=255, null=True, blank=True)
    prenoms   = models.CharField(max_length=255, null=True, blank=True)
    subject   = models.CharField(max_length=255, null=True, blank=True)
    email     = models.CharField(max_length=255, null=True, blank=True)
    message   = models.TextField(default = "")



class Employe(BaseModel):
    nom           = models.CharField(max_length=255, null=True, blank=True)
    prenoms       = models.CharField(max_length=255,  null=True, blank=True)
    fonction      = models.CharField(max_length=255,  null=True, blank=True)
    code          = models.CharField(max_length=255,  null=True, blank=True)
    photo         = models.ImageField(max_length = 255, upload_to = "images/profiles/", default='images/profiles/default.png', null = True, blank=True)
    qrcode        = models.ImageField(max_length = 255, upload_to = "images/qrcodes/", default='images/qrcodes/default.png', null = True, blank=True)
    deleted       = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.nom + '_' + self.prenoms





@receiver(pre_save, sender=Employe)
def _(sender, instance, **kwargs):
    if instance._state.adding:
        instance.code = str(uuid.uuid4()).split('-')[-1].upper()


# @receiver(post_save, sender=Employe)
# def _(sender, instance, created, **kwargs):
#     if created:
#         img = qrcode.make(f"https://www.gstechnologie.com/admin/user/{instance.id}/")
#         instance.qrcode = os.path.join(MEDIA_ROOT, f"images/qrcodes/{instance.id}.png")
#         img.save(f"media/images/qrcodes/{instance.id}.png")
