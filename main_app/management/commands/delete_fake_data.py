from django.core.management.base import BaseCommand
from main_app.models import Tent, Camera, CounterHistory, CameraHeartbeat, User

class Command(BaseCommand):
    help = 'Delete fake data for the models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Deleting fake data...'))

        Tent.objects.all().delete()
        Camera.objects.all().delete()
        CounterHistory.objects.all().delete()
        CameraHeartbeat.objects.all().delete()
        User.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Fake data deleted successfully'))