# main_app/models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tent(models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Camera(models.Model):

    sn = models.CharField(max_length=255)
    tent = models.ForeignKey(Tent, on_delete=models.CASCADE, related_name='cameras')

    def __str__(self):
        # return sn + ' - ' + tent.name
        return self.sn + ' - ' + self.tent.name

