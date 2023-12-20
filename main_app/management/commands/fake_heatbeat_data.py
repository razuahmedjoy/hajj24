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
    "ip_address": "105.119.127.131",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "132.104.224.60",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "178.174.172.35",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "45.239.97.48",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "47.201.91.42",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "64.113.94.6",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "76.114.179.91",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "73.71.21.152",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "206.16.174.132",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "157.127.190.249",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "243.207.253.43",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "29.246.188.249",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "41.195.117.49",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "223.137.7.18",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "172.13.81.65",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "47.94.92.130",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "228.182.41.209",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "54.129.129.240",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "94.31.47.12",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "244.79.255.56",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "149.167.170.247",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "165.112.140.133",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "173.52.137.239",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "186.108.123.169",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "162.103.230.175",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "242.114.195.109",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "132.89.114.29",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "101.117.248.27",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "93.176.243.119",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "249.121.68.88",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "29.233.61.243",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "69.158.41.30",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "58.113.228.148",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "195.32.162.143",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "72.170.147.251",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "242.4.202.74",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "128.83.37.50",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "56.232.50.34",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "166.92.14.204",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "36.28.217.180",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "74.124.229.115",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "173.204.244.99",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "108.220.168.152",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "71.152.9.97",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "171.179.245.243",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "34.117.71.191",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "49.240.50.184",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "8.191.98.214",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "20.231.104.218",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "229.206.169.101",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "84.199.181.60",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "146.31.112.12",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "134.68.1.13",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "235.79.113.96",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "38.124.139.21",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "200.222.255.204",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "214.169.172.188",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "137.106.19.201",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "50.231.44.47",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "119.195.13.10",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "25.24.64.54",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "126.46.184.115",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "60.243.234.15",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "56.10.64.188",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "177.162.2.14",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "21.102.237.75",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "38.38.38.101",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "229.154.13.130",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "139.61.51.78",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "140.144.5.104",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "102.0.86.33",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "208.33.179.14",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "42.130.251.92",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "0.167.233.188",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "134.114.217.139",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "219.201.247.165",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "105.99.103.106",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "55.18.34.140",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "109.105.176.237",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "207.159.154.67",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "33.6.97.167",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "42.235.182.71",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "231.226.171.45",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "173.206.167.46",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "229.183.255.162",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "23.243.254.72",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "254.208.34.117",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "165.125.8.92",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "21.197.181.198",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "141.113.213.144",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "195.41.47.159",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "55.141.49.32",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "41.24.242.11",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "45.65.192.164",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "235.221.192.232",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "53.5.227.174",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "62.226.187.131",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "92.183.196.219",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "82.157.112.43",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "204.191.6.255",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "177.168.162.63",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "47.167.27.112",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "174.137.93.243",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "176.72.121.9",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "60.234.78.229",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "44.110.152.172",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "119.91.39.216",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "120.77.72.251",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "138.108.89.177",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "16.159.146.87",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "155.182.113.177",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "124.121.89.216",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "230.134.147.253",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "170.22.113.28",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "189.31.122.185",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "85.61.236.105",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "111.191.196.36",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "214.64.81.146",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "60.112.16.78",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "52.81.39.65",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "110.16.124.112",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "182.135.178.230",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "133.22.226.223",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "52.42.249.79",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "204.89.18.246",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "219.200.218.211",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "70.55.30.51",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "56.156.170.4",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "23.107.36.168",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "233.75.66.130",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "67.102.21.49",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "44.124.161.80",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "75.161.247.185",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "33.20.216.28",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "34.167.210.248",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "153.162.56.157",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "136.4.245.195",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "211.234.13.172",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "64.110.76.201",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "135.52.37.12",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "55.244.223.154",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "52.117.158.200",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "80.150.123.188",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "165.249.108.25",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "170.178.206.41",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "216.63.184.45",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "160.231.66.216",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "14.153.209.209",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "78.170.69.4",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "52.144.213.58",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "202.30.50.74",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "210.237.107.244",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "120.221.74.45",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "37.135.99.31",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "173.49.255.164",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "157.93.7.222",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "20.52.2.160",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "61.7.29.75",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "128.70.15.201",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "69.147.129.2",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "4.54.18.100",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "216.207.80.212",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "249.9.80.117",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "97.43.153.233",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "64.117.37.255",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "248.197.178.63",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "177.27.74.181",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "246.98.120.41",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "216.27.158.41",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "234.63.119.224",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "43.44.242.143",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "52.98.194.227",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "235.106.242.6",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "240.182.32.181",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "169.203.186.88",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "67.39.116.76",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "229.220.200.99",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "19.220.246.223",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "175.24.60.228",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "243.61.85.207",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "215.75.45.241",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "56.69.97.148",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "31.194.134.113",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "107.14.9.182",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "228.23.157.32",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "6.166.179.93",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "206.216.6.162",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "61.21.28.195",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "209.165.243.98",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "117.151.101.157",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "242.89.188.192",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "241.83.27.191",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "138.216.101.191",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "211.243.75.1",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "16.128.211.55",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "20.167.143.89",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "89.247.126.217",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "233.164.158.164",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "178.154.95.80",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "248.42.138.99",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "77.71.87.89",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "145.52.63.22",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "97.10.153.43",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "132.106.13.74",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "255.234.58.255",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "18.179.247.55",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "81.6.9.253",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "112.232.27.30",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "221.17.14.224",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "1.217.43.79",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "100.16.197.109",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "47.95.198.48",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "71.227.245.39",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "162.52.241.171",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "169.19.76.122",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "187.55.209.111",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "110.237.165.95",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "116.18.174.137",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "136.35.53.211",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "75.183.237.191",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "236.78.8.44",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "3.34.100.43",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "150.219.46.22",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "132.218.208.242",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "183.234.183.182",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "193.212.83.46",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "109.65.226.124",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "111.179.131.210",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "99.130.130.234",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "239.251.187.80",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "129.157.132.133",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "181.17.155.49",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "145.44.113.69",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "252.140.87.169",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "91.227.148.127",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "179.53.142.76",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "14.238.89.241",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "101.146.82.159",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "131.129.69.122",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "35.177.64.53",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "127.62.26.151",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "74.220.90.85",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "171.210.75.205",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "18.162.99.236",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "135.229.23.57",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "133.124.158.13",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "91.157.110.44",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "29.195.195.46",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "25.72.17.80",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "179.207.246.117",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "203.183.85.246",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "198.239.76.206",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "230.60.176.5",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "162.73.144.193",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "58.88.17.3",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "225.170.110.85",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "247.61.112.98",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "130.80.5.85",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "45.152.229.208",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "156.138.47.224",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "103.9.42.55",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "89.140.11.222",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "217.203.128.93",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "207.252.238.194",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "10.130.100.42",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "161.50.157.106",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "164.161.180.100",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "179.114.105.78",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "197.162.115.176",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "73.193.92.241",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "223.43.0.116",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "198.138.191.9",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "39.118.174.188",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "88.140.171.144",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "202.227.133.59",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "38.148.254.87",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "138.176.12.134",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "148.220.14.231",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "144.107.70.72",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "206.235.125.67",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "176.194.234.71",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "112.33.14.62",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "15.231.189.138",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "49.224.131.153",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "111.197.158.233",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "11.106.31.68",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "138.136.181.75",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "21.163.108.199",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "231.16.80.5",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "241.208.67.55",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "96.223.26.229",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "169.204.149.207",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "162.135.152.75",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "205.219.108.76",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "12.37.151.129",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "33.171.161.66",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "250.90.44.85",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "156.72.49.168",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "172.72.1.122",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "2.219.133.88",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "224.162.115.253",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "60.106.95.240",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "148.159.107.164",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "11.252.4.74",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "202.253.59.64",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "91.235.188.255",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "70.53.194.147",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "125.244.117.130",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "72.54.206.67",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "43.9.126.207",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "148.98.31.112",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "246.54.2.164",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "179.47.43.212",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "22.129.236.132",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "116.200.123.158",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "133.195.179.72",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "225.221.31.205",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "233.172.243.159",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "243.25.23.116",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "215.165.236.180",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "50.114.237.16",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "134.189.125.2",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "177.112.49.158",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "82.88.199.111",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "37.241.97.91",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "77.22.110.248",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "82.99.144.77",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "184.6.62.50",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "246.229.108.69",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "120.146.214.106",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "207.243.252.162",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "15.82.84.225",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "64.4.246.111",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "122.207.82.224",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "155.244.35.2",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "87.50.254.204",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "71.188.191.80",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "172.39.30.149",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "138.124.113.218",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "167.232.171.110",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "175.44.89.32",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "231.68.63.225",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "162.38.61.158",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "166.53.107.174",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "189.118.158.254",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "94.48.248.111",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "188.35.207.36",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "160.213.144.195",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "25.157.128.154",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "142.203.233.54",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "42.11.239.48",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "172.194.153.61",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "253.253.236.22",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "10.15.25.231",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "88.191.115.190",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "86.196.108.12",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "243.151.153.148",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "182.5.93.180",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "26.146.126.192",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "238.82.88.65",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "217.169.127.17",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "75.39.163.218",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "162.148.169.118",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "187.67.245.46",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "34.31.179.16",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "222.116.239.127",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "50.107.193.188",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "180.29.98.173",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "194.32.155.203",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "196.235.5.179",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "76.99.134.245",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "105.57.96.113",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "220.253.140.71",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "9.135.38.140",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "99.205.143.78",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "56.163.215.40",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "95.77.173.186",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "158.177.30.116",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "249.71.205.177",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "241.155.251.248",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "229.18.114.107",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "58.164.184.132",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "123.24.190.236",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "109.168.233.22",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "159.87.103.158",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "104.226.21.108",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "184.21.252.210",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "52.101.21.204",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "209.233.88.30",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "133.88.99.101",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "31.106.12.82",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "137.166.56.26",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "200.53.185.146",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "128.221.143.199",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-15T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "207.72.80.146",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "163.124.9.166",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "147.123.21.239",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "21.8.98.188",
    "time_zone": 18,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "90.247.99.64",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "184.37.197.234",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "84.158.163.77",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "96.219.123.31",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "139.49.166.46",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "242.157.187.74",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "124.2.105.246",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "178.98.62.209",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "221.193.83.141",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "204.200.58.8",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "85.72.8.114",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "142.246.217.237",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "96.178.68.122",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-03T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "14.142.121.22",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "226.137.174.210",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "109.42.124.163",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "238.15.195.85",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "120.98.118.23",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "136.116.227.12",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "93.30.84.191",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "154.213.145.229",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "209.155.214.193",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "61.2.191.43",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "242.143.154.50",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "157.38.54.210",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "197.175.18.195",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "117.115.11.143",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-07T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "184.49.123.225",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "59.69.10.221",
    "time_zone": 12,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "7.247.63.187",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "104.168.2.186",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "88.95.11.80",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "217.133.238.3",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "51.188.113.128",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "121.156.183.138",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "188.253.177.67",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "97.135.252.181",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "246.141.146.197",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "127.46.22.0",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "112.189.116.44",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "60.129.221.153",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "42.177.74.20",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "129.122.31.178",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-22T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "183.139.97.49",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "35.133.249.29",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "221.26.182.217",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "154.222.25.224",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "241.144.62.14",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "137.124.138.172",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "153.252.60.124",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "167.101.159.202",
    "time_zone": 6,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "33.13.96.161",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-25T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "12.97.58.207",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "105.188.108.45",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-08T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "237.179.128.244",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "200.101.93.91",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "230.131.50.157",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-29T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "40.42.75.198",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "13.26.168.5",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "185.172.193.222",
    "time_zone": 23,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-26T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "220.229.198.136",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "215.159.5.198",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-19T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "190.186.241.91",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-12T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "108.2.239.148",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "228.139.157.75",
    "time_zone": 10,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-13T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "84.170.50.250",
    "time_zone": 22,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "110.170.119.92",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-18T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "53.162.26.218",
    "time_zone": 13,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "156.9.26.32",
    "time_zone": 3,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-16T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "209.101.31.103",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "82.173.229.34",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-14T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "185.222.160.221",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "246.107.227.177",
    "time_zone": 15,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "156.77.146.197",
    "time_zone": 4,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-01T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "28.210.65.234",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-17T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "219.190.58.39",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-06-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "182.204.169.227",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "98.36.151.169",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "81.90.156.100",
    "time_zone": 20,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "254.197.176.238",
    "time_zone": 9,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-04-24T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "232.36.68.87",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-05T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "192.82.179.134",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-02T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "193.134.28.47",
    "time_zone": 1,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-05-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "216.181.202.63",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "190.140.105.182",
    "time_zone": 7,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "0.207.81.136",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-27T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "147.32.71.242",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-11-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "167.54.113.112",
    "time_zone": 16,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "135.71.67.125",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-21T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "69.34.184.65",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2022-12-30T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "43.77.119.9",
    "time_zone": 8,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-09T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "143.191.67.247",
    "time_zone": 19,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-31T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "61.215.198.47",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-02-20T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "215.181.142.25",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-01-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "242.88.52.228",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-11T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "34.173.42.151",
    "time_zone": 5,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-10-23T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "82.15.191.113",
    "time_zone": 0,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-12-04T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "7.192.78.177",
    "time_zone": 14,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-28T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "139.47.73.238",
    "time_zone": 2,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-07-10T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "211.63.114.187",
    "time_zone": 17,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-03-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "122.17.51.160",
    "time_zone": 11,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-08-06T13:18:48"
  },
  {
    "version": 1,
    "ip_address": "172.25.90.201",
    "time_zone": 21,
    "hw_platform": "platform_xyz",
    "reportDate": "2023-12-20",
    "time": "2023-09-13T13:18:48"
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
