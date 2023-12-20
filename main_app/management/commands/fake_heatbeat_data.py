import random
from django.core.management.base import BaseCommand
from main_app.models import Camera, CameraHeartbeat
from main_app.api.serializers import CreateHeartbeatSerializer

class Command(BaseCommand):
    help = 'Generate and post dummy heartbeat data to the database'

    def handle(self, *args, **options):
        all_cameras = Camera.objects.all()
        dummy_heartbeat_list = [
  {
    "version": 1,
    "ip_address": "39.255.92.225",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-28",
    "time": "2023-05-19T14:23:47.812ZT18:20:19"
  },
  {
    "version": 2,
    "ip_address": "23.178.166.208",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-21",
    "time": "2023-06-05T21:15:03.420ZT23:51:50"
  },
  {
    "version": 10,
    "ip_address": "217.110.216.111",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-05",
    "time": "2023-05-15T00:51:41.297ZT08:47:53"
  },
  {
    "version": 9,
    "ip_address": "251.97.216.36",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-06",
    "time": "2023-09-12T04:47:25.964ZT03:43:31"
  },
  {
    "version": 5,
    "ip_address": "48.32.243.102",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-17",
    "time": "2023-11-16T18:21:19.392ZT03:22:16"
  },
  {
    "version": 10,
    "ip_address": "129.94.76.150",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-29",
    "time": "2023-07-30T15:11:06.863ZT08:52:30"
  },
  {
    "version": 7,
    "ip_address": "27.191.208.103",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-13",
    "time": "2023-09-07T07:58:33.857ZT04:43:22"
  },
  {
    "version": 6,
    "ip_address": "171.27.162.178",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-23",
    "time": "2023-01-29T11:13:28.136ZT17:17:39"
  },
  {
    "version": 7,
    "ip_address": "16.63.180.192",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-07",
    "time": "2023-07-31T08:10:25.019ZT12:46:00"
  },
  {
    "version": 6,
    "ip_address": "195.189.168.124",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-29",
    "time": "2023-10-26T19:59:32.033ZT06:21:00"
  },
  {
    "version": 8,
    "ip_address": "41.49.1.153",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-06",
    "time": "2022-12-31T23:10:13.902ZT06:26:15"
  },
  {
    "version": 7,
    "ip_address": "133.171.136.237",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-15",
    "time": "2023-04-07T05:57:39.540ZT04:30:17"
  },
  {
    "version": 10,
    "ip_address": "30.40.148.78",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-13",
    "time": "2023-12-28T02:48:37.856ZT10:41:53"
  },
  {
    "version": 2,
    "ip_address": "203.179.98.156",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-25",
    "time": "2023-06-30T04:34:21.481ZT13:24:39"
  },
  {
    "version": 5,
    "ip_address": "107.187.97.117",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-27",
    "time": "2023-10-31T09:31:31.683ZT22:54:55"
  },
  {
    "version": 7,
    "ip_address": "94.61.128.245",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-15",
    "time": "2023-04-23T08:03:04.396ZT00:48:13"
  },
  {
    "version": 3,
    "ip_address": "70.11.52.53",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-30",
    "time": "2023-05-20T14:45:25.431ZT14:15:25"
  },
  {
    "version": 7,
    "ip_address": "194.176.200.165",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-28",
    "time": "2023-06-14T04:46:57.678ZT20:54:13"
  },
  {
    "version": 2,
    "ip_address": "136.11.255.84",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-06",
    "time": "2023-05-02T03:56:46.967ZT00:57:03"
  },
  {
    "version": 6,
    "ip_address": "182.30.93.238",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-14",
    "time": "2023-02-11T09:02:01.832ZT07:45:24"
  },
  {
    "version": 1,
    "ip_address": "1.128.252.106",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-11",
    "time": "2023-06-06T16:49:06.190ZT12:15:29"
  },
  {
    "version": 8,
    "ip_address": "85.97.53.125",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-01",
    "time": "2023-06-26T10:31:39.408ZT13:14:48"
  },
  {
    "version": 9,
    "ip_address": "177.157.224.2",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-21",
    "time": "2023-06-07T14:04:30.903ZT13:47:07"
  },
  {
    "version": 1,
    "ip_address": "119.119.105.81",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-25",
    "time": "2023-11-09T15:35:03.851ZT13:29:32"
  },
  {
    "version": 8,
    "ip_address": "143.220.234.233",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-09",
    "time": "2023-10-23T06:23:12.602ZT04:30:01"
  },
  {
    "version": 10,
    "ip_address": "250.221.71.49",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-24",
    "time": "2023-01-03T05:20:58.563ZT19:55:40"
  },
  {
    "version": 8,
    "ip_address": "176.141.241.79",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-16",
    "time": "2023-01-13T05:45:24.994ZT11:30:34"
  },
  {
    "version": 2,
    "ip_address": "74.9.17.50",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-11",
    "time": "2023-09-26T00:40:48.713ZT11:58:21"
  },
  {
    "version": 4,
    "ip_address": "8.157.86.248",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-22",
    "time": "2023-05-30T18:02:38.496ZT11:18:58"
  },
  {
    "version": 10,
    "ip_address": "56.80.208.174",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-24",
    "time": "2023-09-23T09:05:44.819ZT00:08:18"
  },
  {
    "version": 1,
    "ip_address": "49.136.183.164",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-19",
    "time": "2023-09-16T14:05:07.525ZT10:29:27"
  },
  {
    "version": 7,
    "ip_address": "76.34.22.175",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-25",
    "time": "2023-09-24T09:29:21.628ZT23:40:44"
  },
  {
    "version": 5,
    "ip_address": "66.77.181.229",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-12",
    "time": "2023-02-08T15:26:08.523ZT02:36:53"
  },
  {
    "version": 1,
    "ip_address": "130.14.181.189",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-31",
    "time": "2023-06-18T10:19:31.274ZT17:27:45"
  },
  {
    "version": 8,
    "ip_address": "186.37.14.209",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-17",
    "time": "2023-04-05T12:46:46.199ZT17:00:03"
  },
  {
    "version": 1,
    "ip_address": "147.52.29.212",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-25",
    "time": "2023-03-03T20:19:46.055ZT23:13:27"
  },
  {
    "version": 4,
    "ip_address": "60.192.193.142",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-06",
    "time": "2023-03-17T03:41:46.050ZT03:42:22"
  },
  {
    "version": 4,
    "ip_address": "69.40.203.234",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-03",
    "time": "2023-03-29T15:00:56.513ZT13:06:24"
  },
  {
    "version": 7,
    "ip_address": "210.75.9.221",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-24",
    "time": "2023-08-01T01:31:22.624ZT08:23:45"
  },
  {
    "version": 8,
    "ip_address": "146.70.212.112",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-05",
    "time": "2023-10-11T00:17:25.977ZT13:07:10"
  },
  {
    "version": 2,
    "ip_address": "60.24.156.124",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-20",
    "time": "2023-07-28T04:21:36.057ZT21:28:29"
  },
  {
    "version": 2,
    "ip_address": "19.155.146.86",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-18",
    "time": "2023-04-02T18:10:34.753ZT20:31:09"
  },
  {
    "version": 1,
    "ip_address": "143.59.134.115",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-10",
    "time": "2023-08-15T04:20:21.838ZT11:49:16"
  },
  {
    "version": 6,
    "ip_address": "205.25.5.178",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-19",
    "time": "2023-09-09T00:27:58.070ZT12:22:02"
  },
  {
    "version": 7,
    "ip_address": "33.114.123.165",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-18",
    "time": "2023-08-26T17:51:57.777ZT14:26:40"
  },
  {
    "version": 5,
    "ip_address": "53.87.156.63",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-03",
    "time": "2023-11-23T13:47:57.810ZT10:14:24"
  },
  {
    "version": 6,
    "ip_address": "182.172.12.30",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-07",
    "time": "2023-07-17T19:49:49.405ZT08:53:02"
  },
  {
    "version": 10,
    "ip_address": "10.35.175.247",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-06",
    "time": "2023-04-08T02:08:45.925ZT15:55:18"
  },
  {
    "version": 5,
    "ip_address": "53.206.128.71",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-24",
    "time": "2023-08-07T08:28:54.412ZT17:53:31"
  },
  {
    "version": 7,
    "ip_address": "188.42.97.107",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-11",
    "time": "2023-01-17T13:21:56.518ZT16:29:33"
  },
  {
    "version": 10,
    "ip_address": "136.78.9.233",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-17",
    "time": "2023-07-14T06:29:46.598ZT12:30:06"
  },
  {
    "version": 3,
    "ip_address": "201.76.149.196",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-21",
    "time": "2023-07-17T13:53:20.620ZT20:12:40"
  },
  {
    "version": 3,
    "ip_address": "222.9.77.104",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-15",
    "time": "2023-06-16T06:00:00.015ZT20:14:37"
  },
  {
    "version": 7,
    "ip_address": "184.54.192.102",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-26",
    "time": "2023-08-18T20:18:34.899ZT14:00:02"
  },
  {
    "version": 9,
    "ip_address": "30.254.219.147",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-25",
    "time": "2023-05-13T22:27:09.026ZT01:52:40"
  },
  {
    "version": 6,
    "ip_address": "102.32.164.224",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-16",
    "time": "2023-10-04T11:35:06.399ZT14:15:27"
  },
  {
    "version": 8,
    "ip_address": "85.219.156.158",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-15",
    "time": "2023-10-20T10:58:12.431ZT11:25:53"
  },
  {
    "version": 3,
    "ip_address": "103.20.9.123",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-19",
    "time": "2023-02-23T20:05:43.718ZT00:06:33"
  },
  {
    "version": 3,
    "ip_address": "24.15.5.143",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-01",
    "time": "2023-05-17T03:40:45.406ZT11:12:24"
  },
  {
    "version": 1,
    "ip_address": "9.88.88.225",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-30",
    "time": "2023-02-03T07:24:33.566ZT09:28:16"
  },
  {
    "version": 10,
    "ip_address": "35.3.75.63",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-30",
    "time": "2023-03-25T02:52:53.383ZT01:15:11"
  },
  {
    "version": 7,
    "ip_address": "163.180.163.69",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-21",
    "time": "2023-09-28T20:11:25.467ZT14:16:41"
  },
  {
    "version": 10,
    "ip_address": "183.26.177.103",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-13",
    "time": "2023-02-17T10:33:10.028ZT19:40:24"
  },
  {
    "version": 9,
    "ip_address": "172.101.245.250",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-20",
    "time": "2023-04-22T05:45:26.870ZT21:42:41"
  },
  {
    "version": 7,
    "ip_address": "126.196.44.197",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-26",
    "time": "2023-01-23T09:25:55.623ZT21:34:50"
  },
  {
    "version": 2,
    "ip_address": "238.56.18.113",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-25",
    "time": "2023-05-24T04:46:19.590ZT16:16:06"
  },
  {
    "version": 1,
    "ip_address": "1.97.31.125",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-01",
    "time": "2023-05-05T12:10:17.929ZT07:13:09"
  },
  {
    "version": 7,
    "ip_address": "17.75.152.9",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-12",
    "time": "2023-01-18T14:09:10.558ZT21:10:21"
  },
  {
    "version": 6,
    "ip_address": "146.198.45.176",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-23",
    "time": "2023-12-12T12:13:57.566ZT04:11:46"
  },
  {
    "version": 2,
    "ip_address": "150.32.50.119",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-01",
    "time": "2023-10-04T19:05:40.707ZT10:57:16"
  },
  {
    "version": 4,
    "ip_address": "37.25.167.144",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-07",
    "time": "2023-08-05T04:05:06.042ZT17:04:42"
  },
  {
    "version": 9,
    "ip_address": "20.100.9.103",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-03",
    "time": "2023-08-18T18:53:08.483ZT11:15:14"
  },
  {
    "version": 9,
    "ip_address": "100.34.34.117",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-30",
    "time": "2023-07-12T10:49:18.544ZT13:24:40"
  },
  {
    "version": 2,
    "ip_address": "29.179.198.197",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-11",
    "time": "2023-07-23T22:16:29.581ZT21:35:35"
  },
  {
    "version": 2,
    "ip_address": "202.56.15.42",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-11",
    "time": "2023-02-13T17:19:42.972ZT17:34:40"
  },
  {
    "version": 2,
    "ip_address": "136.112.68.21",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-06",
    "time": "2023-02-06T21:02:32.237ZT16:43:54"
  },
  {
    "version": 8,
    "ip_address": "175.21.205.106",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-30",
    "time": "2023-04-22T20:44:52.187ZT17:19:34"
  },
  {
    "version": 7,
    "ip_address": "227.207.238.251",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-01",
    "time": "2023-12-19T15:28:34.128ZT18:23:23"
  },
  {
    "version": 8,
    "ip_address": "209.185.178.33",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-19",
    "time": "2023-04-13T23:33:16.305ZT02:45:41"
  },
  {
    "version": 2,
    "ip_address": "198.126.203.128",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-01",
    "time": "2023-09-04T17:13:36.767ZT20:10:09"
  },
  {
    "version": 3,
    "ip_address": "136.22.34.128",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-01",
    "time": "2023-01-13T08:03:15.875ZT05:55:35"
  },
  {
    "version": 6,
    "ip_address": "104.148.70.233",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-24",
    "time": "2023-04-27T03:58:24.304ZT21:25:58"
  },
  {
    "version": 10,
    "ip_address": "65.54.41.65",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-24",
    "time": "2023-05-23T07:38:23.566ZT11:42:40"
  },
  {
    "version": 7,
    "ip_address": "160.242.87.48",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-11",
    "time": "2023-04-15T12:41:15.122ZT00:14:09"
  },
  {
    "version": 2,
    "ip_address": "136.131.18.31",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-23",
    "time": "2023-09-23T09:19:21.241ZT22:56:41"
  },
  {
    "version": 4,
    "ip_address": "42.194.218.20",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-22",
    "time": "2023-02-19T15:57:39.515ZT00:14:43"
  },
  {
    "version": 9,
    "ip_address": "236.24.255.60",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-13",
    "time": "2023-11-29T02:27:50.498ZT20:35:49"
  },
  {
    "version": 10,
    "ip_address": "109.248.112.108",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-15",
    "time": "2023-03-22T13:36:08.224ZT19:17:00"
  },
  {
    "version": 8,
    "ip_address": "131.143.239.27",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-20",
    "time": "2023-05-24T09:29:51.643ZT05:15:22"
  },
  {
    "version": 10,
    "ip_address": "145.130.90.197",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-12",
    "time": "2023-11-18T06:46:20.611ZT22:11:21"
  },
  {
    "version": 2,
    "ip_address": "135.245.34.79",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-27",
    "time": "2023-07-03T13:30:06.081ZT07:52:24"
  },
  {
    "version": 5,
    "ip_address": "74.15.255.30",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-19",
    "time": "2023-04-04T19:46:54.470ZT15:21:41"
  },
  {
    "version": 4,
    "ip_address": "30.102.203.96",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-31",
    "time": "2023-11-13T12:14:31.646ZT11:00:00"
  },
  {
    "version": 6,
    "ip_address": "172.111.158.138",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-12",
    "time": "2023-08-22T04:45:38.726ZT17:05:32"
  },
  {
    "version": 6,
    "ip_address": "69.12.104.170",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-14",
    "time": "2023-09-04T14:30:20.976ZT05:13:57"
  },
  {
    "version": 5,
    "ip_address": "159.50.189.37",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-06",
    "time": "2023-08-04T16:22:04.391ZT15:14:53"
  },
  {
    "version": 7,
    "ip_address": "38.125.163.248",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-25",
    "time": "2023-01-24T13:28:54.184ZT00:13:19"
  },
  {
    "version": 7,
    "ip_address": "68.190.195.202",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-18",
    "time": "2023-08-26T01:33:15.179ZT18:10:04"
  },
  {
    "version": 3,
    "ip_address": "181.151.140.190",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-02",
    "time": "2023-11-12T12:46:35.209ZT17:07:32"
  },
  {
    "version": 6,
    "ip_address": "131.139.74.105",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-29",
    "time": "2023-12-29T08:17:56.521ZT12:40:43"
  },
  {
    "version": 2,
    "ip_address": "14.89.145.228",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-17",
    "time": "2023-04-29T09:43:44.827ZT06:46:13"
  },
  {
    "version": 10,
    "ip_address": "11.55.155.152",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-03",
    "time": "2023-08-17T22:03:37.633ZT10:39:00"
  },
  {
    "version": 1,
    "ip_address": "137.249.207.230",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-07",
    "time": "2023-10-08T22:11:28.729ZT17:19:29"
  },
  {
    "version": 5,
    "ip_address": "189.18.166.69",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-01",
    "time": "2023-05-28T03:36:31.685ZT06:56:08"
  },
  {
    "version": 5,
    "ip_address": "239.152.76.55",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-14",
    "time": "2023-08-25T07:30:43.854ZT07:00:57"
  },
  {
    "version": 6,
    "ip_address": "142.140.33.107",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-27",
    "time": "2023-12-24T22:30:57.698ZT14:22:03"
  },
  {
    "version": 8,
    "ip_address": "219.26.229.117",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-28",
    "time": "2023-10-12T08:40:56.619ZT03:52:20"
  },
  {
    "version": 6,
    "ip_address": "167.182.208.103",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-03",
    "time": "2023-01-17T09:05:16.705ZT03:57:48"
  },
  {
    "version": 3,
    "ip_address": "205.174.53.113",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-05",
    "time": "2023-01-25T05:47:28.024ZT01:27:59"
  },
  {
    "version": 7,
    "ip_address": "253.253.188.133",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-17",
    "time": "2023-10-29T17:50:48.022ZT06:17:47"
  },
  {
    "version": 4,
    "ip_address": "144.25.178.7",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-12",
    "time": "2023-07-27T01:51:38.428ZT21:26:14"
  },
  {
    "version": 9,
    "ip_address": "36.173.44.144",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-25",
    "time": "2023-09-21T08:02:15.648ZT14:23:15"
  },
  {
    "version": 6,
    "ip_address": "51.231.202.195",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-22",
    "time": "2023-09-02T21:56:34.267ZT13:35:59"
  },
  {
    "version": 2,
    "ip_address": "135.149.162.151",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-20",
    "time": "2023-04-19T13:07:56.234ZT14:30:42"
  },
  {
    "version": 4,
    "ip_address": "180.188.28.196",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-17",
    "time": "2023-03-05T17:01:48.436ZT08:30:51"
  },
  {
    "version": 3,
    "ip_address": "223.0.184.200",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-18",
    "time": "2023-05-26T08:41:27.574ZT05:50:26"
  },
  {
    "version": 4,
    "ip_address": "124.220.253.57",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-16",
    "time": "2023-03-20T11:16:00.259ZT05:17:24"
  },
  {
    "version": 8,
    "ip_address": "203.237.133.163",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-04",
    "time": "2023-01-08T11:59:12.051ZT15:02:48"
  },
  {
    "version": 6,
    "ip_address": "135.2.245.22",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-17",
    "time": "2023-02-27T21:52:42.638ZT08:59:46"
  },
  {
    "version": 10,
    "ip_address": "43.78.8.69",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-01",
    "time": "2023-05-15T13:03:32.679ZT14:20:07"
  },
  {
    "version": 3,
    "ip_address": "59.252.27.82",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-02",
    "time": "2023-07-23T17:02:34.096ZT16:22:19"
  },
  {
    "version": 6,
    "ip_address": "75.105.114.153",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-20",
    "time": "2023-03-18T15:38:36.611ZT13:07:14"
  },
  {
    "version": 2,
    "ip_address": "163.189.239.252",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-31",
    "time": "2023-11-10T20:56:24.975ZT07:29:08"
  },
  {
    "version": 1,
    "ip_address": "104.133.85.48",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-26",
    "time": "2023-02-16T16:08:41.808ZT02:16:01"
  },
  {
    "version": 4,
    "ip_address": "3.213.152.40",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-14",
    "time": "2023-07-27T22:30:52.903ZT08:24:58"
  },
  {
    "version": 7,
    "ip_address": "172.218.254.94",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-06",
    "time": "2023-09-06T11:02:02.253ZT21:44:38"
  },
  {
    "version": 10,
    "ip_address": "74.60.18.65",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-13",
    "time": "2023-08-22T15:04:55.217ZT05:58:00"
  },
  {
    "version": 10,
    "ip_address": "108.3.183.150",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-05",
    "time": "2023-12-23T23:17:45.488ZT14:07:15"
  },
  {
    "version": 7,
    "ip_address": "75.9.85.166",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-21",
    "time": "2023-02-11T07:46:20.121ZT15:18:32"
  },
  {
    "version": 6,
    "ip_address": "253.150.8.8",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-27",
    "time": "2023-10-22T14:43:41.183ZT04:53:57"
  },
  {
    "version": 6,
    "ip_address": "129.242.171.127",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-21",
    "time": "2023-09-13T21:06:11.849ZT16:25:18"
  },
  {
    "version": 1,
    "ip_address": "32.3.72.29",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-07",
    "time": "2023-10-09T00:56:49.364ZT12:19:41"
  },
  {
    "version": 4,
    "ip_address": "208.35.70.134",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-31",
    "time": "2023-08-25T02:07:42.342ZT11:09:06"
  },
  {
    "version": 9,
    "ip_address": "229.186.9.241",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-07",
    "time": "2023-05-19T23:29:56.384ZT21:26:20"
  },
  {
    "version": 8,
    "ip_address": "240.154.167.113",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-13",
    "time": "2023-11-10T01:23:19.947ZT00:42:29"
  },
  {
    "version": 3,
    "ip_address": "50.192.169.13",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-20",
    "time": "2023-02-03T20:48:59.237ZT08:02:00"
  },
  {
    "version": 9,
    "ip_address": "135.0.247.117",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-21",
    "time": "2023-08-27T04:50:55.082ZT18:16:39"
  },
  {
    "version": 6,
    "ip_address": "194.45.22.54",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-12",
    "time": "2023-06-30T14:36:16.483ZT23:16:15"
  },
  {
    "version": 7,
    "ip_address": "182.73.68.58",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-14",
    "time": "2023-07-31T09:14:48.882ZT13:05:34"
  },
  {
    "version": 8,
    "ip_address": "238.3.78.136",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-24",
    "time": "2023-05-07T23:21:27.829ZT11:49:58"
  },
  {
    "version": 5,
    "ip_address": "76.236.21.145",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-19",
    "time": "2023-11-14T14:13:18.930ZT08:50:31"
  },
  {
    "version": 10,
    "ip_address": "97.77.223.41",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-29",
    "time": "2023-12-21T01:46:04.528ZT19:12:55"
  },
  {
    "version": 2,
    "ip_address": "170.53.178.165",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-17",
    "time": "2023-11-20T06:09:41.629ZT12:08:02"
  },
  {
    "version": 6,
    "ip_address": "107.97.228.117",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-09",
    "time": "2023-05-26T14:45:17.328ZT06:06:14"
  },
  {
    "version": 4,
    "ip_address": "188.116.203.253",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-02",
    "time": "2023-08-14T10:21:51.277ZT23:32:58"
  },
  {
    "version": 10,
    "ip_address": "232.100.92.155",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-19",
    "time": "2023-01-24T15:11:25.614ZT14:49:36"
  },
  {
    "version": 9,
    "ip_address": "7.54.26.18",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-15",
    "time": "2023-02-08T18:57:17.056ZT01:59:40"
  },
  {
    "version": 5,
    "ip_address": "232.254.216.83",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-22",
    "time": "2023-06-03T19:38:52.690ZT11:46:51"
  },
  {
    "version": 9,
    "ip_address": "197.26.167.25",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-30",
    "time": "2023-12-10T03:03:04.898ZT11:09:22"
  },
  {
    "version": 9,
    "ip_address": "185.108.12.74",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-21",
    "time": "2023-04-18T22:46:23.866ZT10:59:57"
  },
  {
    "version": 2,
    "ip_address": "107.254.78.104",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-06",
    "time": "2023-11-19T14:18:02.241ZT08:34:40"
  },
  {
    "version": 9,
    "ip_address": "211.105.131.98",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-01",
    "time": "2023-09-16T17:22:12.556ZT00:39:52"
  },
  {
    "version": 7,
    "ip_address": "212.112.105.137",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-28",
    "time": "2023-09-22T03:58:00.372ZT21:59:11"
  },
  {
    "version": 4,
    "ip_address": "194.0.170.30",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-07",
    "time": "2023-07-19T11:48:48.423ZT11:55:59"
  },
  {
    "version": 6,
    "ip_address": "91.251.93.121",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-25",
    "time": "2023-04-28T12:39:28.843ZT14:51:54"
  },
  {
    "version": 4,
    "ip_address": "21.202.177.181",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-11",
    "time": "2023-08-15T13:38:34.149ZT12:53:51"
  },
  {
    "version": 4,
    "ip_address": "182.2.191.138",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-02",
    "time": "2023-08-22T04:10:08.512ZT06:48:28"
  },
  {
    "version": 5,
    "ip_address": "198.97.225.148",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-21",
    "time": "2023-10-24T20:12:38.984ZT18:01:15"
  },
  {
    "version": 1,
    "ip_address": "252.26.224.2",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-22",
    "time": "2023-08-28T17:57:13.327ZT09:27:36"
  },
  {
    "version": 5,
    "ip_address": "158.141.5.24",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-30",
    "time": "2023-09-21T12:26:29.085ZT19:17:53"
  },
  {
    "version": 5,
    "ip_address": "161.94.199.117",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-12",
    "time": "2023-09-21T06:21:05.429ZT08:17:46"
  },
  {
    "version": 10,
    "ip_address": "111.216.107.241",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-31",
    "time": "2023-10-08T15:09:33.227ZT11:16:08"
  },
  {
    "version": 8,
    "ip_address": "170.193.158.4",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-07",
    "time": "2023-07-23T09:13:56.083ZT16:46:13"
  },
  {
    "version": 5,
    "ip_address": "151.162.153.250",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-29",
    "time": "2023-12-11T04:27:36.806ZT11:36:43"
  },
  {
    "version": 8,
    "ip_address": "68.238.166.96",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-05",
    "time": "2023-01-31T07:18:04.233ZT14:57:15"
  },
  {
    "version": 8,
    "ip_address": "121.150.97.12",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-21",
    "time": "2023-05-29T19:29:36.769ZT08:34:21"
  },
  {
    "version": 8,
    "ip_address": "36.133.152.203",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-04",
    "time": "2023-08-23T10:57:26.220ZT19:44:36"
  },
  {
    "version": 6,
    "ip_address": "145.55.251.89",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-23",
    "time": "2023-07-26T03:21:45.092ZT14:23:24"
  },
  {
    "version": 8,
    "ip_address": "81.140.248.233",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-02",
    "time": "2023-05-30T10:56:48.995ZT23:34:44"
  },
  {
    "version": 9,
    "ip_address": "19.191.182.128",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-15",
    "time": "2023-05-23T21:06:47.093ZT23:29:55"
  },
  {
    "version": 8,
    "ip_address": "207.184.146.150",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-16",
    "time": "2023-01-27T07:09:56.201ZT17:25:08"
  },
  {
    "version": 7,
    "ip_address": "162.170.16.169",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-13T09:55:38.267ZT12:52:35"
  },
  {
    "version": 7,
    "ip_address": "21.234.42.220",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-26",
    "time": "2023-12-15T13:49:53.169ZT11:24:09"
  },
  {
    "version": 7,
    "ip_address": "87.35.42.100",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-21",
    "time": "2023-03-10T02:46:57.341ZT14:21:35"
  },
  {
    "version": 8,
    "ip_address": "87.93.170.113",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-05",
    "time": "2023-08-05T13:14:06.858ZT22:27:07"
  },
  {
    "version": 1,
    "ip_address": "8.37.172.127",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-12",
    "time": "2023-03-22T18:19:33.536ZT14:44:11"
  },
  {
    "version": 4,
    "ip_address": "122.2.47.11",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-12",
    "time": "2023-06-08T12:53:30.847ZT23:26:04"
  },
  {
    "version": 9,
    "ip_address": "42.33.219.218",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-01",
    "time": "2023-09-05T15:42:21.294ZT16:02:08"
  },
  {
    "version": 9,
    "ip_address": "69.61.206.188",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-03",
    "time": "2023-11-19T18:54:00.652ZT17:37:38"
  },
  {
    "version": 9,
    "ip_address": "238.208.246.43",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-06",
    "time": "2023-09-01T20:19:06.330ZT13:36:52"
  },
  {
    "version": 6,
    "ip_address": "182.95.1.248",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-21",
    "time": "2023-10-04T14:49:44.071ZT00:32:39"
  },
  {
    "version": 4,
    "ip_address": "147.3.134.26",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-07",
    "time": "2023-07-26T21:39:13.258ZT01:04:18"
  },
  {
    "version": 4,
    "ip_address": "120.124.158.225",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-30",
    "time": "2023-04-09T10:55:14.926ZT08:08:21"
  },
  {
    "version": 3,
    "ip_address": "222.22.169.217",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-12",
    "time": "2023-12-27T14:28:20.292ZT12:27:22"
  },
  {
    "version": 3,
    "ip_address": "215.129.210.84",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-11",
    "time": "2023-07-05T04:59:01.085ZT04:26:20"
  },
  {
    "version": 4,
    "ip_address": "86.208.181.104",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-26",
    "time": "2023-10-14T01:34:20.029ZT06:54:29"
  },
  {
    "version": 4,
    "ip_address": "88.130.162.4",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-14",
    "time": "2023-02-02T01:52:38.858ZT16:19:25"
  },
  {
    "version": 7,
    "ip_address": "84.31.11.207",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-01",
    "time": "2023-03-20T06:50:30.771ZT12:04:37"
  },
  {
    "version": 7,
    "ip_address": "132.95.61.23",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-26",
    "time": "2023-05-16T08:16:57.231ZT16:02:02"
  },
  {
    "version": 2,
    "ip_address": "16.44.234.230",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-14",
    "time": "2023-01-05T05:42:08.290ZT03:11:30"
  },
  {
    "version": 6,
    "ip_address": "154.107.69.179",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-24",
    "time": "2023-01-30T21:55:56.555ZT19:00:40"
  },
  {
    "version": 9,
    "ip_address": "248.73.27.211",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-11",
    "time": "2023-06-06T19:51:16.111ZT17:34:03"
  },
  {
    "version": 4,
    "ip_address": "124.30.137.208",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-14",
    "time": "2023-04-25T04:43:32.083ZT15:07:34"
  },
  {
    "version": 7,
    "ip_address": "27.5.159.35",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-27",
    "time": "2023-07-04T07:32:20.893ZT01:49:49"
  },
  {
    "version": 10,
    "ip_address": "24.119.248.109",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-14",
    "time": "2023-06-11T09:36:21.372ZT03:06:08"
  },
  {
    "version": 6,
    "ip_address": "200.140.11.55",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-12",
    "time": "2023-08-09T19:56:26.649ZT15:58:49"
  },
  {
    "version": 8,
    "ip_address": "134.65.19.131",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-08",
    "time": "2023-02-25T18:58:23.125ZT06:04:37"
  },
  {
    "version": 9,
    "ip_address": "152.183.104.166",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-03",
    "time": "2023-08-16T23:02:15.065ZT20:20:42"
  },
  {
    "version": 9,
    "ip_address": "126.216.114.148",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-07",
    "time": "2023-01-30T08:26:34.421ZT11:07:11"
  },
  {
    "version": 8,
    "ip_address": "90.210.26.144",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-07",
    "time": "2023-09-20T05:42:47.132ZT03:28:58"
  },
  {
    "version": 2,
    "ip_address": "53.203.205.73",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-10",
    "time": "2023-07-05T10:19:14.656ZT18:17:10"
  },
  {
    "version": 10,
    "ip_address": "146.164.103.75",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-18",
    "time": "2023-03-11T05:35:02.916ZT06:22:34"
  },
  {
    "version": 8,
    "ip_address": "132.67.35.29",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-15",
    "time": "2023-04-06T01:14:54.414ZT18:40:18"
  },
  {
    "version": 2,
    "ip_address": "200.71.79.60",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-06",
    "time": "2023-02-04T07:27:42.666ZT16:49:05"
  },
  {
    "version": 1,
    "ip_address": "190.212.5.35",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-02",
    "time": "2023-09-11T17:51:51.038ZT12:54:01"
  },
  {
    "version": 2,
    "ip_address": "91.209.71.241",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-01",
    "time": "2023-03-01T04:14:43.327ZT17:53:13"
  },
  {
    "version": 2,
    "ip_address": "246.236.193.77",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-16",
    "time": "2023-10-11T18:42:39.606ZT07:21:06"
  },
  {
    "version": 2,
    "ip_address": "122.248.21.90",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-28",
    "time": "2023-02-15T01:32:53.311ZT19:17:18"
  },
  {
    "version": 5,
    "ip_address": "1.7.120.86",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-29",
    "time": "2023-03-24T23:42:19.776ZT11:04:11"
  },
  {
    "version": 7,
    "ip_address": "24.19.31.167",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-04",
    "time": "2023-05-19T03:20:19.090ZT03:39:47"
  },
  {
    "version": 8,
    "ip_address": "92.124.120.205",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-02",
    "time": "2023-02-02T12:29:48.202ZT01:45:28"
  },
  {
    "version": 10,
    "ip_address": "213.6.229.136",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-25",
    "time": "2023-01-25T07:19:37.871ZT05:40:54"
  },
  {
    "version": 4,
    "ip_address": "189.140.28.191",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-17",
    "time": "2023-01-05T05:05:22.315ZT20:16:31"
  },
  {
    "version": 8,
    "ip_address": "30.179.197.11",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-27",
    "time": "2023-03-09T22:18:19.466ZT09:43:59"
  },
  {
    "version": 1,
    "ip_address": "48.200.44.58",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-06",
    "time": "2023-03-05T21:45:55.916ZT18:25:13"
  },
  {
    "version": 5,
    "ip_address": "243.245.101.68",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-22",
    "time": "2023-12-05T06:28:53.597ZT18:49:41"
  },
  {
    "version": 5,
    "ip_address": "56.121.114.87",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-15",
    "time": "2023-07-03T22:47:25.920ZT12:20:20"
  },
  {
    "version": 6,
    "ip_address": "119.162.94.47",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-12",
    "time": "2023-10-22T22:31:45.216ZT16:19:26"
  },
  {
    "version": 7,
    "ip_address": "17.69.84.57",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-31",
    "time": "2023-05-20T12:59:15.870ZT19:53:01"
  },
  {
    "version": 10,
    "ip_address": "40.235.154.107",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-03",
    "time": "2023-07-12T18:42:07.651ZT10:39:21"
  },
  {
    "version": 1,
    "ip_address": "96.6.239.124",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-13",
    "time": "2023-12-06T15:44:24.032ZT15:55:11"
  },
  {
    "version": 10,
    "ip_address": "164.132.23.98",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-30",
    "time": "2023-09-18T00:55:07.494ZT05:39:29"
  },
  {
    "version": 2,
    "ip_address": "207.125.160.122",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-17",
    "time": "2023-06-11T12:10:09.887ZT01:10:05"
  },
  {
    "version": 8,
    "ip_address": "123.97.189.66",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-18",
    "time": "2023-05-07T14:09:11.239ZT09:38:34"
  },
  {
    "version": 5,
    "ip_address": "221.222.90.173",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-28",
    "time": "2023-01-25T14:33:36.841ZT22:17:01"
  },
  {
    "version": 1,
    "ip_address": "37.239.202.93",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-21",
    "time": "2023-10-16T10:08:57.136ZT18:20:25"
  },
  {
    "version": 4,
    "ip_address": "142.227.146.196",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-30",
    "time": "2023-08-16T16:51:07.735ZT10:45:41"
  },
  {
    "version": 9,
    "ip_address": "232.150.116.195",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-30",
    "time": "2023-02-25T14:29:08.331ZT11:42:31"
  },
  {
    "version": 1,
    "ip_address": "51.21.251.169",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-16",
    "time": "2023-06-17T14:35:52.001ZT01:27:03"
  },
  {
    "version": 10,
    "ip_address": "248.129.89.52",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-27",
    "time": "2023-03-13T08:45:48.626ZT04:57:24"
  },
  {
    "version": 5,
    "ip_address": "157.36.6.105",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-12",
    "time": "2023-12-01T10:09:45.244ZT11:23:05"
  },
  {
    "version": 9,
    "ip_address": "158.5.229.195",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-26",
    "time": "2023-01-14T03:10:18.392ZT03:39:50"
  },
  {
    "version": 3,
    "ip_address": "193.143.68.123",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-19",
    "time": "2023-04-05T02:01:32.554ZT01:08:55"
  },
  {
    "version": 6,
    "ip_address": "228.75.222.201",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-09",
    "time": "2023-09-20T23:40:21.400ZT00:14:48"
  },
  {
    "version": 6,
    "ip_address": "112.146.17.224",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-13",
    "time": "2023-02-08T23:43:19.471ZT18:07:01"
  },
  {
    "version": 7,
    "ip_address": "254.175.198.171",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-06",
    "time": "2023-10-12T04:16:32.724ZT03:26:02"
  },
  {
    "version": 6,
    "ip_address": "236.245.154.170",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-12",
    "time": "2023-12-02T13:54:31.481ZT12:44:55"
  },
  {
    "version": 7,
    "ip_address": "149.201.105.39",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-30",
    "time": "2023-03-25T07:44:28.270ZT09:30:08"
  },
  {
    "version": 5,
    "ip_address": "74.102.11.254",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-22",
    "time": "2023-12-21T13:25:43.291ZT17:08:48"
  },
  {
    "version": 7,
    "ip_address": "118.39.219.150",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-15",
    "time": "2023-10-10T02:05:37.293ZT06:49:23"
  },
  {
    "version": 7,
    "ip_address": "79.16.96.114",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-24",
    "time": "2023-04-27T04:23:29.266ZT12:51:48"
  },
  {
    "version": 7,
    "ip_address": "67.201.169.48",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-09",
    "time": "2023-12-06T16:06:28.297ZT17:16:24"
  },
  {
    "version": 5,
    "ip_address": "160.163.135.6",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-08",
    "time": "2023-11-26T09:12:38.900ZT16:03:54"
  },
  {
    "version": 1,
    "ip_address": "80.171.12.157",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-30",
    "time": "2023-08-01T02:04:58.332ZT07:14:29"
  },
  {
    "version": 6,
    "ip_address": "1.230.69.175",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-17",
    "time": "2023-11-01T09:08:27.243ZT17:43:33"
  },
  {
    "version": 6,
    "ip_address": "108.211.116.129",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-13",
    "time": "2023-01-24T13:36:29.977ZT00:00:57"
  },
  {
    "version": 9,
    "ip_address": "112.185.176.76",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-05",
    "time": "2023-10-21T14:15:34.266ZT13:57:18"
  },
  {
    "version": 3,
    "ip_address": "197.104.247.17",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-22",
    "time": "2023-10-23T20:40:12.980ZT00:08:43"
  },
  {
    "version": 3,
    "ip_address": "196.48.175.248",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-22",
    "time": "2023-06-14T09:59:29.720ZT10:19:33"
  },
  {
    "version": 6,
    "ip_address": "29.36.21.117",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-19",
    "time": "2023-10-30T18:28:22.560ZT18:12:09"
  },
  {
    "version": 9,
    "ip_address": "255.143.71.219",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-04",
    "time": "2023-09-12T05:17:00.279ZT20:53:01"
  },
  {
    "version": 4,
    "ip_address": "35.195.169.111",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-14",
    "time": "2023-02-25T00:06:03.904ZT12:59:27"
  },
  {
    "version": 10,
    "ip_address": "37.117.82.82",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-07",
    "time": "2023-10-01T17:35:06.579ZT19:27:48"
  },
  {
    "version": 2,
    "ip_address": "161.52.153.246",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-17",
    "time": "2023-05-22T15:49:46.325ZT06:43:46"
  },
  {
    "version": 3,
    "ip_address": "174.94.182.23",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-08",
    "time": "2023-08-06T17:59:18.698ZT22:34:43"
  },
  {
    "version": 2,
    "ip_address": "45.233.227.181",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-07",
    "time": "2023-07-26T03:15:05.744ZT10:29:43"
  },
  {
    "version": 1,
    "ip_address": "194.72.99.57",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-27",
    "time": "2023-09-16T23:52:42.176ZT16:42:34"
  },
  {
    "version": 3,
    "ip_address": "106.190.206.149",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-21",
    "time": "2023-12-07T11:38:14.192ZT22:15:19"
  },
  {
    "version": 2,
    "ip_address": "110.152.232.147",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-17",
    "time": "2023-05-12T05:16:38.125ZT06:29:34"
  },
  {
    "version": 3,
    "ip_address": "35.142.96.117",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-07",
    "time": "2023-04-01T14:28:46.968ZT07:37:21"
  },
  {
    "version": 4,
    "ip_address": "9.23.138.121",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-02",
    "time": "2023-10-08T17:56:55.234ZT08:23:39"
  },
  {
    "version": 2,
    "ip_address": "90.231.195.117",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-12",
    "time": "2023-10-04T08:14:55.461ZT11:54:05"
  },
  {
    "version": 3,
    "ip_address": "233.126.1.239",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-06",
    "time": "2023-08-18T19:17:16.386ZT17:49:27"
  },
  {
    "version": 7,
    "ip_address": "87.29.72.229",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-02",
    "time": "2023-05-17T05:59:09.277ZT14:44:48"
  },
  {
    "version": 3,
    "ip_address": "94.73.74.129",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-11",
    "time": "2023-06-04T14:59:23.103ZT16:59:17"
  },
  {
    "version": 8,
    "ip_address": "15.19.10.239",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-18",
    "time": "2023-03-22T05:19:07.192ZT00:49:20"
  },
  {
    "version": 8,
    "ip_address": "252.230.2.208",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-14",
    "time": "2023-10-25T10:12:26.028ZT01:57:11"
  },
  {
    "version": 3,
    "ip_address": "14.151.30.37",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-07",
    "time": "2023-07-27T04:15:34.208ZT00:58:18"
  },
  {
    "version": 6,
    "ip_address": "123.95.245.126",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-09",
    "time": "2023-03-22T21:48:59.995ZT14:20:15"
  },
  {
    "version": 1,
    "ip_address": "97.249.206.70",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-08",
    "time": "2023-10-26T02:31:26.432ZT21:29:33"
  },
  {
    "version": 6,
    "ip_address": "214.183.7.39",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-23",
    "time": "2023-10-12T19:32:42.087ZT19:26:01"
  },
  {
    "version": 3,
    "ip_address": "6.176.24.249",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-27",
    "time": "2023-04-26T13:52:26.959ZT03:19:48"
  },
  {
    "version": 8,
    "ip_address": "229.212.175.213",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-07",
    "time": "2023-02-16T10:39:43.786ZT15:35:45"
  },
  {
    "version": 10,
    "ip_address": "121.145.5.239",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-02",
    "time": "2023-02-10T05:41:45.705ZT23:01:21"
  },
  {
    "version": 7,
    "ip_address": "252.188.139.172",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-16",
    "time": "2023-01-20T15:56:39.628ZT07:36:22"
  },
  {
    "version": 7,
    "ip_address": "113.109.240.26",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-02",
    "time": "2023-12-04T20:44:10.864ZT12:25:33"
  },
  {
    "version": 8,
    "ip_address": "195.3.129.233",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-26",
    "time": "2023-03-22T23:01:30.256ZT18:59:45"
  },
  {
    "version": 1,
    "ip_address": "188.185.209.240",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-25",
    "time": "2023-04-28T13:41:55.708ZT08:03:11"
  },
  {
    "version": 9,
    "ip_address": "222.244.14.2",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-13",
    "time": "2023-12-17T21:26:55.612ZT22:06:56"
  },
  {
    "version": 4,
    "ip_address": "155.73.135.157",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-23",
    "time": "2023-08-25T02:20:59.946ZT13:34:51"
  },
  {
    "version": 5,
    "ip_address": "74.132.167.181",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-27",
    "time": "2023-06-23T00:36:08.816ZT11:52:16"
  },
  {
    "version": 4,
    "ip_address": "159.23.23.116",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-03",
    "time": "2023-11-07T00:25:42.658ZT11:29:01"
  },
  {
    "version": 10,
    "ip_address": "222.189.72.175",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-13",
    "time": "2023-05-20T15:13:41.198ZT07:14:30"
  },
  {
    "version": 5,
    "ip_address": "215.121.46.30",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-19",
    "time": "2023-10-02T05:45:01.811ZT06:19:50"
  },
  {
    "version": 2,
    "ip_address": "96.198.127.132",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-27",
    "time": "2023-12-10T10:19:58.444ZT14:16:04"
  },
  {
    "version": 7,
    "ip_address": "134.175.154.147",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-08",
    "time": "2023-04-07T16:20:50.882ZT08:06:44"
  },
  {
    "version": 3,
    "ip_address": "159.51.214.174",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-16",
    "time": "2023-10-24T22:24:07.153ZT21:37:00"
  },
  {
    "version": 9,
    "ip_address": "241.188.243.50",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-23",
    "time": "2023-11-10T10:53:33.744ZT13:40:42"
  },
  {
    "version": 7,
    "ip_address": "254.173.96.29",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-10",
    "time": "2023-11-01T19:03:16.154ZT03:12:18"
  },
  {
    "version": 6,
    "ip_address": "74.72.33.84",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-19",
    "time": "2023-09-08T05:15:44.415ZT09:51:57"
  },
  {
    "version": 10,
    "ip_address": "207.32.63.118",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-10",
    "time": "2023-10-23T08:20:54.888ZT12:25:40"
  },
  {
    "version": 10,
    "ip_address": "236.97.178.156",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-01",
    "time": "2023-08-13T13:04:39.446ZT14:50:58"
  },
  {
    "version": 6,
    "ip_address": "4.171.171.209",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-02",
    "time": "2023-11-08T04:14:29.056ZT08:08:55"
  },
  {
    "version": 9,
    "ip_address": "110.235.75.79",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-27",
    "time": "2023-10-25T18:20:20.967ZT01:32:09"
  },
  {
    "version": 1,
    "ip_address": "97.196.29.12",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-23",
    "time": "2023-02-01T18:27:32.163ZT03:30:37"
  },
  {
    "version": 9,
    "ip_address": "86.127.41.211",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-14",
    "time": "2023-05-21T23:38:24.198ZT15:37:34"
  },
  {
    "version": 5,
    "ip_address": "150.135.0.172",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-10",
    "time": "2023-05-22T18:58:51.197ZT12:39:23"
  },
  {
    "version": 8,
    "ip_address": "224.46.158.39",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-30",
    "time": "2023-09-14T04:06:07.845ZT22:59:07"
  },
  {
    "version": 1,
    "ip_address": "186.199.99.223",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-08",
    "time": "2023-10-01T22:29:21.788ZT02:29:49"
  },
  {
    "version": 7,
    "ip_address": "146.109.30.247",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-06",
    "time": "2023-03-20T01:38:18.064ZT23:23:52"
  },
  {
    "version": 3,
    "ip_address": "8.235.123.39",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-08",
    "time": "2023-07-13T01:11:38.270ZT18:39:16"
  },
  {
    "version": 3,
    "ip_address": "35.191.247.241",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-26",
    "time": "2023-01-09T21:19:15.369ZT17:43:56"
  },
  {
    "version": 8,
    "ip_address": "246.149.19.153",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-14",
    "time": "2023-03-19T02:51:35.362ZT14:47:48"
  },
  {
    "version": 9,
    "ip_address": "205.149.118.138",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-09",
    "time": "2023-02-28T19:56:28.153ZT02:57:59"
  },
  {
    "version": 6,
    "ip_address": "205.61.224.180",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-10",
    "time": "2023-08-07T04:08:25.535ZT02:05:21"
  },
  {
    "version": 10,
    "ip_address": "120.236.156.21",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-17",
    "time": "2023-04-14T16:38:40.491ZT08:56:13"
  },
  {
    "version": 3,
    "ip_address": "117.119.28.213",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-11",
    "time": "2023-08-29T01:59:05.631ZT09:23:06"
  },
  {
    "version": 10,
    "ip_address": "20.210.211.67",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-21",
    "time": "2023-12-08T19:03:22.499ZT14:21:20"
  },
  {
    "version": 6,
    "ip_address": "191.130.110.186",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-09",
    "time": "2023-10-16T06:01:12.838ZT20:46:14"
  },
  {
    "version": 5,
    "ip_address": "89.182.255.87",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-18",
    "time": "2023-08-28T10:21:21.956ZT16:37:38"
  },
  {
    "version": 4,
    "ip_address": "139.29.153.43",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-23",
    "time": "2023-03-09T22:03:42.881ZT04:14:22"
  },
  {
    "version": 5,
    "ip_address": "166.1.22.241",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-18",
    "time": "2023-10-07T00:09:39.476ZT14:47:15"
  },
  {
    "version": 3,
    "ip_address": "165.133.6.45",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-13",
    "time": "2023-01-20T13:30:45.628ZT08:55:20"
  },
  {
    "version": 5,
    "ip_address": "147.7.195.112",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-14",
    "time": "2023-10-09T10:03:58.813ZT01:17:40"
  },
  {
    "version": 5,
    "ip_address": "10.98.209.105",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-22",
    "time": "2023-02-26T12:48:26.677ZT06:56:28"
  },
  {
    "version": 4,
    "ip_address": "43.55.65.196",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-04",
    "time": "2023-07-11T10:11:18.396ZT23:15:59"
  },
  {
    "version": 9,
    "ip_address": "152.246.47.221",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-28",
    "time": "2023-09-05T03:53:43.009ZT06:12:52"
  },
  {
    "version": 9,
    "ip_address": "17.97.189.7",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-30",
    "time": "2023-01-14T11:26:57.861ZT09:59:09"
  },
  {
    "version": 1,
    "ip_address": "41.116.66.188",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-06",
    "time": "2023-03-07T01:17:09.740ZT01:58:18"
  },
  {
    "version": 6,
    "ip_address": "238.149.25.69",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-02",
    "time": "2023-09-23T22:27:45.244ZT10:14:35"
  },
  {
    "version": 9,
    "ip_address": "249.206.94.26",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-21",
    "time": "2023-08-03T07:04:22.447ZT17:47:01"
  },
  {
    "version": 7,
    "ip_address": "165.18.126.157",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-06",
    "time": "2023-06-15T22:07:07.745ZT18:57:16"
  },
  {
    "version": 10,
    "ip_address": "88.104.109.179",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-22",
    "time": "2023-05-22T02:54:37.392ZT01:09:12"
  },
  {
    "version": 1,
    "ip_address": "23.116.45.7",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-13",
    "time": "2023-08-27T21:21:20.819ZT20:09:01"
  },
  {
    "version": 3,
    "ip_address": "136.129.56.192",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-15",
    "time": "2023-06-25T00:26:26.679ZT17:09:02"
  },
  {
    "version": 1,
    "ip_address": "126.23.142.113",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-28",
    "time": "2023-11-07T14:05:41.882ZT19:22:40"
  },
  {
    "version": 8,
    "ip_address": "92.224.102.73",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-06",
    "time": "2023-10-21T14:11:20.850ZT22:51:27"
  },
  {
    "version": 1,
    "ip_address": "117.0.37.49",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-04",
    "time": "2023-04-29T20:13:42.164ZT14:07:58"
  },
  {
    "version": 4,
    "ip_address": "92.129.75.203",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-05",
    "time": "2023-05-17T21:57:30.012ZT07:09:29"
  },
  {
    "version": 4,
    "ip_address": "192.88.136.128",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-08",
    "time": "2023-02-09T12:38:56.159ZT03:12:26"
  },
  {
    "version": 6,
    "ip_address": "142.90.193.47",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-01",
    "time": "2023-03-07T02:26:29.845ZT00:47:41"
  },
  {
    "version": 9,
    "ip_address": "5.9.14.17",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-15",
    "time": "2023-01-05T16:59:14.727ZT22:35:33"
  },
  {
    "version": 7,
    "ip_address": "74.201.178.36",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-23",
    "time": "2023-09-24T02:28:52.884ZT16:45:51"
  },
  {
    "version": 5,
    "ip_address": "166.38.118.61",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-11",
    "time": "2023-01-23T06:47:30.292ZT06:46:54"
  },
  {
    "version": 2,
    "ip_address": "191.154.204.159",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-26",
    "time": "2023-10-09T18:14:25.099ZT06:21:20"
  },
  {
    "version": 6,
    "ip_address": "174.101.239.148",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-01",
    "time": "2023-06-07T19:55:22.154ZT11:35:46"
  },
  {
    "version": 10,
    "ip_address": "15.172.162.130",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-11",
    "time": "2023-01-03T04:02:49.854ZT19:21:15"
  },
  {
    "version": 10,
    "ip_address": "83.29.77.244",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-25",
    "time": "2023-03-17T21:37:43.147ZT22:09:32"
  },
  {
    "version": 7,
    "ip_address": "219.238.52.184",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-12",
    "time": "2023-09-05T20:44:48.291ZT05:28:46"
  },
  {
    "version": 7,
    "ip_address": "130.50.130.81",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-02",
    "time": "2023-11-03T20:12:30.548ZT04:24:28"
  },
  {
    "version": 8,
    "ip_address": "105.28.58.100",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-23",
    "time": "2023-12-21T11:57:12.682ZT09:01:47"
  },
  {
    "version": 5,
    "ip_address": "100.213.55.154",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-05",
    "time": "2023-11-16T10:10:51.522ZT20:22:32"
  },
  {
    "version": 8,
    "ip_address": "49.88.220.254",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-25",
    "time": "2023-07-03T17:26:54.293ZT21:58:55"
  },
  {
    "version": 7,
    "ip_address": "29.94.81.191",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-15",
    "time": "2023-01-12T05:46:29.940ZT06:24:04"
  },
  {
    "version": 9,
    "ip_address": "84.240.213.218",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-08",
    "time": "2023-10-13T23:18:13.870ZT03:17:13"
  },
  {
    "version": 5,
    "ip_address": "205.186.46.27",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-06",
    "time": "2023-10-25T01:09:46.369ZT16:07:30"
  },
  {
    "version": 10,
    "ip_address": "153.50.195.206",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-24",
    "time": "2023-05-09T12:13:59.459ZT09:03:56"
  },
  {
    "version": 4,
    "ip_address": "63.152.31.94",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-09",
    "time": "2023-08-21T00:27:41.177ZT07:05:14"
  },
  {
    "version": 1,
    "ip_address": "109.86.183.123",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-07",
    "time": "2023-03-29T02:48:41.736ZT16:26:12"
  },
  {
    "version": 2,
    "ip_address": "239.58.106.162",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-02",
    "time": "2023-02-13T05:19:58.713ZT06:40:57"
  },
  {
    "version": 3,
    "ip_address": "225.122.232.152",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-05",
    "time": "2023-08-20T16:09:18.055ZT06:13:24"
  },
  {
    "version": 10,
    "ip_address": "24.50.224.106",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-24",
    "time": "2023-08-15T16:40:41.801ZT18:40:29"
  },
  {
    "version": 2,
    "ip_address": "11.199.17.74",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-26",
    "time": "2023-04-30T00:51:38.876ZT09:59:18"
  },
  {
    "version": 9,
    "ip_address": "253.189.106.186",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-19",
    "time": "2023-06-02T20:47:32.278ZT01:28:21"
  },
  {
    "version": 3,
    "ip_address": "229.218.17.196",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-03",
    "time": "2023-02-05T05:00:59.321ZT06:00:44"
  },
  {
    "version": 9,
    "ip_address": "45.191.141.197",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-02",
    "time": "2023-05-09T18:05:49.094ZT03:10:25"
  },
  {
    "version": 1,
    "ip_address": "179.243.114.236",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-27",
    "time": "2023-08-29T18:02:59.855ZT01:32:09"
  },
  {
    "version": 4,
    "ip_address": "20.197.10.12",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-26",
    "time": "2023-10-26T23:24:25.666ZT18:47:07"
  },
  {
    "version": 3,
    "ip_address": "68.61.236.198",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-30",
    "time": "2023-12-08T11:48:56.498ZT06:21:57"
  },
  {
    "version": 8,
    "ip_address": "84.191.55.240",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-02",
    "time": "2023-08-09T22:12:42.915ZT00:49:24"
  },
  {
    "version": 6,
    "ip_address": "209.20.236.149",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-12",
    "time": "2023-09-03T13:28:07.145ZT23:42:40"
  },
  {
    "version": 5,
    "ip_address": "23.114.117.12",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-19",
    "time": "2023-06-02T00:41:44.148ZT18:56:46"
  },
  {
    "version": 10,
    "ip_address": "78.57.33.34",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-19",
    "time": "2023-02-18T07:22:32.257ZT17:58:40"
  },
  {
    "version": 5,
    "ip_address": "171.87.241.104",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-23",
    "time": "2023-03-12T23:31:49.805ZT09:58:17"
  },
  {
    "version": 9,
    "ip_address": "221.229.101.25",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-06",
    "time": "2023-06-05T02:36:45.884ZT11:06:45"
  },
  {
    "version": 7,
    "ip_address": "180.63.178.84",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-24",
    "time": "2023-07-21T20:44:05.924ZT08:19:40"
  },
  {
    "version": 7,
    "ip_address": "224.171.250.199",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-09",
    "time": "2023-01-10T12:19:10.616ZT22:15:13"
  },
  {
    "version": 7,
    "ip_address": "71.134.30.246",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-28",
    "time": "2023-07-10T17:51:12.092ZT19:04:44"
  },
  {
    "version": 3,
    "ip_address": "149.158.161.10",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-24",
    "time": "2023-02-06T05:38:51.949ZT22:55:39"
  },
  {
    "version": 7,
    "ip_address": "11.183.48.98",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-17",
    "time": "2023-03-31T23:25:11.925ZT05:01:16"
  },
  {
    "version": 10,
    "ip_address": "134.237.14.48",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-13",
    "time": "2023-01-09T19:22:11.020ZT12:54:06"
  },
  {
    "version": 5,
    "ip_address": "224.198.243.26",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-05",
    "time": "2023-12-07T05:38:04.403ZT09:23:21"
  },
  {
    "version": 9,
    "ip_address": "118.144.151.246",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-09",
    "time": "2023-07-23T09:41:07.957ZT02:20:15"
  },
  {
    "version": 3,
    "ip_address": "116.1.225.23",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-05",
    "time": "2023-02-27T12:01:02.561ZT13:34:58"
  },
  {
    "version": 3,
    "ip_address": "73.157.113.223",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-04",
    "time": "2023-04-30T06:09:54.240ZT18:50:19"
  },
  {
    "version": 1,
    "ip_address": "247.156.155.255",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-27",
    "time": "2023-08-28T13:38:28.174ZT11:54:01"
  },
  {
    "version": 4,
    "ip_address": "196.5.47.14",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-20",
    "time": "2023-07-21T23:33:11.535ZT16:49:15"
  },
  {
    "version": 5,
    "ip_address": "69.27.173.65",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-14",
    "time": "2023-05-25T20:21:28.513ZT15:54:58"
  },
  {
    "version": 7,
    "ip_address": "177.208.241.201",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-17",
    "time": "2023-02-16T21:22:26.142ZT13:47:55"
  },
  {
    "version": 5,
    "ip_address": "235.22.100.219",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-14",
    "time": "2023-10-23T23:47:52.633ZT07:29:55"
  },
  {
    "version": 10,
    "ip_address": "56.138.2.134",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-02",
    "time": "2023-05-25T20:14:34.323ZT21:12:02"
  },
  {
    "version": 1,
    "ip_address": "60.156.95.13",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-06",
    "time": "2023-06-14T19:56:25.846ZT20:23:28"
  },
  {
    "version": 4,
    "ip_address": "67.63.181.183",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-15",
    "time": "2023-02-05T15:07:31.131ZT07:16:32"
  },
  {
    "version": 5,
    "ip_address": "122.254.227.138",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-05",
    "time": "2023-10-11T19:47:19.637ZT04:05:41"
  },
  {
    "version": 5,
    "ip_address": "215.203.50.53",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-11",
    "time": "2023-05-01T13:10:10.570ZT21:28:58"
  },
  {
    "version": 10,
    "ip_address": "104.146.67.244",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-07",
    "time": "2023-01-10T13:41:10.283ZT00:39:55"
  },
  {
    "version": 10,
    "ip_address": "97.160.191.135",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-05",
    "time": "2023-03-22T14:39:01.133ZT04:55:02"
  },
  {
    "version": 2,
    "ip_address": "46.126.185.176",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-20",
    "time": "2023-05-14T04:33:30.939ZT02:16:11"
  },
  {
    "version": 7,
    "ip_address": "219.43.105.14",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-11",
    "time": "2023-04-05T15:56:35.310ZT03:47:18"
  },
  {
    "version": 9,
    "ip_address": "244.126.173.165",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-11",
    "time": "2023-12-23T17:51:05.290ZT18:13:28"
  },
  {
    "version": 3,
    "ip_address": "81.58.206.80",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-27",
    "time": "2023-09-16T23:30:36.882ZT22:51:13"
  },
  {
    "version": 2,
    "ip_address": "77.32.40.74",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-10",
    "time": "2023-07-03T03:06:50.982ZT03:28:09"
  },
  {
    "version": 4,
    "ip_address": "41.250.116.3",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-03",
    "time": "2023-08-26T04:42:55.578ZT23:56:26"
  },
  {
    "version": 4,
    "ip_address": "125.13.28.172",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-09",
    "time": "2023-08-11T00:12:52.804ZT00:23:34"
  },
  {
    "version": 5,
    "ip_address": "64.163.44.187",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-24",
    "time": "2023-04-28T03:03:32.717ZT21:08:01"
  },
  {
    "version": 4,
    "ip_address": "162.217.180.162",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-05",
    "time": "2023-11-27T16:13:14.785ZT12:18:31"
  },
  {
    "version": 6,
    "ip_address": "79.243.248.15",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-26",
    "time": "2023-05-15T13:46:36.893ZT00:27:50"
  },
  {
    "version": 9,
    "ip_address": "228.84.32.209",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-12",
    "time": "2023-03-13T19:36:20.761ZT06:23:57"
  },
  {
    "version": 3,
    "ip_address": "55.249.93.54",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-09",
    "time": "2023-11-02T18:37:32.698ZT08:07:39"
  },
  {
    "version": 7,
    "ip_address": "134.225.121.156",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-13",
    "time": "2023-02-15T08:02:46.333ZT15:52:41"
  },
  {
    "version": 1,
    "ip_address": "141.42.210.194",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-20",
    "time": "2023-12-05T14:19:19.164ZT13:10:28"
  },
  {
    "version": 1,
    "ip_address": "151.92.195.225",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-12",
    "time": "2023-04-16T23:10:59.580ZT20:37:26"
  },
  {
    "version": 5,
    "ip_address": "244.30.106.8",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-23",
    "time": "2023-07-23T03:00:16.936ZT03:09:23"
  },
  {
    "version": 1,
    "ip_address": "195.184.73.208",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-03",
    "time": "2023-12-16T18:32:29.769ZT05:52:54"
  },
  {
    "version": 5,
    "ip_address": "111.193.89.79",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-25",
    "time": "2023-10-31T06:59:56.982ZT08:23:04"
  },
  {
    "version": 2,
    "ip_address": "169.15.54.246",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-21",
    "time": "2023-09-15T10:03:04.620ZT08:37:38"
  },
  {
    "version": 1,
    "ip_address": "63.85.175.98",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-14",
    "time": "2023-06-02T23:52:42.467ZT09:35:06"
  },
  {
    "version": 10,
    "ip_address": "78.92.244.79",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-17",
    "time": "2023-04-08T09:12:30.968ZT23:13:48"
  },
  {
    "version": 2,
    "ip_address": "74.101.149.167",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-27",
    "time": "2023-05-05T19:15:20.799ZT10:23:27"
  },
  {
    "version": 4,
    "ip_address": "157.154.202.98",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-02",
    "time": "2023-08-03T06:19:04.958ZT10:07:37"
  },
  {
    "version": 5,
    "ip_address": "11.91.101.10",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-16",
    "time": "2023-05-06T13:14:28.582ZT23:10:48"
  },
  {
    "version": 7,
    "ip_address": "13.250.7.175",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-17",
    "time": "2023-06-29T10:39:45.749ZT03:40:20"
  },
  {
    "version": 6,
    "ip_address": "65.59.193.195",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-01",
    "time": "2023-01-16T00:19:27.889ZT07:49:07"
  },
  {
    "version": 7,
    "ip_address": "163.181.208.108",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-05",
    "time": "2023-11-02T20:15:09.680ZT18:18:51"
  },
  {
    "version": 10,
    "ip_address": "114.111.78.49",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-14",
    "time": "2023-05-13T07:04:45.082ZT00:51:56"
  },
  {
    "version": 1,
    "ip_address": "105.83.66.143",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-06",
    "time": "2023-10-31T16:19:20.087ZT19:12:05"
  },
  {
    "version": 8,
    "ip_address": "235.181.151.175",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-27",
    "time": "2023-11-05T01:44:27.126ZT04:33:59"
  },
  {
    "version": 2,
    "ip_address": "63.141.188.152",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-21",
    "time": "2023-09-03T09:36:44.633ZT20:03:17"
  },
  {
    "version": 5,
    "ip_address": "141.61.217.232",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-03",
    "time": "2023-09-21T20:44:30.616ZT03:21:02"
  },
  {
    "version": 6,
    "ip_address": "195.43.239.1",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-17",
    "time": "2023-11-28T09:16:09.668ZT07:10:21"
  },
  {
    "version": 6,
    "ip_address": "198.35.122.230",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-20",
    "time": "2023-07-07T12:19:32.650ZT02:28:03"
  },
  {
    "version": 10,
    "ip_address": "151.80.111.21",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-14",
    "time": "2023-11-30T17:09:42.461ZT19:26:32"
  },
  {
    "version": 4,
    "ip_address": "43.209.184.164",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-22",
    "time": "2023-08-01T18:01:56.935ZT07:45:03"
  },
  {
    "version": 3,
    "ip_address": "128.1.111.244",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-21",
    "time": "2023-07-08T15:02:31.274ZT15:46:09"
  },
  {
    "version": 1,
    "ip_address": "69.13.242.106",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-13",
    "time": "2023-05-20T17:27:04.970ZT13:32:39"
  },
  {
    "version": 3,
    "ip_address": "19.210.45.196",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-05",
    "time": "2023-08-18T08:15:59.172ZT07:48:19"
  },
  {
    "version": 6,
    "ip_address": "47.171.67.88",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-30",
    "time": "2023-05-05T23:41:10.766ZT22:39:34"
  },
  {
    "version": 1,
    "ip_address": "226.129.203.92",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-21",
    "time": "2023-10-11T05:52:11.711ZT21:00:11"
  },
  {
    "version": 5,
    "ip_address": "96.132.233.77",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-24",
    "time": "2023-09-16T15:00:22.022ZT08:43:54"
  },
  {
    "version": 5,
    "ip_address": "32.156.171.110",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-02",
    "time": "2023-10-18T20:23:58.543ZT13:20:55"
  },
  {
    "version": 10,
    "ip_address": "17.108.167.183",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-27",
    "time": "2023-09-07T21:32:16.442ZT12:10:13"
  },
  {
    "version": 1,
    "ip_address": "102.250.140.177",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-02",
    "time": "2023-01-10T04:58:11.097ZT14:32:03"
  },
  {
    "version": 4,
    "ip_address": "83.83.255.74",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-15",
    "time": "2023-05-09T02:06:45.388ZT09:19:38"
  },
  {
    "version": 9,
    "ip_address": "212.70.236.158",
    "time_zone": -10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-11",
    "time": "2023-10-11T07:43:38.541ZT00:30:19"
  },
  {
    "version": 5,
    "ip_address": "235.102.104.238",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-04",
    "time": "2023-04-15T11:15:08.474ZT16:54:36"
  },
  {
    "version": 1,
    "ip_address": "157.89.231.175",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-12",
    "time": "2023-08-12T07:58:33.321ZT18:33:08"
  },
  {
    "version": 10,
    "ip_address": "74.173.147.83",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-19",
    "time": "2023-03-18T01:24:41.960ZT16:31:27"
  },
  {
    "version": 6,
    "ip_address": "216.24.221.135",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-11",
    "time": "2023-01-24T19:51:33.197ZT19:12:10"
  },
  {
    "version": 6,
    "ip_address": "65.234.248.204",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-12",
    "time": "2023-09-25T00:42:17.869ZT12:55:09"
  },
  {
    "version": 7,
    "ip_address": "70.30.33.109",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-21",
    "time": "2023-09-23T18:22:55.782ZT15:58:25"
  },
  {
    "version": 10,
    "ip_address": "4.138.50.119",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-07",
    "time": "2023-05-28T04:52:05.570ZT02:02:12"
  },
  {
    "version": 1,
    "ip_address": "164.167.177.81",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-01",
    "time": "2023-10-05T07:15:54.746ZT02:04:16"
  },
  {
    "version": 9,
    "ip_address": "130.32.41.49",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-06",
    "time": "2023-09-11T12:31:55.898ZT10:32:50"
  },
  {
    "version": 8,
    "ip_address": "72.242.139.246",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-21",
    "time": "2023-02-14T08:09:18.651ZT02:24:34"
  },
  {
    "version": 6,
    "ip_address": "122.205.103.250",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-09",
    "time": "2023-06-09T11:24:07.474ZT22:51:43"
  },
  {
    "version": 7,
    "ip_address": "249.220.130.238",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-27",
    "time": "2023-09-24T17:50:08.589ZT19:00:53"
  },
  {
    "version": 8,
    "ip_address": "28.232.122.147",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-22",
    "time": "2023-01-09T06:01:17.947ZT17:18:50"
  },
  {
    "version": 5,
    "ip_address": "32.125.154.130",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-08",
    "time": "2023-07-16T13:31:34.634ZT13:27:08"
  },
  {
    "version": 8,
    "ip_address": "210.191.65.114",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-25",
    "time": "2023-09-21T02:56:41.905ZT13:50:37"
  },
  {
    "version": 1,
    "ip_address": "93.139.74.218",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-02",
    "time": "2023-09-20T07:11:40.955ZT05:38:59"
  },
  {
    "version": 9,
    "ip_address": "209.207.18.168",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-04",
    "time": "2023-06-26T22:51:42.945ZT08:39:52"
  },
  {
    "version": 2,
    "ip_address": "208.253.235.146",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-04",
    "time": "2023-11-16T08:39:30.419ZT20:30:16"
  },
  {
    "version": 10,
    "ip_address": "83.242.121.151",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-29",
    "time": "2023-05-22T19:20:31.677ZT23:55:20"
  },
  {
    "version": 3,
    "ip_address": "97.36.161.138",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-24",
    "time": "2023-10-29T14:16:01.460ZT05:29:29"
  },
  {
    "version": 6,
    "ip_address": "206.36.64.25",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-23",
    "time": "2023-04-03T07:05:07.848ZT11:36:22"
  },
  {
    "version": 2,
    "ip_address": "72.181.182.29",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-07",
    "time": "2023-06-26T15:36:43.328ZT10:43:25"
  },
  {
    "version": 10,
    "ip_address": "106.184.2.60",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-17",
    "time": "2023-04-05T14:21:44.597ZT20:12:00"
  },
  {
    "version": 5,
    "ip_address": "201.116.97.226",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-19",
    "time": "2023-06-07T20:36:33.117ZT10:02:26"
  },
  {
    "version": 6,
    "ip_address": "85.242.188.53",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-31",
    "time": "2023-10-26T04:18:04.070ZT17:14:19"
  },
  {
    "version": 3,
    "ip_address": "30.10.175.89",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-20",
    "time": "2023-07-25T21:34:21.971ZT09:55:57"
  },
  {
    "version": 4,
    "ip_address": "83.215.198.231",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-25",
    "time": "2023-07-25T06:50:41.144ZT22:08:46"
  },
  {
    "version": 5,
    "ip_address": "174.243.79.129",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-29",
    "time": "2023-12-19T19:54:59.630ZT08:01:17"
  },
  {
    "version": 2,
    "ip_address": "192.142.105.147",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-02",
    "time": "2023-10-03T09:57:24.289ZT20:07:23"
  },
  {
    "version": 7,
    "ip_address": "212.27.229.105",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-23",
    "time": "2023-03-17T09:43:57.624ZT18:14:06"
  },
  {
    "version": 5,
    "ip_address": "50.1.67.166",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-18",
    "time": "2023-09-09T02:28:02.348ZT16:31:11"
  },
  {
    "version": 2,
    "ip_address": "127.118.4.38",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-30",
    "time": "2023-08-16T09:51:11.924ZT15:18:39"
  },
  {
    "version": 9,
    "ip_address": "200.13.203.167",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-27",
    "time": "2023-05-28T05:48:41.170ZT06:49:54"
  },
  {
    "version": 10,
    "ip_address": "4.130.129.177",
    "time_zone": -1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-23",
    "time": "2023-07-10T19:42:25.445ZT17:23:05"
  },
  {
    "version": 5,
    "ip_address": "57.176.217.151",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-24",
    "time": "2023-06-08T22:33:21.337ZT02:19:56"
  },
  {
    "version": 6,
    "ip_address": "154.127.129.234",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-29",
    "time": "2023-01-13T02:57:43.083ZT06:52:43"
  },
  {
    "version": 5,
    "ip_address": "220.1.51.45",
    "time_zone": -7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-07",
    "time": "2023-10-15T16:54:02.573ZT04:57:08"
  },
  {
    "version": 4,
    "ip_address": "204.114.191.98",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-05",
    "time": "2023-08-07T09:20:31.825ZT21:37:19"
  },
  {
    "version": 7,
    "ip_address": "175.187.183.82",
    "time_zone": -2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-29",
    "time": "2023-02-22T06:48:48.873ZT19:38:29"
  },
  {
    "version": 3,
    "ip_address": "166.154.229.175",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-02-18",
    "time": "2023-07-13T06:18:21.542ZT11:29:52"
  },
  {
    "version": 10,
    "ip_address": "167.99.158.24",
    "time_zone": -12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-07-09",
    "time": "2023-08-08T19:36:33.443ZT15:55:50"
  },
  {
    "version": 6,
    "ip_address": "5.211.133.193",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-21",
    "time": "2023-11-23T02:14:07.688ZT14:41:23"
  },
  {
    "version": 7,
    "ip_address": "156.5.69.91",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-05-25",
    "time": "2023-02-06T10:09:48.274ZT13:04:08"
  },
  {
    "version": 8,
    "ip_address": "196.236.215.32",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-23",
    "time": "2023-02-10T05:21:43.753ZT19:38:28"
  },
  {
    "version": 4,
    "ip_address": "159.4.108.203",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-30",
    "time": "2023-12-17T05:34:15.222ZT19:59:18"
  },
  {
    "version": 1,
    "ip_address": "229.52.118.209",
    "time_zone": -8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-30",
    "time": "2023-03-18T10:30:16.807ZT13:32:19"
  },
  {
    "version": 6,
    "ip_address": "108.9.239.218",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-25",
    "time": "2023-05-29T03:16:58.225ZT07:10:52"
  },
  {
    "version": 5,
    "ip_address": "140.117.25.65",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-05",
    "time": "2023-05-11T15:18:37.373ZT01:14:17"
  },
  {
    "version": 5,
    "ip_address": "205.90.150.23",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-06",
    "time": "2023-04-12T08:56:30.941ZT04:22:32"
  },
  {
    "version": 8,
    "ip_address": "251.27.45.58",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-27",
    "time": "2023-05-23T07:31:26.640ZT01:42:00"
  },
  {
    "version": 7,
    "ip_address": "91.132.31.8",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-26",
    "time": "2023-05-18T11:10:34.518ZT05:09:05"
  },
  {
    "version": 1,
    "ip_address": "241.116.61.68",
    "time_zone": -5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-22",
    "time": "2023-06-05T13:50:13.763ZT01:28:27"
  },
  {
    "version": 10,
    "ip_address": "246.101.112.248",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-08-02",
    "time": "2023-05-22T06:14:48.303ZT04:10:04"
  },
  {
    "version": 10,
    "ip_address": "119.77.4.110",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-19",
    "time": "2023-04-22T08:57:58.666ZT10:13:08"
  },
  {
    "version": 6,
    "ip_address": "254.224.167.84",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-20",
    "time": "2023-10-29T23:06:31.719ZT08:05:28"
  },
  {
    "version": 9,
    "ip_address": "212.241.11.168",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-04",
    "time": "2023-09-07T13:43:16.041ZT16:11:20"
  },
  {
    "version": 8,
    "ip_address": "97.168.137.167",
    "time_zone": -3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-03-18",
    "time": "2023-11-22T02:14:44.412ZT08:48:57"
  },
  {
    "version": 8,
    "ip_address": "37.24.188.86",
    "time_zone": -11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-08",
    "time": "2023-11-27T04:06:28.679ZT00:33:54"
  },
  {
    "version": 10,
    "ip_address": "205.152.191.40",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-27",
    "time": "2023-07-28T16:55:22.862ZT16:37:53"
  },
  {
    "version": 8,
    "ip_address": "145.122.108.144",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-09",
    "time": "2023-02-02T03:30:19.301ZT22:04:47"
  },
  {
    "version": 2,
    "ip_address": "235.41.219.97",
    "time_zone": -6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-04-23",
    "time": "2023-01-29T13:29:38.564ZT01:43:14"
  },
  {
    "version": 10,
    "ip_address": "2.9.90.93",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-11-26",
    "time": "2023-01-30T13:53:33.102ZT04:05:15"
  },
  {
    "version": 1,
    "ip_address": "76.144.101.221",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-09-30",
    "time": "2023-12-28T09:56:43.747ZT16:55:29"
  },
  {
    "version": 5,
    "ip_address": "187.52.23.33",
    "time_zone": -4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-06-18",
    "time": "2023-07-12T06:17:47.833ZT17:15:31"
  },
  {
    "version": 5,
    "ip_address": "164.128.216.232",
    "time_zone": -9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-01-31",
    "time": "2023-02-01T10:34:44.329ZT03:50:42"
  },
  {
    "version": 9,
    "ip_address": "56.224.180.217",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-10-13",
    "time": "2023-09-26T11:40:10.663ZT18:00:42"
  }
]

        for dummy_heartbeat in dummy_heartbeat_list:
            # Randomly select a camera from the available cameras
            random_camera = random.choice(all_cameras)

            # Use the selected camera's data for the dummy heartbeat data
            dummy_heartbeat["sn"] = random_camera.sn

            # Create a CameraHeartbeat instance
            heartbeat_serializer = CreateHeartbeatSerializer(data=dummy_heartbeat)
            heartbeat_serializer.is_valid(raise_exception=True)
            heartbeat_serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted dummy heartbeat data to the database'))
