# myapp/management/commands/fake_camera_data.py
import random
import datetime
from django.core.management.base import BaseCommand
from main_app.models import Camera, CounterHistory
from main_app.api.serializers import CreateCounterHistorySerializer

class Command(BaseCommand):
    help = 'Generate and post dummy camera data to the database'

    def handle(self, *args, **options):
        # Get all available cameras from the database
        all_cameras = Camera.objects.all()

        # Assuming you have a list of dummy JSON data
        dummy_data_list = []


        for dummy_data in dummy_data_list:
            # Randomly select a camera from the available cameras
            random_camera = random.choice(all_cameras)

            # Use the selected camera's data for the dummy data
            dummy_data["camera"] = random_camera.id
            dummy_data["sn"] = random_camera.sn

            # Create a CounterHistory instance
            counter_history_serializer = CreateCounterHistorySerializer(data=dummy_data)
            counter_history_serializer.is_valid(raise_exception=True)
            counter_history_serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted dummy camera data to the database'))
