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
    tent = models.ForeignKey(Tent, on_delete=models.SET_NULL, null=True, blank=True)
    heart_beat_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(verbose_name="created_at", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)

    def __str__(self):
        return f"{self.sn} - {self.tent.name if self.tent else 'No Tent'}"

class CounterHistory(models.Model):
    camera = models.ForeignKey(Camera, related_name='counter_histories', on_delete=models.CASCADE)
    sn = models.CharField(max_length=255)
    total_in = models.IntegerField(default=0)
    total_out = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)

class CameraHeartbeat(models.Model):
    camera = models.ForeignKey(Camera, related_name='heartbeats', on_delete=models.CASCADE)
    sn = models.CharField(max_length=255)
    version = models.IntegerField()
    ip_address = models.CharField(max_length=255)
    time_zone = models.IntegerField()
    hw_platform = models.CharField(max_length=255)
    time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)