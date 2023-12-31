
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='users'),
    path('del-users/<str:email>/', UserDeleteByEmailAPIView.as_view(), name='users-delete'),
    path('register', UserRegistrationAPIView.as_view(), name='register'),
    path('login', UserLoginAPIView.as_view(), name='login'),
    path('tents', TentListCreateAPIView.as_view(), name='tent-list-create'),
    path('tent', TentWithDayMonthYear.as_view(), name='tent-list-create'),
    path('tents/<int:id>', TentRetrieveUpdateDestroyAPIView.as_view(), name='tent-retrieve-update-destroy'),

    path('cameras', CameraListCreateAPIView.as_view(), name='camera-list-create'),
    path('cameras/<str:sn>/', CameraRetrieveUpdateDestroyAPIView.as_view(), name='camera-retrieve-update-destroy'),
    path('counter-history', CounterHistoryListView.as_view(), name='counter-list-create'),
    path('counter-history/<int:pk>', CounterHistoryDetailView.as_view(), name='counter-detail'),
    path('camera-heartbeat', CameraHeartbeatListCreateView.as_view(), name='camera-heartbeat-list-create'),
    path('camera-heartbeat/<int:pk>/', CameraHeartbeatDetailView.as_view(), name='camera-heartbeat-detail'),
    path('register-camera-with-history/', CameraRegistrationWithHistoryView.as_view(), name='register-camera-with-history'),
    path('create-counter-history', CounterHistoryCreateAPIView.as_view(), name='create-counter-history'),
    path('create_picture/', PictureCreateView.as_view(), name='create-picture'),
    path('tent-counter',CounterHistoryByDateView.as_view(), name="tent-counter"),
    path('tent/<int:tent_id>/graph-counter-hour', CameraCounterHistoryGraphViewHour.as_view(), name="counter-hour"),
    path('tent/<int:tent_id>/graph-counter-day', CameraCounterHistoryGraphViewDay.as_view(), name="counter-day"),
    path('tent/<int:tent_id>/graph-counter-month', CameraCounterHistoryGraphViewMonth.as_view(), name="counter-month"),
]
