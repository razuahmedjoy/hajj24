# main_app/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

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
    sn = models.CharField(max_length=255, unique=True)
    tent = models.ForeignKey('Tent', on_delete=models.SET_NULL, null=True, blank=True)
    heart_beat_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(verbose_name="created_at", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)

    def __str__(self):
        return f"{self.sn} - {self.tent.name if self.tent else 'No Tent'}"

