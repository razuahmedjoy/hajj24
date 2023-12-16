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
        user = User.objects.create_user(**validated_data)
        return user

class CameraTentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id', 'sn', 'heart_beat_time', 'created_at', 'updated_at')

    def create(self, validated_data):
        camera = Camera.objects.create(**validated_data)
        return camera

class TentSerializer(serializers.ModelSerializer):
    # cameras = CameraTentSerializer(many=True, read_only=True)
    cameras = serializers.SerializerMethodField('get_cameras')
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Tent
        fields = ('cameras','id', 'name', 'lat', 'long', 'location', 'created_by', 'created_at', 'updated_at')
    def get_cameras(self, obj):
        cameras = Camera.objects.filter(tent=obj)
        return CameraTentSerializer(cameras, many=True).data



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
        fields = ['camera', 'sn', 'total_in', 'total_out', 'total', 'start_time', 'end_time']

    def create(self, validated_data):
        sn = validated_data.get("sn", None)
        camera = validated_data.get("camera")
        existing_history = CounterHistory.objects.filter(camera=camera, sn=sn).first()
        if existing_history:
            existing_history.total_in = validated_data.get("total_in", 0)
            existing_history.total_out = validated_data.get("total_out", 0)
            existing_history.total = validated_data.get("total", 0)
            existing_history.start_time = validated_data.get("start_time", None)
            existing_history.end_time = validated_data.get("end_time", None)
            existing_history.save()
            return existing_history


        history = CounterHistory.objects.create(
            camera=camera,
            sn=sn,
            total_in=validated_data.get("total_in", 0),
            total_out=validated_data.get("total_out", 0),
            total=validated_data.get("total", 0),
            start_time=validated_data.get("start_time", None),
            end_time=validated_data.get("end_time", None)
        )
        return history


class CreateHeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraHeartbeat
        fields = [
            "sn",
            "version",
            "ip_address",
            "time_zone",
            "hw_platform",
            "time",
        ]

    def create(self, validated_data):
        time = validated_data.pop('time', None)
        time = timezone.now() if time is None else time

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




class CameraDetailSerializer(serializers.ModelSerializer):
    tent_details = TentSerializer(read_only=True, source='tent')
    counter_histories = CreateCounterHistorySerializer(many=True, read_only=True)
    heartbeats = CreateHeartbeatSerializer(many=True, read_only=True)

    class Meta:
        model = Camera
        fields = ['id', 'sn', 'tent', 'tent_details', 'heart_beat_time', 'created_at', 'updated_at', 'counter_histories', 'heartbeats']
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'uploaded_at')

class PictureSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)  # Use ImageSerializer for the ManyToManyField

    class Meta:
        model = Picture
        fields = ('id', 'user', 'images', 'caption', 'created_at', 'updated_at')

    def create(self, validated_data):
        images_data = validated_data.pop('images')  # Extract image data
        picture = Picture.objects.create(**validated_data)  # Create Picture instance

        for image_data in images_data:
            Image.objects.create(picture=picture, **image_data)  # Create Image instances

        return picture