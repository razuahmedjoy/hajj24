
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users', UserListCreateAPIView.as_view(), name='users'),
    path('register', UserRegistrationAPIView.as_view(), name='register'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('tents', TentListCreateAPIView.as_view(), name='tent-list-create'),
    path('tents/<int:id>', TentRetrieveUpdateDestroyAPIView.as_view(), name='tent-retrieve-update-destroy'),

    path('cameras', CameraListCreateAPIView.as_view(), name='camera-list-create'),
    path('cameras/<int:pk>', CameraRetrieveUpdateDestroyAPIView.as_view(), name='camera-retrieve-update-destroy'),

]
