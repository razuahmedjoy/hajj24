import random
from django.core.management.base import BaseCommand
from main_app.models import Camera, CameraHeartbeat
from main_app.api.serializers import CreateHeartbeatSerializer

class Command(BaseCommand):
    help = 'Generate and post dummy heartbeat data to the database'

    def handle(self, *args, **options):
        all_cameras = Camera.objects.all()
        max_heartbeats_per_camera = 5

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
    },
    {
      "version": 1,
      "ip_address": "1.128.252.106",
      "time_zone": 0,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-11",
      "time": "2023-06-06T16:49:06.190Z"
    },
    {
      "version": 8,
      "ip_address": "85.97.53.125",
      "time_zone": 5,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-01",
      "time": "2023-06-26T10:31:39.408Z"
    },
    {
      "version": 9,
      "ip_address": "177.157.224.2",
      "time_zone": 12,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-02-21",
      "time": "2023-06-07T14:04:30.903Z"
    },
    {
      "version": 1,
      "ip_address": "119.119.105.81",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-25",
      "time": "2023-11-09T15:35:03.851Z"
    },
    {
      "version": 8,
      "ip_address": "143.220.234.233",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-01-09",
      "time": "2023-10-23T06:23:12.602Z"
    },
    {
      "version": 10,
      "ip_address": "250.221.71.49",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-09-24",
      "time": "2023-01-03T05:20:58.563Z"
    },
    {
      "version": 8,
      "ip_address": "176.141.241.79",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-02-16",
      "time": "2023-01-13T05:45:24.994Z"
    },
    {
      "version": 2,
      "ip_address": "74.9.17.50",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-11",
      "time": "2023-09-26T00:40:48.713Z"
    },
    {
      "version": 4,
      "ip_address": "8.157.86.248",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-09-22",
      "time": "2023-05-30T18:02:38.496Z"
    },
    {
      "version": 10,
      "ip_address": "56.80.208.174",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-10-24",
      "time": "2023-09-23T09:05:44.819Z"
    },
    {
      "version": 1,
      "ip_address": "49.136.183.164",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-07-19",
      "time": "2023-09-16T14:05:07.525Z"
    },
    {
      "version": 7,
      "ip_address": "76.34.22.175",
      "time_zone": 8,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-07-25",
      "time": "2023-09-24T09:29:21.628Z"
    },
    {
      "version": 5,
      "ip_address": "66.77.181.229",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-12",
      "time": "2023-02-08T15:26:08.523Z"
    },
    {
      "version": 1,
      "ip_address": "130.14.181.189",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-08-31",
      "time": "2023-06-18T10:19:31.274Z"
    },
    {
      "version": 8,
      "ip_address": "186.37.14.209",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-17",
      "time": "2023-04-05T12:46:46.199Z"
    },
    {
      "version": 1,
      "ip_address": "147.52.29.212",
      "time_zone": 4,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-02-25",
      "time": "2023-03-03T20:19:46.055Z"
    },
    {
      "version": 4,
      "ip_address": "60.192.193.142",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-09-06",
      "time": "2023-03-17T03:41:46.050Z"
    },
    {
      "version": 4,
      "ip_address": "69.40.203.234",
      "time_zone": 12,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-03",
      "time": "2023-03-29T15:00:56.513Z"
    },
    {
      "version": 7,
      "ip_address": "210.75.9.221",
      "time_zone": 5,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-24",
      "time": "2023-08-01T01:31:22.624Z"
    },
    {
      "version": 8,
      "ip_address": "146.70.212.112",
      "time_zone": 8,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-05",
      "time": "2023-10-11T00:17:25.977Z"
    },
    {
      "version": 2,
      "ip_address": "60.24.156.124",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-20",
      "time": "2023-07-28T04:21:36.057Z"
    },
    {
      "version": 2,
      "ip_address": "19.155.146.86",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-01-18",
      "time": "2023-04-02T18:10:34.753Z"
    },
    {
      "version": 1,
      "ip_address": "143.59.134.115",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-08-10",
      "time": "2023-08-15T04:20:21.838Z"
    },
    {
      "version": 6,
      "ip_address": "205.25.5.178",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-19",
      "time": "2023-09-09T00:27:58.070Z"
    },
    {
      "version": 7,
      "ip_address": "33.114.123.165",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-18",
      "time": "2023-08-26T17:51:57.777Z"
    },
    {
      "version": 5,
      "ip_address": "53.87.156.63",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-10-03",
      "time": "2023-11-23T13:47:57.810Z"
    },
    {
      "version": 6,
      "ip_address": "182.172.12.30",
      "time_zone": 5,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-08-07",
      "time": "2023-07-17T19:49:49.405Z"
    },
    {
      "version": 10,
      "ip_address": "10.35.175.247",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-06",
      "time": "2023-04-08T02:08:45.925Z"
    },
    {
      "version": 5,
      "ip_address": "53.206.128.71",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-24",
      "time": "2023-08-07T08:28:54.412Z"
    },
    {
      "version": 7,
      "ip_address": "188.42.97.107",
      "time_zone": 8,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-11",
      "time": "2023-01-17T13:21:56.518Z"
    },
    {
      "version": 10,
      "ip_address": "136.78.9.233",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-17",
      "time": "2023-07-14T06:29:46.598Z"
    },
    {
      "version": 3,
      "ip_address": "201.76.149.196",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-21",
      "time": "2023-07-17T13:53:20.620Z"
    },
    {
      "version": 3,
      "ip_address": "222.9.77.104",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-15",
      "time": "2023-06-16T06:00:00.015Z"
    },
    {
      "version": 7,
      "ip_address": "184.54.192.102",
      "time_zone": 8,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-26",
      "time": "2023-08-18T20:18:34.899Z"
    },
    {
      "version": 9,
      "ip_address": "30.254.219.147",
      "time_zone": 1,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-11-25",
      "time": "2023-05-13T22:27:09.026Z"
    },
    {
      "version": 6,
      "ip_address": "102.32.164.224",
      "time_zone": 6,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-09-16",
      "time": "2023-10-04T11:35:06.399Z"
    },
    {
      "version": 8,
      "ip_address": "85.219.156.158",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-10-15",
      "time": "2023-10-20T10:58:12.431Z"
    },
    {
      "version": 3,
      "ip_address": "103.20.9.123",
      "time_zone": 0,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-08-19",
      "time": "2023-02-23T20:05:43.718Z"
    },
    {
      "version": 3,
      "ip_address": "24.15.5.143",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-10-01",
      "time": "2023-05-17T03:40:45.406Z"
    },
    {
      "version": 1,
      "ip_address": "9.88.88.225",
      "time_zone": 10,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-30",
      "time": "2023-02-03T07:24:33.566Z"
    },
    {
      "version": 10,
      "ip_address": "35.3.75.63",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-08-30",
      "time": "2023-03-25T02:52:53.383Z"
    },
    {
      "version": 7,
      "ip_address": "163.180.163.69",
      "time_zone": 12,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-21",
      "time": "2023-09-28T20:11:25.467Z"
    },
    {
      "version": 10,
      "ip_address": "183.26.177.103",
      "time_zone": 8,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-12-13",
      "time": "2023-02-17T10:33:10.028Z"
    },
    {
      "version": 9,
      "ip_address": "172.101.245.250",
      "time_zone": 1,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-09-20",
      "time": "2023-04-22T05:45:26.870Z"
    },
    {
      "version": 7,
      "ip_address": "126.196.44.197",
      "time_zone": 4,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-05-26",
      "time": "2023-01-23T09:25:55.623Z"
    },
    {
      "version": 2,
      "ip_address": "238.56.18.113",
      "time_zone": 11,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-25",
      "time": "2023-05-24T04:46:19.590Z"
    },
    {
      "version": 1,
      "ip_address": "1.97.31.125",
      "time_zone": 1,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-01",
      "time": "2023-05-05T12:10:17.929Z"
    },
    {
      "version": 7,
      "ip_address": "17.75.152.9",
      "time_zone": 0,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-12",
      "time": "2023-01-18T14:09:10.558Z"
    },
    {
      "version": 6,
      "ip_address": "146.198.45.176",
      "time_zone": 4,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-01-23",
      "time": "2023-12-12T12:13:57.566Z"
    },
    {
      "version": 2,
      "ip_address": "150.32.50.119",
      "time_zone": 1,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-01",
      "time": "2023-10-04T19:05:40.707Z"
    },
    {
      "version": 4,
      "ip_address": "37.25.167.144",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-07",
      "time": "2023-08-05T04:05:06.042Z"
    },
    {
      "version": 9,
      "ip_address": "20.100.9.103",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-12-03",
      "time": "2023-08-18T18:53:08.483Z"
    },
    {
      "version": 9,
      "ip_address": "100.34.34.117",
      "time_zone": 3,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-03-30",
      "time": "2023-07-12T10:49:18.544Z"
    },
    {
      "version": 2,
      "ip_address": "29.179.198.197",
      "time_zone": 7,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-02-11",
      "time": "2023-07-23T22:16:29.581Z"
    },
    {
      "version": 2,
      "ip_address": "202.56.15.42",
      "time_zone": 5,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-11",
      "time": "2023-02-13T17:19:42.972Z"
    },
    {
      "version": 2,
      "ip_address": "136.112.68.21",
      "time_zone": 9,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-04-06",
      "time": "2023-02-06T21:02:32.237Z"
    },
    {
      "version": 8,
      "ip_address": "175.21.205.106",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-07-30",
      "time": "2023-04-22T20:44:52.187Z"
    },
    {
      "version": 7,
      "ip_address": "227.207.238.251",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-02-01",
      "time": "2023-12-19T15:28:34.128Z"
    },
    {
      "version": 8,
      "ip_address": "209.185.178.33",
      "time_zone": 5,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-10-19",
      "time": "2023-04-13T23:33:16.305Z"
    },
    {
      "version": 2,
      "ip_address": "198.126.203.128",
      "time_zone": 2,
      "hw_platform": "platform_xyz",
      "reportDate": "2023-06-01",
      "time": "2023-09-04T17:13:36.767Z"
    }
  ]

        for camera in all_cameras:
            selected_heartbeats = random.sample(dummy_heartbeat_list, min(len(dummy_heartbeat_list), max_heartbeats_per_camera))

            for dummy_heartbeat in selected_heartbeats:
                dummy_heartbeat["sn"] = camera.sn

                # Create a CameraHeartbeat instance
                heartbeat_serializer = CreateHeartbeatSerializer(data=dummy_heartbeat)
                heartbeat_serializer.is_valid(raise_exception=True)
                heartbeat_serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted dummy heartbeat data to the database'))
