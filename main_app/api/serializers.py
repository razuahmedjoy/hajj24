# main_app/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from main_app.models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    class Meta:
        model = User
        fields = ('id','email','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class TentSerializer(serializers.ModelSerializer):
    # fetch the created_by users data also when fetching the tent data
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Tent
        fields = ('id', 'name', 'lat', 'long', 'location', 'created_by', 'created_at', 'updated_at')



class CameraSerializer(serializers.ModelSerializer):
    tent_details = TentSerializer(read_only=True, source='tent')

    class Meta:
        model = Camera
        fields = ('id', 'sn', 'tent', 'tent_details', 'heart_beat_time', 'created_at', 'updated_at')

    def create(self, validated_data):
        camera = Camera.objects.create(**validated_data)
        return camera

class CreateCounterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterHistory
        fields = [
            "sn",
            "total_in",
            "total_out",
            "total",
            "start_time",
            "end_time",
        ]

    def create(self, validated_data):
        sn = validated_data.get("sn", None)
        camera = None

        if sn:
            cameras = Camera.objects.filter(sn=sn)
            if cameras.exists():
                camera = cameras[0]
            else:
                camera = Camera.objects.create(sn=str(sn), tent=None)
        else:
            raise serializers.ValidationError("Camera serial number is required.")

        history = CounterHistory.objects.create(
            camera=camera,
            **validated_data
        )
        return history


class CreateHeartbeatSerializer(serializers.ModelSerializer):
    reportDate = serializers.DateField(source="report_date")
    time = serializers.DateTimeField(required=False)

    class Meta:
        model = CameraHeartbeat
        fields = [
            "sn",
            "version",
            "ip_address",
            "time_zone",
            "hw_platform",
            "reportDate",
            "time",
        ]

    def create(self, validated_data):
        time = None
        try:
            time = validated_data.pop("time")
            time = datetime.datetime.fromtimestamp(time, tz=timezone.utc)
        except:
            time = None
        sn = validated_data.get("sn", None)
        camera = None
        if sn:
            cameras = Camera.objects.filter(sn=sn)
            if cameras.exists():
                camera = cameras.first()

                camera.heart_beat_time = timezone.now()
                camera.save()
            else:
                camera = Camera.objects.create(sn=str(sn), tent=None)
        else:
            raise serializers.ValidationError("Camera serial number is required.")

        heartbeat = CameraHeartbeat.objects.create(
            camera=camera, time=time, **validated_data
        )

        return heartbeat
