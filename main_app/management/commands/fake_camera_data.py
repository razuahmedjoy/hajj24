import random
from django.core.management.base import BaseCommand
from django.db import transaction
from main_app.models import Tent, Camera
from main_app.api.serializers import CameraSerializer

class Command(BaseCommand):
    help = 'Create cameras with direct data'

    def handle(self, *args, **options):
        # Fetch all tents from the database
        tents = Tent.objects.all()

        camera_data = [
  { "sn": '658201333c364083b8090806' },
  { "sn": '65820133e0cfb20ba39d561d' },
  { "sn": '6582013367344b8486def37a' },
  { "sn": '65820133a7c211f27b746140' },
  { "sn": '65820133c237248f184fccd6' },
  { "sn": '658201337208ef6ee0e94d60' },
  { "sn": '658201330af99d54e9af5493' },
  { "sn": '6582013361d461ef089d6fc1' },
  { "sn": '658201339dcd1c84fe3e9d61' },
  { "sn": '6582013392400f907b435596' },
  { "sn": '658201330f81f7431a394a1a' },
  { "sn": '658201338648b04ab7c86b5d' },
  { "sn": '65820133fc585beebeec3dae' },
  { "sn": '65820133b77ccf20e51e881d' },
  { "sn": '658201334e85c4b82b82a405' },
  { "sn": '65820133648c1ae87fb9f432' },
  { "sn": '658201333e95ef70635958ea' },
  { "sn": '6582013368a6081c26911e91' },
  { "sn": '658201337a27e245cf91c654' },
  { "sn": '658201333a5fced30893ca31' }
]


        try:
            with transaction.atomic():      
              max_cameras_per_tent = 2
              cameras_assigned_per_tent = {}

               
              for camera_info in camera_data:
                random_tent = random.choice(tents)
                if random_tent.id not in cameras_assigned_per_tent:
                    cameras_assigned_per_tent[random_tent.id] = 0

                if cameras_assigned_per_tent[random_tent.id] < max_cameras_per_tent:
                    camera_info["tent"] = random_tent.id

                    camera_serializer = CameraSerializer(data=camera_info)
                    if camera_serializer.is_valid():
                        camera_serializer.save()
                        cameras_assigned_per_tent[random_tent.id] += 1
                    else:
                        print(f"Error creating camera: {camera_serializer.errors}")
                else:
                    print(f"Max cameras reached for tent {random_tent.id}. Skipping camera creation.")

        except Exception as e:
            print(f"Error creating cameras with direct data: {e}")
