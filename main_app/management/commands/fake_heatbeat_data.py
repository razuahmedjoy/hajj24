import random
from django.core.management.base import BaseCommand
from main_app.models import Camera
from main_app.api.serializers import CreateHeartbeatSerializer

class Command(BaseCommand):
    help = 'Generate and post dummy heartbeat data to the database'

    def handle(self, *args, **options):
        all_cameras = Camera.objects.all()

        dummy_heartbeat_list = [
    {
      "version": 1,
      "ip_address": "39.255.92.225",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-09-28",
      "time": "2023-05-19T14:23:47.812Z"
    },
    {
      "version": 2,
      "ip_address": "23.178.166.208",
      "time_zone": 1,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-21",
      "time": "2023-06-05T21:15:03.420Z"
    },
    {
      "version": 10,
      "ip_address": "217.110.216.111",
      "time_zone": 12,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-05",
      "time": "2023-05-15T00:51:41.297Z"
    },
    {
      "version": 9,
      "ip_address": "251.97.216.36",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-01-06",
      "time": "2023-09-12T04:47:25.964Z"
    },
    {
      "version": 5,
      "ip_address": "48.32.243.102",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-17",
      "time": "2023-11-16T18:21:19.392Z"
    },
    {
      "version": 10,
      "ip_address": "129.94.76.150",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-29",
      "time": "2023-07-30T15:11:06.863Z"
    },
    {
      "version": 7,
      "ip_address": "27.191.208.103",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-13",
      "time": "2023-09-07T07:58:33.857Z"
    },
    {
      "version": 6,
      "ip_address": "171.27.162.178",
      "time_zone": 1,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-23",
      "time": "2023-01-29T11:13:28.136Z"
    },
    {
      "version": 7,
      "ip_address": "16.63.180.192",
      "time_zone": 12,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-07",
      "time": "2023-07-31T08:10:25.019Z"
    },
    {
      "version": 6,
      "ip_address": "195.189.168.124",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-29",
      "time": "2023-10-26T19:59:32.033Z"
    },
    {
      "version": 8,
      "ip_address": "41.49.1.153",
      "time_zone": 5,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-06",
      "time": "2022-12-31T23:10:13.902Z"
    },
    {
      "version": 7,
      "ip_address": "133.171.136.237",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-15",
      "time": "2023-04-07T05:57:39.540Z"
    },
    {
      "version": 10,
      "ip_address": "30.40.148.78",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-12-13",
      "time": "2023-12-28T02:48:37.856Z"
    },
    {
      "version": 2,
      "ip_address": "203.179.98.156",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-25",
      "time": "2023-06-30T04:34:21.481Z"
    },
    {
      "version": 5,
      "ip_address": "107.187.97.117",
      "time_zone": 10,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-02-27",
      "time": "2023-10-31T09:31:31.683Z"
    },
    {
      "version": 7,
      "ip_address": "94.61.128.245",
      "time_zone": 10,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-10-15",
      "time": "2023-04-23T08:03:04.396Z"
    },
    {
      "version": 3,
      "ip_address": "70.11.52.53",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-01-30",
      "time": "2023-05-20T14:45:25.431Z"
    },
    {
      "version": 7,
      "ip_address": "194.176.200.165",
      "time_zone": 0,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-28",
      "time": "2023-06-14T04:46:57.678Z"
    },
    {
      "version": 2,
      "ip_address": "136.11.255.84",
      "time_zone": 8,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-06",
      "time": "2023-05-02T03:56:46.967Z"
    },
    {
      "version": 6,
      "ip_address": "182.30.93.238",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-14",
      "time": "2023-02-11T09:02:01.832Z"
    }
  ]

        for camera in all_cameras:
            # Limit the sample size to 1 for each camera
            selected_heartbeat = random.sample(dummy_heartbeat_list, 1)[0]

            selected_heartbeat["sn"] = camera.sn

            # Create a CameraHeartbeat instance
            heartbeat_serializer = CreateHeartbeatSerializer(data=selected_heartbeat)
            heartbeat_serializer.is_valid(raise_exception=True)
            heartbeat_serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted dummy heartbeat data to the database'))
