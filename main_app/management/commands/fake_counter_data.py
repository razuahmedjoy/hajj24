import random
from django.core.management.base import BaseCommand
from main_app.models import Camera, CounterHistory
from main_app.api.serializers import CreateCounterHistorySerializer

class Command(BaseCommand):
    help = 'Generate and post dummy camera data to the database'

    def handle(self, *args, **options):
        all_cameras = Camera.objects.all()
        counters_per_camera = {}

        dummy_data_list =   [
    {
      "total_in": 27,
      "total_out": 5,
      "total": 22,
      "start_time": "1998-06-01T16:29:06.590Z",
      "end_time": "1998-06-02T00:26:47.995Z"
    },
    {
      "total_in": 45,
      "total_out": 37,
      "total": 8,
      "start_time": "2015-09-22T11:57:36.333Z",
      "end_time": "2015-09-27T00:49:41.337Z"
    },
    {
      "total_in": 4,
      "total_out": 3,
      "total": 1,
      "start_time": "2020-08-03T20:54:01.632Z",
      "end_time": "2020-08-11T23:17:23.240Z"
    },
    {
      "total_in": 26,
      "total_out": 22,
      "total": 4,
      "start_time": "2023-08-07T00:05:30.851Z",
      "end_time": "2023-08-07T04:37:48.022Z"
    },
    {
      "total_in": 10,
      "total_out": 2,
      "total": 8,
      "start_time": "1973-05-30T19:42:47.516Z",
      "end_time": "1973-06-05T09:38:44.881Z"
    },
    {
      "total_in": 42,
      "total_out": 7,
      "total": 35,
      "start_time": "2018-05-20T20:17:24.284Z",
      "end_time": "2018-05-27T16:31:44.200Z"
    },
    {
      "total_in": 87,
      "total_out": 15,
      "total": 72,
      "start_time": "2008-07-05T09:43:01.010Z",
      "end_time": "2008-07-07T03:37:24.858Z"
    },
    {
      "total_in": 7,
      "total_out": 6,
      "total": 1,
      "start_time": "1992-11-16T12:09:50.441Z",
      "end_time": "1992-11-24T12:23:13.405Z"
    },
    {
      "total_in": 44,
      "total_out": 25,
      "total": 19,
      "start_time": "1992-03-03T05:43:06.615Z",
      "end_time": "1992-03-04T01:00:33.969Z"
    },
    {
      "total_in": 50,
      "total_out": 46,
      "total": 4,
      "start_time": "1974-10-25T08:26:59.229Z",
      "end_time": "1974-11-02T07:34:02.787Z"
    },
    {
      "total_in": 11,
      "total_out": 6,
      "total": 5,
      "start_time": "2011-05-12T08:23:09.115Z",
      "end_time": "2011-05-14T10:54:09.319Z"
    },
    {
      "total_in": 9,
      "total_out": 5,
      "total": 4,
      "start_time": "2020-04-14T23:58:52.122Z",
      "end_time": "2020-04-24T12:39:55.908Z"
    },
    {
      "total_in": 13,
      "total_out": 7,
      "total": 6,
      "start_time": "1994-11-20T08:52:30.697Z",
      "end_time": "1994-11-26T12:06:03.467Z"
    },
    {
      "total_in": 36,
      "total_out": 31,
      "total": 5,
      "start_time": "1996-09-12T10:11:34.955Z",
      "end_time": "1996-09-14T11:30:31.987Z"
    },
    {
      "total_in": 46,
      "total_out": 46,
      "total": 0,
      "start_time": "1976-07-03T09:29:19.215Z",
      "end_time": "1976-07-05T00:43:19.256Z"
    },
    {
      "total_in": 86,
      "total_out": 16,
      "total": 70,
      "start_time": "1985-08-03T23:09:12.085Z",
      "end_time": "1985-08-09T10:35:10.741Z"
    },
    {
      "total_in": 56,
      "total_out": 40,
      "total": 16,
      "start_time": "1976-04-23T04:49:16.531Z",
      "end_time": "1976-04-28T16:11:59.412Z"
    },
    {
      "total_in": 47,
      "total_out": 14,
      "total": 33,
      "start_time": "1995-07-02T13:56:13.488Z",
      "end_time": "1995-07-10T16:28:33.589Z"
    },
    {
      "total_in": 47,
      "total_out": 46,
      "total": 1,
      "start_time": "2002-10-17T10:08:59.791Z",
      "end_time": "2002-10-26T02:31:18.622Z"
    },
    {
      "total_in": 13,
      "total_out": 11,
      "total": 2,
      "start_time": "2015-03-30T18:18:27.898Z",
      "end_time": "2015-03-31T20:16:36.065Z"
    },
    {
      "total_in": 75,
      "total_out": 9,
      "total": 66,
      "start_time": "2007-06-17T10:50:26.299Z",
      "end_time": "2007-06-19T20:55:00.850Z"
    },
    {
      "total_in": 83,
      "total_out": 49,
      "total": 34,
      "start_time": "1982-05-31T03:06:48.933Z",
      "end_time": "1982-06-06T02:47:51.787Z"
    },
    {
      "total_in": 1,
      "total_out": 1,
      "total": 0,
      "start_time": "2005-02-08T04:41:22.019Z",
      "end_time": "2005-02-14T13:20:34.357Z"
    },
    {
      "total_in": 17,
      "total_out": 9,
      "total": 8,
      "start_time": "1988-08-06T20:41:31.538Z",
      "end_time": "1988-08-12T04:40:47.496Z"
    },
    {
      "total_in": 42,
      "total_out": 23,
      "total": 19,
      "start_time": "1978-03-13T02:43:06.761Z",
      "end_time": "1978-03-16T22:12:48.016Z"
    },
    {
      "total_in": 51,
      "total_out": 4,
      "total": 47,
      "start_time": "2004-02-25T07:02:09.110Z",
      "end_time": "2004-02-28T17:58:07.855Z"
    },
    {
      "total_in": 99,
      "total_out": 48,
      "total": 51,
      "start_time": "1999-10-29T08:11:32.340Z",
      "end_time": "1999-11-05T11:39:40.154Z"
    },
    {
      "total_in": 52,
      "total_out": 25,
      "total": 27,
      "start_time": "1981-08-29T10:26:26.252Z",
      "end_time": "1981-09-02T08:59:45.732Z"
    },
    {
      "total_in": 73,
      "total_out": 49,
      "total": 24,
      "start_time": "2008-11-24T04:58:49.988Z",
      "end_time": "2008-11-29T03:05:42.644Z"
    },
    {
      "total_in": 14,
      "total_out": 7,
      "total": 7,
      "start_time": "1986-08-12T16:53:37.174Z",
      "end_time": "1986-08-20T07:09:45.851Z"
    },
    {
      "total_in": 66,
      "total_out": 62,
      "total": 4,
      "start_time": "1984-12-03T11:24:00.965Z",
      "end_time": "1984-12-12T03:52:13.977Z"
    },
    {
      "total_in": 72,
      "total_out": 36,
      "total": 36,
      "start_time": "1981-11-20T18:11:57.440Z",
      "end_time": "1981-11-22T01:43:42.146Z"
    },
    {
      "total_in": 74,
      "total_out": 63,
      "total": 11,
      "start_time": "2023-06-25T20:16:11.233Z",
      "end_time": "2023-06-30T00:59:59.503Z"
    },
    {
      "total_in": 45,
      "total_out": 7,
      "total": 38,
      "start_time": "1997-12-16T01:14:19.719Z",
      "end_time": "1997-12-18T01:11:23.592Z"
    },
    {
      "total_in": 100,
      "total_out": 1,
      "total": 99,
      "start_time": "1974-11-13T16:49:32.634Z",
      "end_time": "1974-11-19T22:13:48.089Z"
    },
    {
      "total_in": 16,
      "total_out": 6,
      "total": 10,
      "start_time": "1978-09-27T17:29:52.802Z",
      "end_time": "1978-09-30T20:11:05.732Z"
    },
    {
      "total_in": 34,
      "total_out": 31,
      "total": 3,
      "start_time": "2011-05-09T13:23:44.390Z",
      "end_time": "2011-05-16T12:41:53.117Z"
    },
    {
      "total_in": 5,
      "total_out": 4,
      "total": 1,
      "start_time": "1984-12-08T20:01:23.069Z",
      "end_time": "1984-12-11T11:45:06.088Z"
    },
    {
      "total_in": 18,
      "total_out": 5,
      "total": 13,
      "start_time": "2015-12-24T23:55:14.957Z",
      "end_time": "2015-12-29T09:29:52.462Z"
    },
    {
      "total_in": 61,
      "total_out": 27,
      "total": 34,
      "start_time": "2004-06-08T18:06:58.806Z",
      "end_time": "2004-06-16T14:44:30.711Z"
    },
    {
      "total_in": 29,
      "total_out": 14,
      "total": 15,
      "start_time": "2011-08-03T10:01:30.207Z",
      "end_time": "2011-08-10T14:12:27.045Z"
    },
    {
      "total_in": 50,
      "total_out": 45,
      "total": 5,
      "start_time": "1972-12-12T17:28:22.524Z",
      "end_time": "1972-12-17T21:22:03.422Z"
    },
    {
      "total_in": 82,
      "total_out": 64,
      "total": 18,
      "start_time": "2016-09-11T05:11:17.183Z",
      "end_time": "2016-09-11T20:02:47.357Z"
    },
    {
      "total_in": 99,
      "total_out": 49,
      "total": 50,
      "start_time": "2016-08-27T04:14:20.475Z",
      "end_time": "2016-09-02T13:41:44.552Z"
    },
    {
      "total_in": 62,
      "total_out": 59,
      "total": 3,
      "start_time": "1991-07-07T20:29:51.208Z",
      "end_time": "1991-07-15T06:52:09.263Z"
    },
    {
      "total_in": 93,
      "total_out": 22,
      "total": 71,
      "start_time": "1996-01-01T15:25:54.363Z",
      "end_time": "1996-01-10T23:37:52.579Z"
    },
    {
      "total_in": 78,
      "total_out": 15,
      "total": 63,
      "start_time": "2000-12-16T01:59:44.795Z",
      "end_time": "2000-12-22T23:51:13.057Z"
    },
    {
      "total_in": 70,
      "total_out": 53,
      "total": 17,
      "start_time": "1979-02-24T21:19:24.981Z",
      "end_time": "1979-02-27T04:08:00.499Z"
    },
    {
      "total_in": 58,
      "total_out": 35,
      "total": 23,
      "start_time": "1971-05-04T20:36:02.982Z",
      "end_time": "1971-05-10T11:48:58.033Z"
    },
    {
      "total_in": 75,
      "total_out": 17,
      "total": 58,
      "start_time": "2023-01-22T23:53:18.008Z",
      "end_time": "2023-01-30T02:17:13.453Z"
    },
    {
      "total_in": 83,
      "total_out": 80,
      "total": 3,
      "start_time": "2020-11-18T13:10:31.295Z",
      "end_time": "2020-11-20T11:41:35.092Z"
    },
    {
      "total_in": 25,
      "total_out": 1,
      "total": 24,
      "start_time": "2005-10-30T04:09:41.846Z",
      "end_time": "2005-11-04T22:31:16.684Z"
    },
    {
      "total_in": 47,
      "total_out": 8,
      "total": 39,
      "start_time": "2006-09-13T23:50:52.218Z",
      "end_time": "2006-09-14T08:52:05.114Z"
    },
    {
      "total_in": 18,
      "total_out": 7,
      "total": 11,
      "start_time": "2023-01-11T17:21:54.715Z",
      "end_time": "2023-01-17T19:18:07.333Z"
    },
    {
      "total_in": 13,
      "total_out": 8,
      "total": 5,
      "start_time": "2017-06-24T22:08:36.999Z",
      "end_time": "2017-07-01T04:46:21.164Z"
    },
    {
      "total_in": 52,
      "total_out": 17,
      "total": 35,
      "start_time": "1972-02-25T03:22:41.689Z",
      "end_time": "1972-03-03T18:48:17.372Z"
    },
    {
      "total_in": 47,
      "total_out": 21,
      "total": 26,
      "start_time": "2003-10-28T13:35:42.858Z",
      "end_time": "2003-10-28T23:08:51.208Z"
    },
    {
      "total_in": 31,
      "total_out": 7,
      "total": 24,
      "start_time": "2022-04-13T16:09:15.117Z",
      "end_time": "2022-04-21T18:52:21.531Z"
    },
    {
      "total_in": 89,
      "total_out": 49,
      "total": 40,
      "start_time": "2016-07-22T15:14:06.762Z",
      "end_time": "2016-07-22T20:45:51.756Z"
    },
    {
      "total_in": 1,
      "total_out": 1,
      "total": 0,
      "start_time": "1981-11-05T23:38:33.091Z",
      "end_time": "1981-11-15T17:31:07.047Z"
    },
    {
      "total_in": 7,
      "total_out": 6,
      "total": 1,
      "start_time": "2015-08-24T11:41:40.162Z",
      "end_time": "2015-08-24T22:41:07.843Z"
    },
    {
      "total_in": 7,
      "total_out": 7,
      "total": 0,
      "start_time": "2005-12-04T14:04:00.095Z",
      "end_time": "2005-12-10T12:58:09.751Z"
    },
    {
      "total_in": 31,
      "total_out": 5,
      "total": 26,
      "start_time": "2007-11-05T02:22:40.061Z",
      "end_time": "2007-11-07T03:14:52.409Z"
    },
    {
      "total_in": 12,
      "total_out": 1,
      "total": 11,
      "start_time": "1972-02-14T05:19:37.949Z",
      "end_time": "1972-02-22T03:17:25.026Z"
    },
    {
      "total_in": 16,
      "total_out": 1,
      "total": 15,
      "start_time": "1970-01-06T04:21:34.321Z",
      "end_time": "1970-01-07T11:41:56.341Z"
    },
    {
      "total_in": 81,
      "total_out": 39,
      "total": 42,
      "start_time": "1978-05-26T23:26:13.052Z",
      "end_time": "1978-06-05T04:52:35.168Z"
    },
    {
      "total_in": 69,
      "total_out": 12,
      "total": 57,
      "start_time": "1996-07-17T19:59:20.820Z",
      "end_time": "1996-07-18T16:19:16.776Z"
    },
    {
      "total_in": 6,
      "total_out": 5,
      "total": 1,
      "start_time": "1985-02-16T21:52:53.929Z",
      "end_time": "1985-02-21T09:34:03.642Z"
    },
    {
      "total_in": 83,
      "total_out": 13,
      "total": 70,
      "start_time": "1971-04-19T00:36:38.789Z",
      "end_time": "1971-04-24T02:59:09.548Z"
    },
    {
      "total_in": 14,
      "total_out": 5,
      "total": 9,
      "start_time": "2021-10-01T09:40:37.569Z",
      "end_time": "2021-10-01T12:17:44.727Z"
    },
    {
      "total_in": 77,
      "total_out": 29,
      "total": 48,
      "start_time": "2009-05-11T10:00:38.078Z",
      "end_time": "2009-05-15T22:26:33.226Z"
    },
    {
      "total_in": 41,
      "total_out": 34,
      "total": 7,
      "start_time": "1994-05-28T08:03:33.972Z",
      "end_time": "1994-06-03T13:50:43.272Z"
    },
    {
      "total_in": 67,
      "total_out": 60,
      "total": 7,
      "start_time": "1992-12-06T09:03:35.456Z",
      "end_time": "1992-12-08T02:41:38.975Z"
    },
    {
      "total_in": 68,
      "total_out": 52,
      "total": 16,
      "start_time": "1989-07-13T17:58:05.946Z",
      "end_time": "1989-07-15T04:19:23.580Z"
    },
    {
      "total_in": 45,
      "total_out": 34,
      "total": 11,
      "start_time": "1986-08-25T01:31:18.834Z",
      "end_time": "1986-08-26T22:30:25.340Z"
    },
    {
      "total_in": 24,
      "total_out": 17,
      "total": 7,
      "start_time": "2022-02-27T13:08:59.215Z",
      "end_time": "2022-03-01T04:26:57.966Z"
    },
    {
      "total_in": 47,
      "total_out": 5,
      "total": 42,
      "start_time": "2015-11-16T21:11:48.695Z",
      "end_time": "2015-11-22T11:26:45.574Z"
    },
    {
      "total_in": 64,
      "total_out": 40,
      "total": 24,
      "start_time": "1970-09-27T22:23:29.267Z",
      "end_time": "1970-09-29T22:54:47.628Z"
    },
    {
      "total_in": 67,
      "total_out": 27,
      "total": 40,
      "start_time": "1972-05-19T19:43:09.448Z",
      "end_time": "1972-05-29T07:14:52.988Z"
    },
    {
      "total_in": 89,
      "total_out": 60,
      "total": 29,
      "start_time": "1979-11-24T21:11:48.335Z",
      "end_time": "1979-11-30T08:09:08.501Z"
    }
  ]

        for dummy_data in dummy_data_list:
            random_camera = random.choice(all_cameras)
            if random_camera.id not in counters_per_camera:
                counters_per_camera[random_camera.id] = 1
            else:
                if counters_per_camera[random_camera.id] >= 5:
                    continue

                counters_per_camera[random_camera.id] += 1

            dummy_data["camera"] = random_camera.id
            dummy_data["sn"] = random_camera.sn

            counter_history_serializer = CreateCounterHistorySerializer(data=dummy_data)
            counter_history_serializer.is_valid(raise_exception=True)
            counter_history_serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted dummy camera data to the database'))
