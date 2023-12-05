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
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Tent
        fields = ('id', 'name', 'lat', 'long', 'location', 'created_by', 'created_at', 'updated_at')


# create a serializer for the Camera model
class CameraSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Camera
        fields = ('id', 'sn', 'tent_details', 'tent')
    tent_details = TentSerializer(read_only=True, source='tent')





    def create(self, validated_data):
    
        # check if all required fields are provided
        try:
            camera = Camera.objects.create(**validated_data)
            return camera
        except KeyError:
            raise serializers.ValidationError({'error': 'Something went wrong'})
