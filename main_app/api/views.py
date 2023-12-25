# main_app/views.py

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.authtoken.models import Token
from main_app.models import *
from .serializers import *
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db.models import Prefetch, Sum, Count
from datetime import date, timedelta
from django.db.models import Count, Sum, Avg, F, Case, Q, When, ExpressionWrapper
from django.db.models.functions import (
    ExtractDay,
    ExtractMonth,
    ExtractMinute,
    ExtractYear,
    ExtractHour,
    Cast,
)
from datetime import datetime, timedelta
from collections import Counter
from calendar import monthrange
import calendar
from rest_framework.authtoken.models import Token
from django.db import models

from django.utils import timezone

import json

User = get_user_model()

#  create a userList api view from where we can get all the users and create a new user
@method_decorator(csrf_protect, name='dispatch')
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk, 'email': user.email}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk, 'email': user.email}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# @permission_classes([IsAuthenticated])
class TentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        month = self.request.query_params.get('month')
        year = self.request.query_params.get('year')

        if month and year:
            queryset = queryset.filter(Q(updated_at__month=month) & Q(updated_at__year=year))

        return queryset

class TentWithDayMonthYear(generics.ListCreateAPIView):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        value = self.request.query_params.get('value')
        print(value)

        if "day"== value:
            today = timezone.now().date()
            queryset = queryset.filter(updated_at__date=today)

        elif "week" == value:
            last_week = timezone.now().date() - timedelta(days=7)
            queryset = queryset.filter(updated_at__date__gte=last_week)

        elif "month" == value:
            last_month = timezone.now().date() - timedelta(days=30)
            queryset = queryset.filter(updated_at__date__gte=last_month)

        elif "year" == value:
            last_year = timezone.now().date() - timedelta(days=365)
            queryset = queryset.filter(updated_at__date__gte=last_year)
        return queryset

class TentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CameraListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CameraDetailSerializer

    def get_queryset(self):
        camera_id = self.request.query_params.get('id')
        queryset = Camera.objects.all()

        if camera_id:
            queryset = queryset.filter(id=camera_id)

        queryset = queryset.prefetch_related(
            Prefetch('counter_histories', queryset=CounterHistory.objects.all()),
            Prefetch('heartbeats', queryset=CameraHeartbeat.objects.all())
        )
        
        return queryset

class CameraRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraDetailSerializer
    lookup_field = 'sn'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        counter_histories = instance.counterhistory_set.all()
        heartbeat_data = instance.cameraheartbeat_set.all()
        counter_history_serializer = CreateCounterHistorySerializer(counter_histories, many=True)
        heartbeat_serializer = CreateHeartbeatSerializer(heartbeat_data, many=True)
        serializer_data = serializer.data
        serializer_data['counter_histories'] = counter_history_serializer.data
        serializer_data['heartbeats'] = heartbeat_serializer.data

        return Response(serializer_data)

