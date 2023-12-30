# main_app/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.conf import settings

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, null=False, blank=False)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    sensor_update_permission = models.BooleanField(default=False)
    assigned_tent = models.ManyToManyField("Tent", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Tent(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    lat = models.CharField(max_length=255, null=False, blank=False)
    long = models.CharField(max_length=255, null=False, blank=False)
    location = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tents')
    created_at = models.DateTimeField(verbose_name="created_at",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at",auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Camera(models.Model):
    sn = models.CharField(max_length=255, unique=True)
    tent = models.ForeignKey(Tent, on_delete=models.SET_NULL, null=True, blank=True)
    heart_beat_time = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(verbose_name="created_at", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)
    status = models.BooleanField(default=False, help_text='Indicates if the camera is active or not')  # New field

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


# main_app/models.py
class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField('Image', related_name='pictures')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Image(models.Model):
    picture = models.ForeignKey(Picture, related_name='image_set', on_delete=models.CASCADE, default=1)  # Replace '1' with the ID of an existing Picture instance
    image = models.ImageField(upload_to='user_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)