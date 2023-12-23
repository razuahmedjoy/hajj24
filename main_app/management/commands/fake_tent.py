import random
import string
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from main_app.models import Tent, Camera
from main_app.api.serializers import TentSerializer, CameraSerializer

User = get_user_model()

tent_data = [
  {
    "name": "Tent 1",
    "lat": -47.998487,
    "long": -137.126745,
    "location": "Williamson"
  },
  {
    "name": "Tent 2",
    "lat": -5.478587,
    "long": 166.435343,
    "location": "Waterview"
  },
  {
    "name": "Tent 3",
    "lat": 75.689802,
    "long": -43.825902,
    "location": "Orovada"
  },
  {
    "name": "Tent 4",
    "lat": -6.036967,
    "long": 82.576962,
    "location": "Manitou"
  },
  {
    "name": "Tent 5",
    "lat": -13.029214,
    "long": -130.735033,
    "location": "Lithium"
  },
  {
    "name": "Tent 6",
    "lat": 9.282648,
    "long": -35.45568,
    "location": "Beyerville"
  },
  {
    "name": "Tent 7",
    "lat": 60.18884,
    "long": -21.749121,
    "location": "Townsend"
  },
  {
    "name": "Tent 8",
    "lat": 81.008556,
    "long": 173.285958,
    "location": "Santel"
  },
  {
    "name": "Tent 9",
    "lat": 27.513879,
    "long": 68.536359,
    "location": "Brooktrails"
  },
  {
    "name": "Tent 10",
    "lat": -51.575294,
    "long": -121.548114,
    "location": "Makena"
  }
]


class Command(BaseCommand):
    help = 'Create fake data for tents with empty arrays for cameras'

    def generate_random_sn(self):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(16))

    def handle(self, *args, **options):
        users = User.objects.all()

        try:
            with transaction.atomic():
                for tent_info in tent_data:
                    tent_info["created_by"] = random.choice(users).id
                    tent_serializer = TentSerializer(data=tent_info)
                    if tent_serializer.is_valid():
                        tent = tent_serializer.save()

        except Exception as e:
            print(f"Error creating tents with empty arrays for cameras: {e}")