class CounterHistoryListView(APIView):
    def get(self, request):
        try:
            counter_histories = CounterHistory.objects.all()
            serializer = CounterHistorySerializer(counter_histories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CounterHistoryListCreateView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CreateCounterHistorySerializer

    def get_queryset(self):
        camera_sn = self.request.query_params.get('camera', None)
        if camera_sn is not None:
            return CounterHistory.objects.filter(camera__sn=camera_sn)
        else:
            return CounterHistory.objects.all()

    def post(self, request, *args, **kwargs):
        camera_id = request.data.get('camera')
        sn = request.data.get('sn')
        camera = get_object_or_404(Camera, id=camera_id, sn=sn)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['camera'] = camera.id
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CounterHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CounterHistory.objects.all()
    serializer_class = CreateCounterHistorySerializer

class CameraHeartbeatDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CameraHeartbeat.objects.all()
    serializer_class = CreateHeartbeatSerializer


# ==========================================================



class CameraRegistrationWithHistoryView(APIView):

    def post(self, request, *args, **kwargs):
        sn = request.data.get('sn')
        tent_id = request.data.get('tent')
        tent = get_object_or_404(Tent, id=tent_id)
        if not tent:
            return Response({"detail": "Tent with this ID does not exist."},
                            status=status.HTTP_400_BAD_REQUEST)
        existing_camera = Camera.objects.filter(sn=sn).first()
        if existing_camera:
            return Response({"detail": "Camera with this serial number is already registered."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = CameraSerializer(data={'sn': sn, 'tent': tent.id, 'heart_beat_time': timezone.now()})
        if serializer.is_valid():
            camera = serializer.save()
            counter_history_data = {
                'camera': camera.id,
                'sn': sn,
                'start_time': timezone.now(),
                'end_time': None,
                'total_in': 0,
                'total_out': 0,
                'total': 0
            }
            counter_history_serializer = CreateCounterHistorySerializer(data=counter_history_data)
            if counter_history_serializer.is_valid():
                counter_history_serializer.save()
            else:
                return Response(counter_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            heartbeat_data = {
                'camera': camera.id,
                'sn': sn,
                'version': 1,
                'ip_address': request.META['REMOTE_ADDR'],
                'time_zone': 0,
                'hw_platform': "unknown",
                'report_date': timezone.now().date(),
                'time': timezone.now()
            }
            heartbeat_serializer = CreateHeartbeatSerializer(data=heartbeat_data)
            if heartbeat_serializer.is_valid():
                heartbeat_serializer.save()
            else:
                return Response(heartbeat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CounterHistoryCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        sn = request.data.get('sn')
        camera = get_object_or_404(Camera, sn=sn)
        
        counter_history_data = {
            'camera': camera.id,
            'sn': sn,
            'start_time': request.data.get('start_time'),
            'end_time': request.data.get('end_time'),
            'total_in': request.data.get('total_in', 0),
            'total_out': request.data.get('total_out', 0),
            'total': request.data.get('total', 0)
        }

        counter_history_serializer = CreateCounterHistorySerializer(data=counter_history_data)

        if counter_history_serializer.is_valid():
            counter_history_serializer.save()
            return Response(counter_history_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(counter_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CameraHeartbeatListCreateView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CameraHeartbeat.objects.all()
    serializer_class = CreateHeartbeatSerializer

    def post(self, request, *args, **kwargs):
        sn = request.data.get('sn')
        camera = get_object_or_404(Camera, sn=sn)
        
        heartbeat_data = {
            'sn': sn,
            'version': request.data.get('version'),
            'ip_address': request.data.get('ip_address'),
            'time_zone': request.data.get('time_zone'),
            'hw_platform': request.data.get('hw_platform'),
            'time': request.data.get('time', None),
        }

        heartbeat_serializer = CreateHeartbeatSerializer(data=heartbeat_data)

        if heartbeat_serializer.is_valid():
            camera.heart_beat_time = timezone.now()
            camera.save()
            validated_data = heartbeat_serializer.validated_data
            validated_data['camera'] = camera

            heartbeat = CameraHeartbeat.objects.create(**validated_data)

            return Response(heartbeat_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(heartbeat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PictureCreateView(generics.CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CounterHistoryByDateView(APIView):
    def get(self, request):
        try:
            tent_id = request.query_params.get('tent', None)
            if not tent_id:
                return Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)

            tent_history = CounterHistory.objects.filter(
                camera__tent_id=tent_id,
            ).values("camera").annotate(
                totals_in=Sum("total_in"),
                totals_out=Sum("total_out"),
            )

            camera_data = []
            total_in_sum = 0
            total_out_sum = 0

            for entry in tent_history:
                camera_id = entry['camera']
                camera = Camera.objects.get(id=camera_id)
                serializer = CameraSerializer(camera)
                camera_status = serializer.data['status']

                total_in_sum += entry['totals_in']
                total_out_sum += entry['totals_out']

                camera_entry = {
                    'camera': camera_id,
                    'totals_in': entry['totals_in'],
                    'totals_out': entry['totals_out'],
                    'status': camera_status,
                }
                camera_data.append(camera_entry)

            response_data = {
                'history': camera_data,
                'total_in_sum': total_in_sum,
                'total_out_sum': total_out_sum,
            }

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CameraCounterHistoryGraphView(APIView):
    def get(self, request, tent_id, *args, **kwargs):
        try:
            tent = Tent.objects.get(id=tent_id)
        except Tent.DoesNotExist:
            return Response({'error': 'Tent not found'}, status=404)

        date_str = self.request.query_params.get('date')
        if not date_str:
            return Response({'error': 'Date parameter is required'}, status=400)

        try:
            date = datetime.strptime(date_str, '%d-%m-%Y').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use DD-MM-YYYY'}, status=400)

        counter_history_data = self.get_counter_history_data(tent, date)

        return Response(counter_history_data)

    def get_counter_history_data(self, tent, date):
        counter_history_data = {'tent_id': tent.id, 'date': date.strftime('%d-%m-%Y'), 'counter_history': []}

        # cameras = tent.camera_set.all()
        hourly_data = CounterHistory.objects.filter(
                camera__tent=tent,
                start_time__date=date,
            ).values(hour=ExtractHour("start_time")).annotate(
                total_in=Sum('total_in'),
                total_out=Sum('total_out'),
                total=Sum('total')
            )

        # print(hourly_data)

        data_counterised = Counter({d["hour"]: d["total_in"] for d in hourly_data})
        result = [data_counterised[i] for i in range(0, 23 + 1)]
        labels = ["Hour " + str(i) for i in range(0, 23 + 1)]
        data = {"labels": labels, "chartdata": result}
        print(data)

        return data