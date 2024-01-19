from django.core.management.base import BaseCommand
from main_app.api.serializers import UserSerializer
import json

class Command(BaseCommand):
    help = 'Inserts fake user data into the database'

    def handle(self, *args, **options):
        fake_data = [
  {
    "email": "rpentony1@sciencedaily.com",
    "username": "shell",
    "password": "hello1world"
  },
  {
    "email": "eferraresi2@arstechnica.com",
    "username": "fish",
    "password": "hello1world"
  },
  {
    "email": "nsiggers3@163.com",
    "username": "fry",
    "password": "hello1world"
  },
  {
    "email": "krochelle4@furl.net",
    "username": "cry",
    "password": "hello1world"
  }]

        for user_data in fake_data:
            serializer = UserSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully inserted user: {user_data["username"]}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to insert user: {user_data["username"]}'))
                self.stdout.write(self.style.ERROR(serializer.errors))
