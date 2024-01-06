# main_app/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from main_app.models import *

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    verification = serializers.BooleanField(default=False)
    extra_kwargs = {
        'password': {'write_only': True},
    }

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'verification', 'assigned_tent']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"], username=validated_data["username"]
        )
        password = validated_data["password"]
        user.set_password(password)
        user.save()
        for item in validated_data['assigned_tent']:
            user.assigned_tent.add(item)
        return user

class CameraTentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ('id', 'sn', 'heart_beat_time', 'created_at', 'updated_at')

    def create(self, validated_data):
        camera = Camera.objects.create(**validated_data)
        return camera

class TentSerializer(serializers.ModelSerializer):
    cameras = serializers.SerializerMethodField('get_cameras')
    # created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
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
        fields = ['id', 'sn', 'version','time_zone', 'hw_platform', 'tent', 'tent_details', 'heart_beat_time', 'created_at', 'updated_at', 'status'] # Include 'status' field

    def create(self, validated_data):
        camera = Camera.objects.create(**validated_data)
        return camera

    version = serializers.IntegerField(required=False)
    time_zone = serializers.IntegerField(required=False)
    hw_platform = serializers.CharField(max_length=255, required=False)

class CounterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterHistory
        fields = ['sn', 'total_in', 'total_out', 'total', 'start_time', 'end_time']
    def create(self, validated_data):
        sn = validated_data.get("sn", None)
        camera = None
        if sn:
            cameras = Camera.objects.filter(sn=sn)
            if cameras.exists():
                cameras = cameras[0]
                camera.save()
            else:
                camera = Camera.objects.create(sn=str(sn))
        else:
            raise Exception("error")

class CreateCounterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterHistory
        fields = ['camera', 'sn', 'total_in', 'total_out', 'total', 'start_time', 'end_time']

    def create(self, validated_data):
        sn = validated_data.get("sn", None)
        camera = Camera.objects.filter(sn=sn).first()

        if not camera:
            camera = Camera.objects.create(sn=sn)

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




class CameraWithHeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'sn', 'tent', 'heart_beat_time', 'created_at', 'updated_at', 'status']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Include heartbeat fields directly within the Camera representation
        latest_heartbeat = instance.heartbeats.latest('time')

        data.update({
            "version": latest_heartbeat.version,
            "ip_address": latest_heartbeat.ip_address,
            "time_zone": latest_heartbeat.time_zone,
            "hw_platform": latest_heartbeat.hw_platform,
            "time": latest_heartbeat.time,
        })

        return data
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