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
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.db.models import Prefetch, Sum, Count
from datetime import date, timedelta
from django.db.models import Count, Sum, Avg, F, Case, Q, When, ExpressionWrapper
from django.db import transaction
from django.db.models.functions import (
    ExtractDay,
    ExtractMonth,
    ExtractMinute,
    ExtractYear,
    ExtractHour,
    Cast,
    TruncDate
)
from datetime import datetime, timedelta
from collections import Counter
from calendar import monthrange
import calendar
from rest_framework.authtoken.models import Token
from django.db import models

import json

User = get_user_model()

#  create a userList api view from where we can get all the users and create a new user
@method_decorator(csrf_protect, name='dispatch')
class UserListAPIView(generics.ListAPIView):
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
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk, 'email': user.email}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserDeleteByEmailAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email'

    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: lookup_value}
        obj = generics.get_object_or_404(queryset, **filter_kwargs)

        return obj

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        print(user)
        # if not request.user.is_staff:
        #     raise PermissionDenied("You do not have permission to perform this action.")

        user.delete()
        return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

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

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Tent deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class CameraListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CameraWithHeartbeatSerializer

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

class CameraRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CameraSerializer

    def delete(self, request, *args, **kwargs):
        sn = kwargs.get('sn')

        try:
            with transaction.atomic():
                camera = Camera.objects.get(sn=sn)
                print(camera)
                camera.delete()
                return Response({'message': 'Camera deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Camera.DoesNotExist:
            return Response({'error': 'Camera not found'}, status=status.HTTP_404_NOT_FOUND)

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

        existing_heartbeat = CameraHeartbeat.objects.filter(sn=sn).first()

        if existing_heartbeat:
            # Update existing instance if it already exists
            heartbeat_serializer = CreateHeartbeatSerializer(existing_heartbeat, data=heartbeat_data)
        else:
            # Create a new instance if it doesn't exist
            heartbeat_serializer = CreateHeartbeatSerializer(data=heartbeat_data)

        if heartbeat_serializer.is_valid():
            camera.heart_beat_time = timezone.now()
            camera.save()
            validated_data = heartbeat_serializer.validated_data
            validated_data['camera'] = camera

            heartbeat = heartbeat_serializer.save()

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
                #last_heartbeat_time=F('camera__heartbeats__time')
            )



            # print(tent_history)
            #return Response(tent_history)

            camera_data = []
            total_in_sum = 0
            total_out_sum = 0

            for entry in tent_history:
                camera_id = entry['camera']
                camera = Camera.objects.get(id=camera_id)
                serializer = CameraSerializer(camera)
                heart_beat_time = serializer.data['heart_beat_time']

                total_in_sum += entry['totals_in']
                total_out_sum += entry['totals_out']

                camera_entry = {
                    'camera': camera_id,
                    'totals_in': entry['totals_in'],
                    'totals_out': entry['totals_out'],
                    'status': heart_beat_time,
                    'time': heart_beat_time,
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


class CameraCounterHistoryGraphViewHour(APIView):
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
        # print("value",timezone.now())

        hourly_data = CounterHistory.objects.filter(
                camera__tent=tent,
                start_time__date=date,
            ).values(hour=ExtractHour("start_time")).annotate(
                total_in=Sum('total_in'),
                total_out=Sum('total_out'),
                total=Sum('total')
            )
        
        print("hourly_data", CounterHistory.objects.filter(
                camera__tent=tent,
                # start_time__date=date,
            ).query)

        prev_data = CounterHistory.objects.filter(
            camera__tent=tent,
            start_time__date__lt=date
        ).aggregate(
            total = Sum('total')
        )
        number = prev_data['total'] if prev_data['total'] is not None else 0

        date_total_in = Counter({d["hour"]: d["total_in"] for d in hourly_data})
        date_total_out = Counter({d["hour"]: d["total_out"] for d in hourly_data})
        date_total_stay = Counter({d["hour"]: d["total"] for d in hourly_data})
        result_in = [date_total_in[i] for i in range(0, 23 + 1)]
        result_out = [date_total_out[i] for i in range(0, 23 + 1)]
        array1 = [date_total_stay[i] for i in range(0, 23 + 1)]
        

        result_stay = []
        array1[0] += number
        result_stay.append(array1[0])
        array1.pop(0)
        for value in array1:
            result_stay.append(value + result_stay[-1])
        labels = ["Hour " + str(i) for i in range(1, 24 + 1)]
        data = {"labels": labels, "total_in": result_in, "total_out": result_out, "staying": result_stay }

        return data

class CameraCounterHistoryGraphViewDay(APIView):
    def get(self, request, tent_id, *args, **kwargs):
        try:
            tent = Tent.objects.get(id=tent_id)
        except Tent.DoesNotExist:
            return Response({'error': 'Tent not found'}, status=404)

        start_date_str = self.request.query_params.get('start_date')
        end_date_str = self.request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({'error': 'Both start_date and end_date parameters are required'}, status=400)

        try:
            start_date = datetime.strptime(start_date_str, '%d-%m-%Y').date()
            end_date = datetime.strptime(end_date_str, '%d-%m-%Y').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use DD-MM-YYYY'}, status=400)

        counter_history_data = self.get_counter_history_data(tent, start_date, end_date)

        return Response(counter_history_data)

    def get_counter_history_data(self, tent, start_date, end_date):
        counter_history_data = []

        daily_data = CounterHistory.objects.filter(
            camera__tent=tent,
            start_time__date__gte=start_date,
            start_time__date__lte=end_date,
        ).values(day=TruncDate('start_time')).annotate(
            total_in=Sum('total_in'),
            total_out=Sum('total_out'),
            total=Sum('total')
        )

        #print("daily data: ",daily_data)

        prev_data = CounterHistory.objects.filter(
            camera__tent=tent,
            start_time__date__lt=start_date
        ).aggregate(
            total = Sum('total')
        )
        # print("first_print",tent, start_date, end_date)
        # print("daily_data filter:", CounterHistory.objects.filter(
        #     camera__tent=tent,
        #     start_time__range=(start_date, end_date)
        # ))
        # print("prev_data filter:", CounterHistory.objects.filter(
        #     camera__tent=tent,
        #     end_time__date__gt=end_date
        # ))

        print("daily prev data : ",prev_data)

        number = prev_data['total'] if prev_data['total'] is not None else 0
        prev_data['total'] = number

        counter_history_list = list(daily_data)

        print("couter history list: ",counter_history_list)
        total_days = (end_date - start_date).days + 1
        result_in = [0] * total_days
        result_out = [0] * total_days
        result_stay = [0] * total_days
        array1 = [0] * total_days
        print(counter_history_list, "value", daily_data)

        for entry in counter_history_list:
            if entry['day'] is None:
                continue
            day = (entry['day'] - start_date).days + 1
            result_in[day - 1] = entry['total_in']
            result_out[day - 1] = entry['total_out']
            result_stay[day - 1] = entry['total'] + prev_data['total']
            prev_data['total'] = result_stay[day - 1]
 
        # TO-DO: Print day range of month
        delta = timedelta(days=1)
        labels=[]
        # Iterate over the range of dates
        current_date = start_date
        while current_date <= end_date:
            # Do something with the current date

            labels.append(current_date.strftime("%d %b"))
            # Move to the next date
            current_date += delta
        result_stay = []
        if number is not None:
            array1[0] += number
        result_stay.append(array1[0])
        array1.pop(0)
        for value in array1:
            result_stay.append(value + result_stay[-1])

        data = {"labels": labels, "total_in": result_in, "total_out": result_out, "staying": result_stay }

        return data



class CameraCounterHistoryGraphViewMonth(APIView):
    def get(self, request, tent_id, *args, **kwargs):
        try:
            tent = Tent.objects.get(id=tent_id)
        except Tent.DoesNotExist:
            return Response({'error': 'Tent not found'}, status=404)

        date_str = self.request.query_params.get('date')
        if not date_str:
            return Response({'error': 'Date parameter is required'}, status=400)

        try:
            date = datetime.strptime(date_str, '%m-%Y').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Use MM-YYYY'}, status=400)

        counter_history_data = self.get_counter_history_data(tent, date)

        return Response(counter_history_data)

    def get_counter_history_data(self, tent, date):
        monthly_data = CounterHistory.objects.filter(
            camera__tent=tent,
            start_time__year=date.year,
            start_time__month=date.month
        ).values(day=ExtractDay("start_time")).annotate(
            total_in=Sum('total_in'),
            total_out=Sum('total_out'),
            total=Sum('total')
        )

        prev_data = CounterHistory.objects.filter(
            camera__tent=tent,
            start_time__year__lte=date.year,
            start_time__month__lt=date.month
        ).aggregate(
            total = Sum('total')
        )
    
        counter_history_list = list(monthly_data)
        date_total_in = Counter({d["day"]: d["total_in"] for d in counter_history_list})
        date_total_out = Counter({d["day"]: d["total_out"] for d in counter_history_list})
        date_total_stay = Counter({d["day"]: d["total"] for d in counter_history_list})

        print("date: ",date.month)
        print("len :",monthrange(date.year, date.month))
        selected_month=date.strftime('%b')
        # __, ds = monthrange(datetime.today().year, datetime.today().month)
        __, ds = monthrange(date.year, date.month)
        result_in = [date_total_in[i] for i in range(1, ds + 1)]
        result_out = [date_total_out[i] for i in range(1, ds + 1)]
        array1 = [date_total_stay[i] for i in range(1, ds + 1)]

        labels = [selected_month+" " + str(i) for i in range(1, ds + 1)]
        number = prev_data['total'] if prev_data['total'] is not None else 0
        result_stay = []
        array1[0] += number
        result_stay.append(array1[0])
        array1.pop(0)
        for value in array1:
            result_stay.append(value + result_stay[-1])

        data = {"labels": labels, "total_in": result_in, "total_out": result_out, "staying": result_stay }

        return data




