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
