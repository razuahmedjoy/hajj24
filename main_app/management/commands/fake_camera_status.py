# main_app/management/commands/fake_camera_status.py

from django.core.management.base import BaseCommand
from main_app.models import Camera
import random

class Command(BaseCommand):
    help = 'Set fake status for existing cameras'

    def handle(self, *args, **options):
        cameras = Camera.objects.all()

        for camera in cameras:
            # Set a random status for each camera (True or False)
            camera.status = random.choice([True, False])
            camera.save()

        self.stdout.write(self.style.SUCCESS('Fake camera status has been set successfully'))
