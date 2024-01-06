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
    {'sn': '658201333c364083b8090806', 'ip_address': '236.123.55.22'},
    {'sn': '65820133e0cfb20ba39d561d', 'ip_address': '64.22.198.189'},
    {'sn': '6582013367344b8486def37a', 'ip_address': '168.203.111.85'},
    {'sn': '65820133a7c211f27b746140', 'ip_address': '39.234.14.97'},
    {'sn': '65820133c237248f184fccd6', 'ip_address': '185.22.45.17'},
    {'sn': '658201337208ef6ee0e94d60', 'ip_address': '29.103.99.161'},
    {'sn': '658201330af99d54e9af5493', 'ip_address': '106.229.42.201'},
    {'sn': '6582013361d461ef089d6fc1', 'ip_address': '79.1.76.97'},
    {'sn': '658201339dcd1c84fe3e9d61', 'ip_address': '122.223.214.123'},
    {'sn': '6582013392400f907b435596', 'ip_address': '190.221.56.98'},
    {'sn': '658201330f81f7431a394a1a', 'ip_address': '135.188.42.37'},
    {'sn': '658201338648b04ab7c86b5d', 'ip_address': '44.11.56.221'},
    {'sn': '65820133fc585beebeec3dae', 'ip_address': '92.10.134.44'},
    {'sn': '65820133b77ccf20e51e881d', 'ip_address': '92.218.91.67'},
    {'sn': '658201334e85c4b82b82a405', 'ip_address': '77.211.171.162'},
    {'sn': '65820133648c1ae87fb9f432', 'ip_address': '203.96.201.127'},
    {'sn': '658201333e95ef70635958ea', 'ip_address': '55.87.213.10'},
    {'sn': '6582013368a6081c26911e91', 'ip_address': '185.99.240.166'},
    {'sn': '658201337a27e245cf91c654', 'ip_address': '39.157.198.35'},
    {'sn': '658201333a5fced30893ca31', 'ip_address': '90.209.33.189'}
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
