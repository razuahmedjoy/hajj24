# myapp/management/commands/fake_camera_data.py
import random
import datetime
from django.core.management.base import BaseCommand
from main_app.models import Camera, CounterHistory
from main_app.api.serializers import CreateCounterHistorySerializer

class Command(BaseCommand):
    help = 'Generate and post dummy camera data to the database'

    def handle(self, *args, **options):
        # Get all available cameras from the database
        all_cameras = Camera.objects.all()

        # Assuming you have a list of dummy JSON data
        dummy_data_list = [
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
  },
  {
    "total_in": 88,
    "total_out": 16,
    "total": 72,
    "start_time": "1977-11-29T09:11:23.702Z",
    "end_time": "1977-12-06T23:43:07.982Z"
  },
  {
    "total_in": 87,
    "total_out": 82,
    "total": 5,
    "start_time": "2012-10-01T09:25:34.572Z",
    "end_time": "2012-10-03T10:55:35.361Z"
  },
  {
    "total_in": 22,
    "total_out": 8,
    "total": 14,
    "start_time": "1979-08-23T20:52:05.892Z",
    "end_time": "1979-08-25T17:30:50.723Z"
  },
  {
    "total_in": 74,
    "total_out": 6,
    "total": 68,
    "start_time": "2009-06-14T05:17:51.779Z",
    "end_time": "2009-06-16T14:08:05.025Z"
  },
  {
    "total_in": 32,
    "total_out": 19,
    "total": 13,
    "start_time": "2006-08-12T10:01:16.945Z",
    "end_time": "2006-08-22T05:36:58.397Z"
  },
  {
    "total_in": 64,
    "total_out": 14,
    "total": 50,
    "start_time": "2019-09-26T02:06:42.939Z",
    "end_time": "2019-09-27T22:29:11.113Z"
  },
  {
    "total_in": 83,
    "total_out": 53,
    "total": 30,
    "start_time": "1980-07-30T02:32:19.526Z",
    "end_time": "1980-07-30T21:13:32.985Z"
  },
  {
    "total_in": 78,
    "total_out": 51,
    "total": 27,
    "start_time": "2012-12-30T07:27:28.197Z",
    "end_time": "2013-01-02T09:27:28.471Z"
  },
  {
    "total_in": 31,
    "total_out": 21,
    "total": 10,
    "start_time": "1973-11-30T14:29:08.963Z",
    "end_time": "1973-12-04T19:41:07.258Z"
  },
  {
    "total_in": 30,
    "total_out": 16,
    "total": 14,
    "start_time": "2002-09-07T11:47:39.785Z",
    "end_time": "2002-09-14T01:51:41.667Z"
  },
  {
    "total_in": 15,
    "total_out": 9,
    "total": 6,
    "start_time": "2001-04-24T17:56:44.866Z",
    "end_time": "2001-04-26T23:30:34.609Z"
  },
  {
    "total_in": 1,
    "total_out": 1,
    "total": 0,
    "start_time": "1990-10-26T22:59:59.654Z",
    "end_time": "1990-11-05T19:49:28.054Z"
  },
  {
    "total_in": 59,
    "total_out": 29,
    "total": 30,
    "start_time": "2018-04-14T08:37:04.513Z",
    "end_time": "2018-04-14T18:17:41.085Z"
  },
  {
    "total_in": 65,
    "total_out": 21,
    "total": 44,
    "start_time": "1971-08-22T06:02:39.041Z",
    "end_time": "1971-08-30T09:16:34.090Z"
  },
  {
    "total_in": 18,
    "total_out": 11,
    "total": 7,
    "start_time": "1975-08-26T15:14:04.768Z",
    "end_time": "1975-08-26T20:39:48.986Z"
  },
  {
    "total_in": 50,
    "total_out": 1,
    "total": 49,
    "start_time": "1990-02-06T14:30:43.934Z",
    "end_time": "1990-02-10T01:32:36.484Z"
  },
  {
    "total_in": 87,
    "total_out": 49,
    "total": 38,
    "start_time": "1978-02-27T20:24:38.043Z",
    "end_time": "1978-03-05T11:32:29.792Z"
  },
  {
    "total_in": 11,
    "total_out": 4,
    "total": 7,
    "start_time": "1991-04-30T03:55:30.248Z",
    "end_time": "1991-05-03T01:40:32.327Z"
  },
  {
    "total_in": 100,
    "total_out": 2,
    "total": 98,
    "start_time": "2000-04-11T08:24:28.557Z",
    "end_time": "2000-04-15T03:25:11.237Z"
  },
  {
    "total_in": 18,
    "total_out": 18,
    "total": 0,
    "start_time": "2004-10-18T06:14:46.165Z",
    "end_time": "2004-10-24T09:58:45.908Z"
  },
  {
    "total_in": 66,
    "total_out": 58,
    "total": 8,
    "start_time": "1982-12-12T05:45:56.586Z",
    "end_time": "1982-12-13T05:45:47.540Z"
  },
  {
    "total_in": 74,
    "total_out": 54,
    "total": 20,
    "start_time": "2011-02-24T11:10:49.106Z",
    "end_time": "2011-02-25T19:44:34.671Z"
  },
  {
    "total_in": 44,
    "total_out": 39,
    "total": 5,
    "start_time": "2012-03-22T03:00:15.440Z",
    "end_time": "2012-03-24T21:42:51.935Z"
  },
  {
    "total_in": 26,
    "total_out": 5,
    "total": 21,
    "start_time": "2015-12-27T07:34:31.715Z",
    "end_time": "2016-01-01T05:33:21.641Z"
  },
  {
    "total_in": 14,
    "total_out": 7,
    "total": 7,
    "start_time": "1977-06-10T09:25:28.313Z",
    "end_time": "1977-06-11T21:53:23.484Z"
  },
  {
    "total_in": 35,
    "total_out": 1,
    "total": 34,
    "start_time": "2019-08-09T17:53:18.340Z",
    "end_time": "2019-08-12T09:09:20.750Z"
  },
  {
    "total_in": 41,
    "total_out": 15,
    "total": 26,
    "start_time": "1994-09-23T22:39:35.656Z",
    "end_time": "1994-09-28T05:55:24.910Z"
  },
  {
    "total_in": 52,
    "total_out": 12,
    "total": 40,
    "start_time": "2000-05-17T05:05:07.153Z",
    "end_time": "2000-05-21T19:34:26.050Z"
  },
  {
    "total_in": 92,
    "total_out": 56,
    "total": 36,
    "start_time": "1986-06-18T09:49:28.903Z",
    "end_time": "1986-06-23T18:59:43.439Z"
  },
  {
    "total_in": 24,
    "total_out": 15,
    "total": 9,
    "start_time": "2000-05-27T00:28:46.373Z",
    "end_time": "2000-05-27T12:40:57.407Z"
  },
  {
    "total_in": 12,
    "total_out": 10,
    "total": 2,
    "start_time": "1990-04-28T02:16:57.402Z",
    "end_time": "1990-05-04T08:27:08.794Z"
  },
  {
    "total_in": 36,
    "total_out": 10,
    "total": 26,
    "start_time": "2023-06-12T06:12:50.321Z",
    "end_time": "2023-06-19T15:28:24.255Z"
  },
  {
    "total_in": 93,
    "total_out": 17,
    "total": 76,
    "start_time": "1994-10-12T01:32:25.980Z",
    "end_time": "1994-10-18T04:46:48.925Z"
  },
  {
    "total_in": 99,
    "total_out": 48,
    "total": 51,
    "start_time": "1986-05-01T18:30:46.911Z",
    "end_time": "1986-05-08T07:02:32.286Z"
  },
  {
    "total_in": 83,
    "total_out": 60,
    "total": 23,
    "start_time": "2016-04-25T22:45:44.106Z",
    "end_time": "2016-05-04T09:39:30.684Z"
  },
  {
    "total_in": 57,
    "total_out": 50,
    "total": 7,
    "start_time": "2000-08-28T10:01:43.899Z",
    "end_time": "2000-09-04T20:08:53.294Z"
  },
  {
    "total_in": 36,
    "total_out": 15,
    "total": 21,
    "start_time": "2021-07-13T19:02:47.870Z",
    "end_time": "2021-07-21T05:37:31.623Z"
  },
  {
    "total_in": 33,
    "total_out": 23,
    "total": 10,
    "start_time": "2013-09-29T10:20:10.251Z",
    "end_time": "2013-10-02T08:51:00.781Z"
  },
  {
    "total_in": 3,
    "total_out": 1,
    "total": 2,
    "start_time": "1993-03-10T15:43:44.569Z",
    "end_time": "1993-03-14T23:41:04.791Z"
  },
  {
    "total_in": 39,
    "total_out": 28,
    "total": 11,
    "start_time": "2015-03-10T12:17:48.910Z",
    "end_time": "2015-03-18T07:49:25.694Z"
  },
  {
    "total_in": 57,
    "total_out": 46,
    "total": 11,
    "start_time": "1978-08-04T02:16:23.828Z",
    "end_time": "1978-08-11T21:45:58.607Z"
  },
  {
    "total_in": 32,
    "total_out": 20,
    "total": 12,
    "start_time": "1977-07-08T20:50:26.357Z",
    "end_time": "1977-07-12T23:17:30.776Z"
  },
  {
    "total_in": 11,
    "total_out": 6,
    "total": 5,
    "start_time": "2018-02-21T07:57:10.751Z",
    "end_time": "2018-02-27T19:37:25.833Z"
  },
  {
    "total_in": 7,
    "total_out": 2,
    "total": 5,
    "start_time": "2014-02-03T02:29:49.790Z",
    "end_time": "2014-02-07T06:17:20.094Z"
  },
  {
    "total_in": 97,
    "total_out": 96,
    "total": 1,
    "start_time": "1988-05-31T08:56:47.017Z",
    "end_time": "1988-06-05T19:29:51.953Z"
  },
  {
    "total_in": 64,
    "total_out": 43,
    "total": 21,
    "start_time": "1973-11-23T12:17:44.139Z",
    "end_time": "1973-11-26T17:18:25.425Z"
  },
  {
    "total_in": 36,
    "total_out": 3,
    "total": 33,
    "start_time": "2022-01-21T20:23:39.952Z",
    "end_time": "2022-01-22T08:29:10.212Z"
  },
  {
    "total_in": 96,
    "total_out": 70,
    "total": 26,
    "start_time": "1986-04-07T05:32:27.869Z",
    "end_time": "1986-04-09T21:44:37.865Z"
  },
  {
    "total_in": 20,
    "total_out": 20,
    "total": 0,
    "start_time": "1994-12-29T02:44:32.567Z",
    "end_time": "1994-12-31T18:26:59.183Z"
  },
  {
    "total_in": 90,
    "total_out": 29,
    "total": 61,
    "start_time": "2016-07-05T20:40:25.062Z",
    "end_time": "2016-07-12T04:29:16.005Z"
  },
  {
    "total_in": 6,
    "total_out": 3,
    "total": 3,
    "start_time": "2002-02-04T06:22:04.534Z",
    "end_time": "2002-02-11T05:24:07.440Z"
  },
  {
    "total_in": 25,
    "total_out": 7,
    "total": 18,
    "start_time": "2017-02-02T21:23:25.361Z",
    "end_time": "2017-02-03T16:32:09.141Z"
  },
  {
    "total_in": 66,
    "total_out": 19,
    "total": 47,
    "start_time": "2013-12-28T07:59:29.786Z",
    "end_time": "2014-01-05T12:37:45.867Z"
  },
  {
    "total_in": 30,
    "total_out": 29,
    "total": 1,
    "start_time": "2007-01-26T15:15:40.038Z",
    "end_time": "2007-02-04T01:33:18.105Z"
  },
  {
    "total_in": 89,
    "total_out": 81,
    "total": 8,
    "start_time": "2004-01-05T03:17:46.884Z",
    "end_time": "2004-01-06T12:57:23.205Z"
  },
  {
    "total_in": 63,
    "total_out": 17,
    "total": 46,
    "start_time": "1970-10-13T14:58:26.115Z",
    "end_time": "1970-10-16T21:26:05.339Z"
  },
  {
    "total_in": 66,
    "total_out": 56,
    "total": 10,
    "start_time": "1978-03-16T06:39:26.190Z",
    "end_time": "1978-03-17T03:10:13.565Z"
  },
  {
    "total_in": 97,
    "total_out": 60,
    "total": 37,
    "start_time": "2014-10-03T12:49:13.775Z",
    "end_time": "2014-10-12T03:05:22.225Z"
  },
  {
    "total_in": 6,
    "total_out": 5,
    "total": 1,
    "start_time": "1990-10-05T06:45:24.272Z",
    "end_time": "1990-10-11T17:56:41.141Z"
  },
  {
    "total_in": 97,
    "total_out": 22,
    "total": 75,
    "start_time": "1987-10-07T03:15:20.611Z",
    "end_time": "1987-10-11T23:47:22.552Z"
  },
  {
    "total_in": 76,
    "total_out": 27,
    "total": 49,
    "start_time": "2005-06-20T10:43:06.964Z",
    "end_time": "2005-06-24T01:22:27.425Z"
  },
  {
    "total_in": 67,
    "total_out": 37,
    "total": 30,
    "start_time": "2014-02-10T22:41:03.164Z",
    "end_time": "2014-02-20T01:20:52.425Z"
  },
  {
    "total_in": 18,
    "total_out": 16,
    "total": 2,
    "start_time": "1988-09-24T23:45:58.716Z",
    "end_time": "1988-10-03T07:41:45.415Z"
  },
  {
    "total_in": 59,
    "total_out": 26,
    "total": 33,
    "start_time": "1997-02-16T14:50:50.962Z",
    "end_time": "1997-02-20T07:13:47.798Z"
  },
  {
    "total_in": 76,
    "total_out": 4,
    "total": 72,
    "start_time": "1973-10-27T08:42:00.156Z",
    "end_time": "1973-11-02T14:28:11.495Z"
  },
  {
    "total_in": 76,
    "total_out": 59,
    "total": 17,
    "start_time": "2017-06-12T09:15:05.360Z",
    "end_time": "2017-06-14T07:48:14.285Z"
  },
  {
    "total_in": 40,
    "total_out": 1,
    "total": 39,
    "start_time": "2006-05-09T02:30:37.560Z",
    "end_time": "2006-05-19T00:46:00.142Z"
  },
  {
    "total_in": 61,
    "total_out": 12,
    "total": 49,
    "start_time": "1975-02-20T15:14:53.292Z",
    "end_time": "1975-02-26T00:42:16.795Z"
  },
  {
    "total_in": 6,
    "total_out": 4,
    "total": 2,
    "start_time": "1983-12-04T15:31:06.014Z",
    "end_time": "1983-12-10T22:59:44.198Z"
  },
  {
    "total_in": 8,
    "total_out": 1,
    "total": 7,
    "start_time": "1977-04-10T04:13:07.993Z",
    "end_time": "1977-04-17T22:01:34.070Z"
  },
  {
    "total_in": 86,
    "total_out": 59,
    "total": 27,
    "start_time": "2009-09-28T08:00:07.884Z",
    "end_time": "2009-10-08T02:49:47.079Z"
  },
  {
    "total_in": 74,
    "total_out": 23,
    "total": 51,
    "start_time": "2001-08-07T22:40:53.070Z",
    "end_time": "2001-08-13T15:43:52.616Z"
  },
  {
    "total_in": 63,
    "total_out": 54,
    "total": 9,
    "start_time": "2022-09-16T18:40:34.676Z",
    "end_time": "2022-09-16T21:49:43.812Z"
  },
  {
    "total_in": 14,
    "total_out": 13,
    "total": 1,
    "start_time": "2009-07-28T01:01:12.723Z",
    "end_time": "2009-07-30T20:36:09.879Z"
  },
  {
    "total_in": 51,
    "total_out": 44,
    "total": 7,
    "start_time": "2010-08-07T21:26:48.566Z",
    "end_time": "2010-08-10T20:46:03.826Z"
  },
  {
    "total_in": 60,
    "total_out": 54,
    "total": 6,
    "start_time": "2012-12-21T11:38:34.432Z",
    "end_time": "2012-12-25T03:42:54.344Z"
  },
  {
    "total_in": 3,
    "total_out": 2,
    "total": 1,
    "start_time": "1975-07-31T12:16:37.066Z",
    "end_time": "1975-08-07T21:55:14.241Z"
  },
  {
    "total_in": 88,
    "total_out": 9,
    "total": 79,
    "start_time": "1977-02-03T00:41:46.254Z",
    "end_time": "1977-02-12T14:58:45.211Z"
  },
  {
    "total_in": 8,
    "total_out": 5,
    "total": 3,
    "start_time": "2005-11-16T12:02:49.373Z",
    "end_time": "2005-11-18T06:22:03.008Z"
  },
  {
    "total_in": 28,
    "total_out": 16,
    "total": 12,
    "start_time": "1997-10-07T09:16:46.740Z",
    "end_time": "1997-10-13T02:05:15.069Z"
  },
  {
    "total_in": 54,
    "total_out": 8,
    "total": 46,
    "start_time": "2013-02-18T15:18:01.259Z",
    "end_time": "2013-02-26T22:46:34.107Z"
  },
  {
    "total_in": 74,
    "total_out": 3,
    "total": 71,
    "start_time": "1982-02-07T07:43:36.251Z",
    "end_time": "1982-02-12T03:01:11.446Z"
  },
  {
    "total_in": 82,
    "total_out": 39,
    "total": 43,
    "start_time": "1986-01-21T17:10:58.919Z",
    "end_time": "1986-01-27T06:47:02.758Z"
  },
  {
    "total_in": 59,
    "total_out": 49,
    "total": 10,
    "start_time": "1970-08-28T04:07:56.277Z",
    "end_time": "1970-08-30T09:16:01.355Z"
  },
  {
    "total_in": 67,
    "total_out": 37,
    "total": 30,
    "start_time": "1977-12-13T10:43:04.621Z",
    "end_time": "1977-12-16T06:14:05.378Z"
  },
  {
    "total_in": 4,
    "total_out": 3,
    "total": 1,
    "start_time": "1976-03-19T01:07:30.077Z",
    "end_time": "1976-03-19T20:09:31.660Z"
  },
  {
    "total_in": 83,
    "total_out": 38,
    "total": 45,
    "start_time": "2020-07-12T04:07:08.942Z",
    "end_time": "2020-07-18T11:23:18.832Z"
  },
  {
    "total_in": 63,
    "total_out": 15,
    "total": 48,
    "start_time": "1980-04-30T07:52:20.182Z",
    "end_time": "1980-05-05T05:52:14.054Z"
  },
  {
    "total_in": 72,
    "total_out": 58,
    "total": 14,
    "start_time": "1974-04-25T05:10:02.659Z",
    "end_time": "1974-05-02T16:19:41.801Z"
  },
  {
    "total_in": 99,
    "total_out": 89,
    "total": 10,
    "start_time": "1998-11-23T17:17:39.469Z",
    "end_time": "1998-12-01T10:29:13.358Z"
  },
  {
    "total_in": 33,
    "total_out": 29,
    "total": 4,
    "start_time": "2021-06-19T09:31:41.601Z",
    "end_time": "2021-06-26T10:22:33.914Z"
  },
  {
    "total_in": 53,
    "total_out": 49,
    "total": 4,
    "start_time": "2019-01-05T23:16:46.973Z",
    "end_time": "2019-01-08T11:14:25.994Z"
  },
  {
    "total_in": 87,
    "total_out": 11,
    "total": 76,
    "start_time": "1975-07-03T09:32:52.433Z",
    "end_time": "1975-07-05T15:23:24.347Z"
  },
  {
    "total_in": 50,
    "total_out": 23,
    "total": 27,
    "start_time": "1977-02-03T22:25:24.211Z",
    "end_time": "1977-02-08T08:38:54.342Z"
  },
  {
    "total_in": 41,
    "total_out": 22,
    "total": 19,
    "start_time": "1974-06-12T13:24:10.717Z",
    "end_time": "1974-06-18T13:36:13.162Z"
  },
  {
    "total_in": 74,
    "total_out": 57,
    "total": 17,
    "start_time": "1999-07-04T04:21:20.015Z",
    "end_time": "1999-07-09T09:56:48.973Z"
  },
  {
    "total_in": 33,
    "total_out": 1,
    "total": 32,
    "start_time": "1994-01-31T12:45:49.223Z",
    "end_time": "1994-02-05T20:49:34.860Z"
  },
  {
    "total_in": 80,
    "total_out": 55,
    "total": 25,
    "start_time": "1989-10-26T07:58:39.329Z",
    "end_time": "1989-10-29T07:15:20.754Z"
  },
  {
    "total_in": 12,
    "total_out": 2,
    "total": 10,
    "start_time": "1971-05-09T13:13:16.878Z",
    "end_time": "1971-05-14T22:52:57.728Z"
  },
  {
    "total_in": 75,
    "total_out": 19,
    "total": 56,
    "start_time": "1980-09-27T08:12:47.582Z",
    "end_time": "1980-10-02T01:07:24.706Z"
  },
  {
    "total_in": 65,
    "total_out": 31,
    "total": 34,
    "start_time": "1992-10-16T13:47:06.512Z",
    "end_time": "1992-10-24T12:26:30.962Z"
  },
  {
    "total_in": 69,
    "total_out": 50,
    "total": 19,
    "start_time": "1997-09-05T21:43:06.032Z",
    "end_time": "1997-09-09T20:22:47.440Z"
  },
  {
    "total_in": 44,
    "total_out": 28,
    "total": 16,
    "start_time": "2009-06-21T21:03:11.033Z",
    "end_time": "2009-07-01T19:08:17.445Z"
  },
  {
    "total_in": 47,
    "total_out": 7,
    "total": 40,
    "start_time": "1993-06-05T14:19:28.277Z",
    "end_time": "1993-06-08T10:02:24.153Z"
  },
  {
    "total_in": 42,
    "total_out": 26,
    "total": 16,
    "start_time": "1997-07-10T06:41:40.226Z",
    "end_time": "1997-07-11T17:18:34.256Z"
  },
  {
    "total_in": 89,
    "total_out": 62,
    "total": 27,
    "start_time": "1982-10-31T10:44:28.178Z",
    "end_time": "1982-11-06T06:42:15.966Z"
  },
  {
    "total_in": 69,
    "total_out": 1,
    "total": 68,
    "start_time": "1977-07-02T03:18:16.970Z",
    "end_time": "1977-07-09T22:03:38.320Z"
  },
  {
    "total_in": 18,
    "total_out": 15,
    "total": 3,
    "start_time": "2000-05-28T05:55:50.467Z",
    "end_time": "2000-06-04T00:10:45.258Z"
  },
  {
    "total_in": 91,
    "total_out": 25,
    "total": 66,
    "start_time": "2004-11-23T09:10:33.376Z",
    "end_time": "2004-11-29T19:19:37.420Z"
  },
  {
    "total_in": 88,
    "total_out": 78,
    "total": 10,
    "start_time": "2019-03-17T02:54:00.916Z",
    "end_time": "2019-03-26T13:26:24.820Z"
  },
  {
    "total_in": 43,
    "total_out": 26,
    "total": 17,
    "start_time": "1992-08-11T01:38:46.522Z",
    "end_time": "1992-08-15T16:45:36.174Z"
  },
  {
    "total_in": 58,
    "total_out": 54,
    "total": 4,
    "start_time": "1993-08-06T14:57:40.627Z",
    "end_time": "1993-08-08T10:01:46.969Z"
  },
  {
    "total_in": 79,
    "total_out": 3,
    "total": 76,
    "start_time": "2009-01-17T03:37:08.214Z",
    "end_time": "2009-01-20T19:33:23.268Z"
  },
  {
    "total_in": 90,
    "total_out": 61,
    "total": 29,
    "start_time": "1982-05-28T21:08:33.657Z",
    "end_time": "1982-06-07T06:46:00.468Z"
  },
  {
    "total_in": 85,
    "total_out": 37,
    "total": 48,
    "start_time": "1981-07-03T22:35:16.043Z",
    "end_time": "1981-07-05T03:23:05.672Z"
  },
  {
    "total_in": 62,
    "total_out": 22,
    "total": 40,
    "start_time": "1998-05-24T20:42:40.317Z",
    "end_time": "1998-06-02T22:38:16.125Z"
  },
  {
    "total_in": 45,
    "total_out": 8,
    "total": 37,
    "start_time": "2001-08-01T08:44:32.883Z",
    "end_time": "2001-08-04T19:53:41.406Z"
  },
  {
    "total_in": 84,
    "total_out": 12,
    "total": 72,
    "start_time": "1978-02-21T17:00:54.756Z",
    "end_time": "1978-03-03T07:11:08.851Z"
  },
  {
    "total_in": 89,
    "total_out": 60,
    "total": 29,
    "start_time": "1975-01-17T08:36:11.366Z",
    "end_time": "1975-01-27T07:59:39.928Z"
  },
  {
    "total_in": 33,
    "total_out": 12,
    "total": 21,
    "start_time": "2001-03-21T20:31:45.892Z",
    "end_time": "2001-03-23T08:36:19.317Z"
  },
  {
    "total_in": 75,
    "total_out": 58,
    "total": 17,
    "start_time": "1993-02-11T10:33:25.166Z",
    "end_time": "1993-02-14T07:03:33.544Z"
  },
  {
    "total_in": 10,
    "total_out": 1,
    "total": 9,
    "start_time": "2012-03-15T22:38:59.352Z",
    "end_time": "2012-03-22T15:26:30.412Z"
  },
  {
    "total_in": 4,
    "total_out": 4,
    "total": 0,
    "start_time": "2001-09-19T19:32:11.499Z",
    "end_time": "2001-09-26T22:46:01.217Z"
  },
  {
    "total_in": 95,
    "total_out": 67,
    "total": 28,
    "start_time": "1985-02-08T14:59:07.367Z",
    "end_time": "1985-02-14T10:47:13.981Z"
  },
  {
    "total_in": 34,
    "total_out": 10,
    "total": 24,
    "start_time": "2008-12-10T06:43:09.017Z",
    "end_time": "2008-12-12T02:37:20.306Z"
  },
  {
    "total_in": 74,
    "total_out": 9,
    "total": 65,
    "start_time": "2022-07-07T06:27:33.862Z",
    "end_time": "2022-07-08T20:44:07.218Z"
  },
  {
    "total_in": 48,
    "total_out": 4,
    "total": 44,
    "start_time": "1990-07-06T16:39:02.935Z",
    "end_time": "1990-07-08T12:39:32.794Z"
  },
  {
    "total_in": 43,
    "total_out": 24,
    "total": 19,
    "start_time": "1983-11-03T06:01:04.898Z",
    "end_time": "1983-11-07T21:48:25.501Z"
  },
  {
    "total_in": 68,
    "total_out": 9,
    "total": 59,
    "start_time": "1970-09-16T17:07:28.041Z",
    "end_time": "1970-09-17T17:11:27.038Z"
  },
  {
    "total_in": 78,
    "total_out": 17,
    "total": 61,
    "start_time": "1973-11-27T15:22:05.930Z",
    "end_time": "1973-12-03T06:58:40.452Z"
  },
  {
    "total_in": 44,
    "total_out": 14,
    "total": 30,
    "start_time": "2022-10-11T11:50:33.813Z",
    "end_time": "2022-10-18T21:29:00.801Z"
  },
  {
    "total_in": 13,
    "total_out": 13,
    "total": 0,
    "start_time": "1985-04-15T02:30:20.833Z",
    "end_time": "1985-04-19T22:34:12.362Z"
  },
  {
    "total_in": 28,
    "total_out": 22,
    "total": 6,
    "start_time": "1982-07-31T21:07:08.971Z",
    "end_time": "1982-08-09T16:34:59.534Z"
  },
  {
    "total_in": 72,
    "total_out": 59,
    "total": 13,
    "start_time": "1972-01-09T15:38:42.675Z",
    "end_time": "1972-01-14T08:40:55.796Z"
  },
  {
    "total_in": 100,
    "total_out": 98,
    "total": 2,
    "start_time": "2001-07-09T10:36:04.452Z",
    "end_time": "2001-07-18T08:35:26.591Z"
  },
  {
    "total_in": 38,
    "total_out": 28,
    "total": 10,
    "start_time": "2008-06-09T08:01:26.782Z",
    "end_time": "2008-06-15T10:18:49.184Z"
  },
  {
    "total_in": 51,
    "total_out": 13,
    "total": 38,
    "start_time": "2011-05-30T04:01:59.572Z",
    "end_time": "2011-06-08T05:33:37.838Z"
  },
  {
    "total_in": 26,
    "total_out": 26,
    "total": 0,
    "start_time": "1999-06-30T09:48:01.620Z",
    "end_time": "1999-07-03T14:26:26.444Z"
  },
  {
    "total_in": 21,
    "total_out": 4,
    "total": 17,
    "start_time": "1992-10-13T05:38:12.128Z",
    "end_time": "1992-10-13T08:15:50.356Z"
  },
  {
    "total_in": 86,
    "total_out": 71,
    "total": 15,
    "start_time": "2002-10-05T23:15:10.342Z",
    "end_time": "2002-10-13T02:28:14.950Z"
  },
  {
    "total_in": 65,
    "total_out": 58,
    "total": 7,
    "start_time": "2000-02-09T08:51:06.130Z",
    "end_time": "2000-02-15T20:31:21.109Z"
  },
  {
    "total_in": 73,
    "total_out": 34,
    "total": 39,
    "start_time": "1998-01-16T05:50:42.235Z",
    "end_time": "1998-01-25T12:23:57.151Z"
  },
  {
    "total_in": 18,
    "total_out": 13,
    "total": 5,
    "start_time": "1976-05-06T03:38:21.893Z",
    "end_time": "1976-05-13T05:02:15.701Z"
  },
  {
    "total_in": 14,
    "total_out": 9,
    "total": 5,
    "start_time": "2016-10-17T21:22:15.966Z",
    "end_time": "2016-10-27T21:04:13.751Z"
  },
  {
    "total_in": 80,
    "total_out": 35,
    "total": 45,
    "start_time": "1985-06-07T10:17:12.318Z",
    "end_time": "1985-06-15T20:15:38.097Z"
  },
  {
    "total_in": 85,
    "total_out": 74,
    "total": 11,
    "start_time": "2014-06-03T12:18:53.386Z",
    "end_time": "2014-06-10T11:36:21.756Z"
  },
  {
    "total_in": 42,
    "total_out": 2,
    "total": 40,
    "start_time": "2014-01-01T22:26:24.459Z",
    "end_time": "2014-01-08T05:24:39.809Z"
  },
  {
    "total_in": 94,
    "total_out": 75,
    "total": 19,
    "start_time": "2017-04-25T22:58:36.660Z",
    "end_time": "2017-05-01T07:28:59.020Z"
  },
  {
    "total_in": 36,
    "total_out": 13,
    "total": 23,
    "start_time": "1991-02-26T13:31:50.399Z",
    "end_time": "1991-03-04T17:25:13.835Z"
  },
  {
    "total_in": 65,
    "total_out": 29,
    "total": 36,
    "start_time": "2002-12-23T21:18:13.381Z",
    "end_time": "2002-12-27T00:44:32.089Z"
  },
  {
    "total_in": 18,
    "total_out": 1,
    "total": 17,
    "start_time": "1976-10-26T10:11:45.033Z",
    "end_time": "1976-10-29T11:29:00.715Z"
  },
  {
    "total_in": 46,
    "total_out": 31,
    "total": 15,
    "start_time": "2017-02-25T23:15:42.125Z",
    "end_time": "2017-03-06T02:52:15.508Z"
  },
  {
    "total_in": 100,
    "total_out": 64,
    "total": 36,
    "start_time": "1970-12-13T08:58:04.776Z",
    "end_time": "1970-12-18T11:31:52.585Z"
  },
  {
    "total_in": 35,
    "total_out": 18,
    "total": 17,
    "start_time": "1985-09-11T06:52:54.214Z",
    "end_time": "1985-09-19T02:27:46.828Z"
  },
  {
    "total_in": 88,
    "total_out": 61,
    "total": 27,
    "start_time": "2020-06-06T10:39:30.435Z",
    "end_time": "2020-06-09T01:05:08.480Z"
  },
  {
    "total_in": 38,
    "total_out": 26,
    "total": 12,
    "start_time": "1982-12-20T08:44:57.417Z",
    "end_time": "1982-12-22T12:20:18.166Z"
  },
  {
    "total_in": 93,
    "total_out": 77,
    "total": 16,
    "start_time": "2008-09-02T07:08:59.524Z",
    "end_time": "2008-09-02T17:03:57.443Z"
  },
  {
    "total_in": 73,
    "total_out": 13,
    "total": 60,
    "start_time": "1979-03-12T01:56:47.639Z",
    "end_time": "1979-03-16T14:30:19.151Z"
  },
  {
    "total_in": 24,
    "total_out": 11,
    "total": 13,
    "start_time": "1980-05-03T11:52:36.177Z",
    "end_time": "1980-05-05T18:22:13.858Z"
  },
  {
    "total_in": 34,
    "total_out": 14,
    "total": 20,
    "start_time": "1982-06-11T02:40:35.136Z",
    "end_time": "1982-06-19T06:49:02.397Z"
  },
  {
    "total_in": 79,
    "total_out": 19,
    "total": 60,
    "start_time": "1975-01-01T21:40:07.911Z",
    "end_time": "1975-01-03T13:59:56.666Z"
  },
  {
    "total_in": 49,
    "total_out": 9,
    "total": 40,
    "start_time": "2011-03-04T15:11:53.076Z",
    "end_time": "2011-03-07T22:24:50.662Z"
  },
  {
    "total_in": 23,
    "total_out": 7,
    "total": 16,
    "start_time": "1992-09-29T19:02:18.644Z",
    "end_time": "1992-10-08T15:34:42.162Z"
  },
  {
    "total_in": 93,
    "total_out": 32,
    "total": 61,
    "start_time": "1993-12-31T18:39:12.030Z",
    "end_time": "1994-01-10T05:29:48.511Z"
  },
  {
    "total_in": 47,
    "total_out": 33,
    "total": 14,
    "start_time": "1990-12-12T10:04:44.877Z",
    "end_time": "1990-12-12T22:55:18.079Z"
  },
  {
    "total_in": 38,
    "total_out": 1,
    "total": 37,
    "start_time": "1992-07-12T09:04:42.524Z",
    "end_time": "1992-07-16T04:57:35.598Z"
  },
  {
    "total_in": 86,
    "total_out": 59,
    "total": 27,
    "start_time": "1989-01-26T21:08:31.472Z",
    "end_time": "1989-01-31T23:00:40.507Z"
  },
  {
    "total_in": 79,
    "total_out": 53,
    "total": 26,
    "start_time": "1999-06-28T20:06:44.584Z",
    "end_time": "1999-06-30T17:43:06.167Z"
  },
  {
    "total_in": 11,
    "total_out": 3,
    "total": 8,
    "start_time": "1974-02-23T18:38:00.679Z",
    "end_time": "1974-03-03T23:46:29.676Z"
  },
  {
    "total_in": 27,
    "total_out": 3,
    "total": 24,
    "start_time": "1978-10-13T01:32:15.952Z",
    "end_time": "1978-10-22T14:40:53.578Z"
  },
  {
    "total_in": 20,
    "total_out": 8,
    "total": 12,
    "start_time": "2011-01-13T05:15:31.924Z",
    "end_time": "2011-01-22T15:45:18.084Z"
  },
  {
    "total_in": 88,
    "total_out": 49,
    "total": 39,
    "start_time": "1996-03-26T02:50:13.977Z",
    "end_time": "1996-03-31T00:39:49.262Z"
  },
  {
    "total_in": 61,
    "total_out": 23,
    "total": 38,
    "start_time": "1997-02-21T19:18:39.137Z",
    "end_time": "1997-02-21T20:35:32.043Z"
  },
  {
    "total_in": 90,
    "total_out": 73,
    "total": 17,
    "start_time": "2022-12-02T02:56:28.562Z",
    "end_time": "2022-12-02T21:16:33.991Z"
  },
  {
    "total_in": 33,
    "total_out": 24,
    "total": 9,
    "start_time": "1970-06-25T16:43:35.619Z",
    "end_time": "1970-07-05T10:03:18.949Z"
  },
  {
    "total_in": 44,
    "total_out": 23,
    "total": 21,
    "start_time": "2012-07-07T14:41:47.958Z",
    "end_time": "2012-07-09T09:09:22.290Z"
  },
  {
    "total_in": 15,
    "total_out": 3,
    "total": 12,
    "start_time": "2009-04-20T09:08:25.710Z",
    "end_time": "2009-04-21T15:47:14.228Z"
  },
  {
    "total_in": 41,
    "total_out": 14,
    "total": 27,
    "start_time": "2001-11-22T04:58:05.008Z",
    "end_time": "2001-11-27T05:09:27.801Z"
  },
  {
    "total_in": 67,
    "total_out": 12,
    "total": 55,
    "start_time": "2004-03-17T05:13:37.876Z",
    "end_time": "2004-03-22T14:46:45.531Z"
  },
  {
    "total_in": 31,
    "total_out": 29,
    "total": 2,
    "start_time": "1997-10-28T20:22:41.336Z",
    "end_time": "1997-11-07T06:33:45.365Z"
  },
  {
    "total_in": 75,
    "total_out": 47,
    "total": 28,
    "start_time": "1999-04-28T23:49:05.209Z",
    "end_time": "1999-05-06T04:19:38.443Z"
  },
  {
    "total_in": 48,
    "total_out": 41,
    "total": 7,
    "start_time": "2010-04-10T23:37:51.340Z",
    "end_time": "2010-04-11T19:08:26.879Z"
  },
  {
    "total_in": 95,
    "total_out": 74,
    "total": 21,
    "start_time": "1993-12-06T04:29:15.289Z",
    "end_time": "1993-12-13T10:45:01.238Z"
  },
  {
    "total_in": 63,
    "total_out": 59,
    "total": 4,
    "start_time": "1998-11-23T10:53:17.498Z",
    "end_time": "1998-11-29T14:11:11.299Z"
  },
  {
    "total_in": 32,
    "total_out": 16,
    "total": 16,
    "start_time": "1997-02-02T14:21:10.734Z",
    "end_time": "1997-02-08T12:39:07.224Z"
  },
  {
    "total_in": 16,
    "total_out": 1,
    "total": 15,
    "start_time": "1976-02-17T08:49:14.908Z",
    "end_time": "1976-02-24T23:22:21.897Z"
  },
  {
    "total_in": 91,
    "total_out": 58,
    "total": 33,
    "start_time": "2012-10-04T12:21:01.828Z",
    "end_time": "2012-10-07T22:35:53.935Z"
  },
  {
    "total_in": 31,
    "total_out": 15,
    "total": 16,
    "start_time": "1980-07-23T14:45:49.472Z",
    "end_time": "1980-07-25T14:58:27.515Z"
  },
  {
    "total_in": 76,
    "total_out": 8,
    "total": 68,
    "start_time": "1993-07-18T17:48:42.152Z",
    "end_time": "1993-07-21T20:06:57.188Z"
  },
  {
    "total_in": 85,
    "total_out": 59,
    "total": 26,
    "start_time": "2014-12-11T10:35:24.350Z",
    "end_time": "2014-12-13T09:20:51.067Z"
  },
  {
    "total_in": 54,
    "total_out": 12,
    "total": 42,
    "start_time": "2010-01-24T16:02:37.128Z",
    "end_time": "2010-02-02T11:46:25.182Z"
  },
  {
    "total_in": 90,
    "total_out": 7,
    "total": 83,
    "start_time": "1987-04-24T01:31:05.770Z",
    "end_time": "1987-05-03T07:07:04.254Z"
  },
  {
    "total_in": 22,
    "total_out": 15,
    "total": 7,
    "start_time": "1974-07-21T22:29:42.248Z",
    "end_time": "1974-07-25T00:41:42.347Z"
  },
  {
    "total_in": 31,
    "total_out": 19,
    "total": 12,
    "start_time": "1988-01-23T18:25:42.331Z",
    "end_time": "1988-02-01T06:25:21.968Z"
  },
  {
    "total_in": 46,
    "total_out": 8,
    "total": 38,
    "start_time": "2008-06-11T20:20:35.960Z",
    "end_time": "2008-06-18T01:13:37.950Z"
  },
  {
    "total_in": 50,
    "total_out": 4,
    "total": 46,
    "start_time": "1996-05-07T08:08:06.352Z",
    "end_time": "1996-05-16T02:33:28.391Z"
  },
  {
    "total_in": 47,
    "total_out": 45,
    "total": 2,
    "start_time": "1988-08-16T06:39:17.833Z",
    "end_time": "1988-08-21T16:27:19.615Z"
  },
  {
    "total_in": 46,
    "total_out": 38,
    "total": 8,
    "start_time": "1987-06-22T13:13:09.765Z",
    "end_time": "1987-06-30T03:38:53.810Z"
  },
  {
    "total_in": 71,
    "total_out": 3,
    "total": 68,
    "start_time": "1971-12-17T23:06:59.880Z",
    "end_time": "1971-12-26T04:28:24.023Z"
  },
  {
    "total_in": 67,
    "total_out": 58,
    "total": 9,
    "start_time": "2022-04-14T15:57:06.240Z",
    "end_time": "2022-04-19T12:50:51.534Z"
  },
  {
    "total_in": 87,
    "total_out": 11,
    "total": 76,
    "start_time": "1981-04-25T20:23:18.089Z",
    "end_time": "1981-04-26T17:38:03.659Z"
  },
  {
    "total_in": 30,
    "total_out": 11,
    "total": 19,
    "start_time": "1980-09-01T17:39:02.277Z",
    "end_time": "1980-09-02T05:05:52.480Z"
  },
  {
    "total_in": 9,
    "total_out": 5,
    "total": 4,
    "start_time": "2004-11-10T05:48:09.358Z",
    "end_time": "2004-11-13T19:13:15.192Z"
  },
  {
    "total_in": 89,
    "total_out": 39,
    "total": 50,
    "start_time": "2003-01-07T04:40:39.297Z",
    "end_time": "2003-01-07T15:16:17.165Z"
  },
  {
    "total_in": 82,
    "total_out": 23,
    "total": 59,
    "start_time": "1977-04-25T06:07:42.527Z",
    "end_time": "1977-04-30T22:15:00.616Z"
  },
  {
    "total_in": 37,
    "total_out": 6,
    "total": 31,
    "start_time": "1975-11-09T15:37:05.705Z",
    "end_time": "1975-11-17T03:50:01.987Z"
  },
  {
    "total_in": 61,
    "total_out": 10,
    "total": 51,
    "start_time": "2000-05-08T17:20:00.568Z",
    "end_time": "2000-05-14T08:54:18.467Z"
  },
  {
    "total_in": 20,
    "total_out": 17,
    "total": 3,
    "start_time": "1985-02-05T05:14:59.223Z",
    "end_time": "1985-02-05T16:37:17.842Z"
  },
  {
    "total_in": 6,
    "total_out": 2,
    "total": 4,
    "start_time": "1986-06-29T11:13:51.071Z",
    "end_time": "1986-07-04T10:42:02.339Z"
  },
  {
    "total_in": 87,
    "total_out": 60,
    "total": 27,
    "start_time": "1973-04-26T01:49:27.829Z",
    "end_time": "1973-05-04T10:50:02.154Z"
  },
  {
    "total_in": 77,
    "total_out": 3,
    "total": 74,
    "start_time": "2021-10-12T13:25:19.311Z",
    "end_time": "2021-10-12T20:52:02.067Z"
  },
  {
    "total_in": 46,
    "total_out": 10,
    "total": 36,
    "start_time": "2018-08-26T04:56:24.491Z",
    "end_time": "2018-09-03T12:36:35.635Z"
  },
  {
    "total_in": 91,
    "total_out": 67,
    "total": 24,
    "start_time": "1990-08-11T20:17:21.933Z",
    "end_time": "1990-08-21T16:42:06.249Z"
  },
  {
    "total_in": 25,
    "total_out": 1,
    "total": 24,
    "start_time": "2019-09-08T19:47:59.230Z",
    "end_time": "2019-09-10T17:51:46.474Z"
  },
  {
    "total_in": 86,
    "total_out": 85,
    "total": 1,
    "start_time": "2023-01-28T10:54:48.028Z",
    "end_time": "2023-02-07T02:28:00.168Z"
  },
  {
    "total_in": 95,
    "total_out": 83,
    "total": 12,
    "start_time": "2010-12-22T00:24:02.702Z",
    "end_time": "2010-12-30T09:19:22.508Z"
  },
  {
    "total_in": 38,
    "total_out": 31,
    "total": 7,
    "start_time": "1971-03-10T18:00:35.268Z",
    "end_time": "1971-03-18T13:52:58.255Z"
  },
  {
    "total_in": 84,
    "total_out": 57,
    "total": 27,
    "start_time": "1972-08-14T09:47:02.142Z",
    "end_time": "1972-08-22T08:19:22.816Z"
  },
  {
    "total_in": 46,
    "total_out": 14,
    "total": 32,
    "start_time": "1992-08-18T15:40:18.746Z",
    "end_time": "1992-08-23T20:47:53.268Z"
  },
  {
    "total_in": 14,
    "total_out": 5,
    "total": 9,
    "start_time": "1973-04-11T06:42:10.954Z",
    "end_time": "1973-04-19T08:00:09.702Z"
  },
  {
    "total_in": 45,
    "total_out": 39,
    "total": 6,
    "start_time": "2017-09-09T21:50:55.526Z",
    "end_time": "2017-09-11T10:55:28.197Z"
  },
  {
    "total_in": 2,
    "total_out": 2,
    "total": 0,
    "start_time": "2002-11-15T13:29:44.154Z",
    "end_time": "2002-11-23T21:47:01.867Z"
  },
  {
    "total_in": 23,
    "total_out": 14,
    "total": 9,
    "start_time": "1993-03-27T05:03:29.703Z",
    "end_time": "1993-04-02T01:31:20.797Z"
  },
  {
    "total_in": 65,
    "total_out": 21,
    "total": 44,
    "start_time": "1972-06-05T16:01:27.439Z",
    "end_time": "1972-06-13T17:47:37.708Z"
  },
  {
    "total_in": 69,
    "total_out": 58,
    "total": 11,
    "start_time": "2005-08-08T22:18:35.742Z",
    "end_time": "2005-08-10T12:57:26.669Z"
  },
  {
    "total_in": 23,
    "total_out": 17,
    "total": 6,
    "start_time": "1991-01-13T04:32:55.456Z",
    "end_time": "1991-01-19T11:08:12.294Z"
  },
  {
    "total_in": 77,
    "total_out": 27,
    "total": 50,
    "start_time": "2010-05-25T09:53:08.638Z",
    "end_time": "2010-06-03T01:38:06.928Z"
  },
  {
    "total_in": 28,
    "total_out": 18,
    "total": 10,
    "start_time": "2005-09-16T08:53:41.879Z",
    "end_time": "2005-09-22T00:15:21.657Z"
  },
  {
    "total_in": 67,
    "total_out": 56,
    "total": 11,
    "start_time": "2012-12-27T08:00:29.540Z",
    "end_time": "2013-01-03T03:42:24.390Z"
  },
  {
    "total_in": 63,
    "total_out": 53,
    "total": 10,
    "start_time": "2010-06-27T13:14:50.420Z",
    "end_time": "2010-07-07T04:07:32.961Z"
  },
  {
    "total_in": 10,
    "total_out": 6,
    "total": 4,
    "start_time": "1980-11-15T02:27:30.299Z",
    "end_time": "1980-11-22T06:23:56.821Z"
  },
  {
    "total_in": 56,
    "total_out": 11,
    "total": 45,
    "start_time": "1990-07-06T08:31:12.120Z",
    "end_time": "1990-07-12T20:39:48.625Z"
  },
  {
    "total_in": 43,
    "total_out": 39,
    "total": 4,
    "start_time": "2022-10-11T17:34:23.323Z",
    "end_time": "2022-10-13T06:41:15.155Z"
  },
  {
    "total_in": 66,
    "total_out": 49,
    "total": 17,
    "start_time": "1993-06-04T11:49:52.957Z",
    "end_time": "1993-06-09T00:33:28.667Z"
  },
  {
    "total_in": 41,
    "total_out": 9,
    "total": 32,
    "start_time": "2013-09-05T04:55:57.335Z",
    "end_time": "2013-09-10T17:07:19.074Z"
  },
  {
    "total_in": 95,
    "total_out": 32,
    "total": 63,
    "start_time": "1995-11-24T13:37:33.851Z",
    "end_time": "1995-11-28T23:33:30.144Z"
  },
  {
    "total_in": 21,
    "total_out": 11,
    "total": 10,
    "start_time": "1984-10-17T12:14:30.543Z",
    "end_time": "1984-10-18T02:04:41.167Z"
  },
  {
    "total_in": 32,
    "total_out": 27,
    "total": 5,
    "start_time": "1982-07-18T11:50:19.911Z",
    "end_time": "1982-07-20T21:53:10.566Z"
  },
  {
    "total_in": 5,
    "total_out": 4,
    "total": 1,
    "start_time": "1973-07-11T06:25:48.830Z",
    "end_time": "1973-07-12T16:56:52.292Z"
  },
  {
    "total_in": 3,
    "total_out": 3,
    "total": 0,
    "start_time": "1992-12-05T12:30:10.333Z",
    "end_time": "1992-12-13T19:34:34.641Z"
  },
  {
    "total_in": 28,
    "total_out": 4,
    "total": 24,
    "start_time": "2021-12-29T19:05:52.711Z",
    "end_time": "2022-01-01T18:45:25.421Z"
  },
  {
    "total_in": 12,
    "total_out": 11,
    "total": 1,
    "start_time": "1991-05-06T11:35:38.730Z",
    "end_time": "1991-05-15T06:42:05.055Z"
  },
  {
    "total_in": 32,
    "total_out": 15,
    "total": 17,
    "start_time": "1973-07-20T11:14:30.561Z",
    "end_time": "1973-07-21T04:02:20.146Z"
  },
  {
    "total_in": 2,
    "total_out": 1,
    "total": 1,
    "start_time": "1983-04-30T05:05:32.268Z",
    "end_time": "1983-05-09T12:34:57.426Z"
  },
  {
    "total_in": 100,
    "total_out": 12,
    "total": 88,
    "start_time": "1978-12-08T09:40:11.799Z",
    "end_time": "1978-12-11T21:07:37.087Z"
  },
  {
    "total_in": 41,
    "total_out": 24,
    "total": 17,
    "start_time": "1983-05-08T22:21:30.228Z",
    "end_time": "1983-05-13T22:54:55.903Z"
  },
  {
    "total_in": 97,
    "total_out": 65,
    "total": 32,
    "start_time": "1971-03-31T13:52:46.544Z",
    "end_time": "1971-04-05T23:55:01.862Z"
  },
  {
    "total_in": 10,
    "total_out": 10,
    "total": 0,
    "start_time": "2021-01-25T13:28:25.387Z",
    "end_time": "2021-01-25T21:25:40.360Z"
  },
  {
    "total_in": 26,
    "total_out": 10,
    "total": 16,
    "start_time": "1993-01-04T12:22:14.134Z",
    "end_time": "1993-01-12T13:36:36.530Z"
  },
  {
    "total_in": 98,
    "total_out": 94,
    "total": 4,
    "start_time": "2011-03-08T07:28:03.294Z",
    "end_time": "2011-03-13T20:33:24.519Z"
  },
  {
    "total_in": 91,
    "total_out": 45,
    "total": 46,
    "start_time": "1974-11-05T04:22:29.026Z",
    "end_time": "1974-11-14T11:48:04.665Z"
  },
  {
    "total_in": 69,
    "total_out": 21,
    "total": 48,
    "start_time": "1984-03-06T22:42:23.863Z",
    "end_time": "1984-03-14T16:10:44.147Z"
  },
  {
    "total_in": 82,
    "total_out": 26,
    "total": 56,
    "start_time": "1996-03-13T06:41:14.147Z",
    "end_time": "1996-03-20T04:54:06.517Z"
  },
  {
    "total_in": 41,
    "total_out": 39,
    "total": 2,
    "start_time": "2019-01-18T08:38:27.057Z",
    "end_time": "2019-01-18T14:36:24.780Z"
  },
  {
    "total_in": 34,
    "total_out": 12,
    "total": 22,
    "start_time": "2017-07-17T11:26:48.848Z",
    "end_time": "2017-07-20T15:16:32.345Z"
  },
  {
    "total_in": 85,
    "total_out": 64,
    "total": 21,
    "start_time": "1986-02-15T03:42:05.863Z",
    "end_time": "1986-02-15T09:28:42.050Z"
  },
  {
    "total_in": 41,
    "total_out": 20,
    "total": 21,
    "start_time": "1994-10-05T19:51:10.397Z",
    "end_time": "1994-10-12T00:14:33.386Z"
  },
  {
    "total_in": 12,
    "total_out": 10,
    "total": 2,
    "start_time": "1978-10-25T13:38:20.478Z",
    "end_time": "1978-10-30T00:44:45.020Z"
  },
  {
    "total_in": 98,
    "total_out": 58,
    "total": 40,
    "start_time": "1979-08-19T15:45:13.230Z",
    "end_time": "1979-08-20T09:41:04.189Z"
  },
  {
    "total_in": 34,
    "total_out": 20,
    "total": 14,
    "start_time": "1998-01-06T02:13:09.969Z",
    "end_time": "1998-01-10T07:48:17.244Z"
  },
  {
    "total_in": 2,
    "total_out": 2,
    "total": 0,
    "start_time": "1981-07-16T04:02:02.184Z",
    "end_time": "1981-07-22T13:43:41.888Z"
  },
  {
    "total_in": 80,
    "total_out": 3,
    "total": 77,
    "start_time": "2004-03-28T14:11:32.474Z",
    "end_time": "2004-03-30T12:28:37.709Z"
  },
  {
    "total_in": 16,
    "total_out": 8,
    "total": 8,
    "start_time": "1973-02-10T09:49:24.810Z",
    "end_time": "1973-02-16T18:59:17.992Z"
  },
  {
    "total_in": 47,
    "total_out": 24,
    "total": 23,
    "start_time": "1981-01-25T00:25:03.355Z",
    "end_time": "1981-01-26T10:45:15.451Z"
  },
  {
    "total_in": 50,
    "total_out": 1,
    "total": 49,
    "start_time": "1976-06-22T23:59:17.061Z",
    "end_time": "1976-06-28T12:03:23.549Z"
  },
  {
    "total_in": 61,
    "total_out": 12,
    "total": 49,
    "start_time": "2007-06-10T00:44:52.977Z",
    "end_time": "2007-06-10T12:21:24.511Z"
  },
  {
    "total_in": 77,
    "total_out": 71,
    "total": 6,
    "start_time": "2001-08-08T23:30:49.062Z",
    "end_time": "2001-08-15T10:46:49.526Z"
  },
  {
    "total_in": 26,
    "total_out": 18,
    "total": 8,
    "start_time": "1977-12-07T10:53:57.226Z",
    "end_time": "1977-12-09T04:05:43.041Z"
  },
  {
    "total_in": 69,
    "total_out": 55,
    "total": 14,
    "start_time": "1972-10-21T02:03:24.068Z",
    "end_time": "1972-10-29T04:43:55.161Z"
  },
  {
    "total_in": 67,
    "total_out": 7,
    "total": 60,
    "start_time": "1999-11-06T17:28:20.335Z",
    "end_time": "1999-11-10T17:45:07.828Z"
  },
  {
    "total_in": 96,
    "total_out": 75,
    "total": 21,
    "start_time": "2015-01-07T08:39:15.190Z",
    "end_time": "2015-01-09T04:22:46.706Z"
  },
  {
    "total_in": 74,
    "total_out": 71,
    "total": 3,
    "start_time": "2018-07-06T02:18:14.908Z",
    "end_time": "2018-07-06T15:26:32.503Z"
  },
  {
    "total_in": 31,
    "total_out": 24,
    "total": 7,
    "start_time": "2001-02-03T20:34:50.696Z",
    "end_time": "2001-02-10T02:25:21.515Z"
  },
  {
    "total_in": 48,
    "total_out": 6,
    "total": 42,
    "start_time": "1992-11-30T05:58:38.268Z",
    "end_time": "1992-12-03T15:43:29.776Z"
  },
  {
    "total_in": 10,
    "total_out": 5,
    "total": 5,
    "start_time": "2010-10-25T22:50:36.703Z",
    "end_time": "2010-10-27T21:00:56.844Z"
  },
  {
    "total_in": 54,
    "total_out": 22,
    "total": 32,
    "start_time": "1989-10-27T12:28:58.713Z",
    "end_time": "1989-11-06T11:54:27.526Z"
  },
  {
    "total_in": 66,
    "total_out": 34,
    "total": 32,
    "start_time": "1993-02-09T10:54:54.946Z",
    "end_time": "1993-02-10T05:38:41.406Z"
  },
  {
    "total_in": 26,
    "total_out": 14,
    "total": 12,
    "start_time": "2022-07-28T20:53:13.593Z",
    "end_time": "2022-08-06T14:54:24.210Z"
  },
  {
    "total_in": 81,
    "total_out": 27,
    "total": 54,
    "start_time": "2003-09-25T18:55:13.869Z",
    "end_time": "2003-10-01T17:49:08.967Z"
  },
  {
    "total_in": 24,
    "total_out": 17,
    "total": 7,
    "start_time": "1994-11-10T08:24:04.727Z",
    "end_time": "1994-11-18T21:08:53.594Z"
  },
  {
    "total_in": 57,
    "total_out": 8,
    "total": 49,
    "start_time": "1985-07-21T13:16:00.589Z",
    "end_time": "1985-07-29T09:51:19.374Z"
  },
  {
    "total_in": 7,
    "total_out": 6,
    "total": 1,
    "start_time": "1998-03-13T10:31:17.388Z",
    "end_time": "1998-03-14T00:48:35.169Z"
  },
  {
    "total_in": 58,
    "total_out": 13,
    "total": 45,
    "start_time": "2013-03-15T15:40:39.285Z",
    "end_time": "2013-03-19T23:19:07.513Z"
  },
  {
    "total_in": 26,
    "total_out": 25,
    "total": 1,
    "start_time": "2005-10-13T10:32:53.523Z",
    "end_time": "2005-10-18T05:11:43.241Z"
  },
  {
    "total_in": 54,
    "total_out": 8,
    "total": 46,
    "start_time": "2000-12-20T14:59:33.760Z",
    "end_time": "2000-12-20T21:19:27.442Z"
  },
  {
    "total_in": 28,
    "total_out": 28,
    "total": 0,
    "start_time": "2021-02-16T17:00:11.119Z",
    "end_time": "2021-02-24T01:33:08.640Z"
  },
  {
    "total_in": 10,
    "total_out": 8,
    "total": 2,
    "start_time": "2001-03-11T11:04:48.545Z",
    "end_time": "2001-03-17T12:34:04.997Z"
  },
  {
    "total_in": 17,
    "total_out": 14,
    "total": 3,
    "start_time": "1971-02-26T13:27:13.689Z",
    "end_time": "1971-03-01T14:32:48.695Z"
  },
  {
    "total_in": 86,
    "total_out": 25,
    "total": 61,
    "start_time": "1996-02-25T17:33:23.686Z",
    "end_time": "1996-03-06T02:45:42.049Z"
  },
  {
    "total_in": 62,
    "total_out": 8,
    "total": 54,
    "start_time": "1993-07-25T11:10:05.641Z",
    "end_time": "1993-07-27T10:46:38.360Z"
  },
  {
    "total_in": 61,
    "total_out": 36,
    "total": 25,
    "start_time": "1970-08-10T08:28:50.320Z",
    "end_time": "1970-08-11T23:24:45.387Z"
  },
  {
    "total_in": 39,
    "total_out": 26,
    "total": 13,
    "start_time": "1981-09-19T03:44:12.304Z",
    "end_time": "1981-09-23T02:23:45.847Z"
  },
  {
    "total_in": 75,
    "total_out": 31,
    "total": 44,
    "start_time": "1976-11-09T15:59:53.622Z",
    "end_time": "1976-11-16T17:53:55.432Z"
  },
  {
    "total_in": 47,
    "total_out": 24,
    "total": 23,
    "start_time": "2022-04-18T19:13:43.888Z",
    "end_time": "2022-04-21T04:59:35.790Z"
  },
  {
    "total_in": 28,
    "total_out": 18,
    "total": 10,
    "start_time": "1977-01-19T14:46:32.967Z",
    "end_time": "1977-01-27T22:32:11.886Z"
  },
  {
    "total_in": 9,
    "total_out": 4,
    "total": 5,
    "start_time": "2014-04-27T00:24:48.117Z",
    "end_time": "2014-05-01T07:35:53.781Z"
  },
  {
    "total_in": 70,
    "total_out": 56,
    "total": 14,
    "start_time": "1970-06-04T00:04:05.282Z",
    "end_time": "1970-06-09T10:31:18.083Z"
  },
  {
    "total_in": 54,
    "total_out": 14,
    "total": 40,
    "start_time": "1972-11-08T21:03:49.345Z",
    "end_time": "1972-11-18T08:32:28.329Z"
  },
  {
    "total_in": 8,
    "total_out": 3,
    "total": 5,
    "start_time": "1990-06-16T01:07:02.471Z",
    "end_time": "1990-06-23T12:09:04.117Z"
  },
  {
    "total_in": 63,
    "total_out": 17,
    "total": 46,
    "start_time": "2004-09-09T21:43:07.641Z",
    "end_time": "2004-09-17T22:54:09.007Z"
  },
  {
    "total_in": 63,
    "total_out": 55,
    "total": 8,
    "start_time": "2006-03-03T02:35:30.859Z",
    "end_time": "2006-03-05T07:39:59.168Z"
  },
  {
    "total_in": 68,
    "total_out": 56,
    "total": 12,
    "start_time": "1990-09-10T01:12:45.353Z",
    "end_time": "1990-09-19T07:01:12.387Z"
  },
  {
    "total_in": 84,
    "total_out": 52,
    "total": 32,
    "start_time": "2006-08-04T23:36:54.705Z",
    "end_time": "2006-08-07T21:26:23.246Z"
  },
  {
    "total_in": 87,
    "total_out": 21,
    "total": 66,
    "start_time": "1992-07-10T17:06:50.397Z",
    "end_time": "1992-07-12T13:26:30.228Z"
  },
  {
    "total_in": 33,
    "total_out": 28,
    "total": 5,
    "start_time": "2012-08-26T17:25:54.396Z",
    "end_time": "2012-08-31T19:37:21.234Z"
  },
  {
    "total_in": 26,
    "total_out": 20,
    "total": 6,
    "start_time": "1976-10-13T11:57:33.508Z",
    "end_time": "1976-10-18T20:10:51.199Z"
  },
  {
    "total_in": 12,
    "total_out": 4,
    "total": 8,
    "start_time": "2022-10-22T00:45:45.307Z",
    "end_time": "2022-10-28T02:09:11.813Z"
  },
  {
    "total_in": 51,
    "total_out": 19,
    "total": 32,
    "start_time": "2008-02-22T06:23:15.657Z",
    "end_time": "2008-03-01T01:15:10.382Z"
  },
  {
    "total_in": 51,
    "total_out": 42,
    "total": 9,
    "start_time": "1971-11-16T09:29:24.990Z",
    "end_time": "1971-11-20T03:37:57.885Z"
  },
  {
    "total_in": 97,
    "total_out": 97,
    "total": 0,
    "start_time": "2021-02-28T08:55:36.883Z",
    "end_time": "2021-03-09T20:16:58.258Z"
  },
  {
    "total_in": 89,
    "total_out": 38,
    "total": 51,
    "start_time": "2004-05-13T01:31:29.895Z",
    "end_time": "2004-05-22T12:26:15.463Z"
  },
  {
    "total_in": 20,
    "total_out": 3,
    "total": 17,
    "start_time": "1982-05-18T10:50:47.010Z",
    "end_time": "1982-05-27T02:28:50.488Z"
  },
  {
    "total_in": 73,
    "total_out": 3,
    "total": 70,
    "start_time": "1983-05-23T02:00:37.355Z",
    "end_time": "1983-05-31T13:54:03.405Z"
  },
  {
    "total_in": 4,
    "total_out": 1,
    "total": 3,
    "start_time": "1989-07-20T01:14:01.586Z",
    "end_time": "1989-07-24T07:38:32.042Z"
  },
  {
    "total_in": 85,
    "total_out": 5,
    "total": 80,
    "start_time": "2013-01-09T10:59:41.620Z",
    "end_time": "2013-01-11T21:16:54.168Z"
  },
  {
    "total_in": 64,
    "total_out": 1,
    "total": 63,
    "start_time": "1984-07-30T06:43:25.800Z",
    "end_time": "1984-08-07T09:04:26.591Z"
  },
  {
    "total_in": 79,
    "total_out": 51,
    "total": 28,
    "start_time": "2000-09-05T19:28:35.728Z",
    "end_time": "2000-09-10T00:11:57.840Z"
  },
  {
    "total_in": 19,
    "total_out": 4,
    "total": 15,
    "start_time": "1980-07-22T05:19:49.260Z",
    "end_time": "1980-07-24T15:18:54.486Z"
  },
  {
    "total_in": 88,
    "total_out": 73,
    "total": 15,
    "start_time": "2009-08-24T10:01:22.507Z",
    "end_time": "2009-08-24T12:36:50.356Z"
  },
  {
    "total_in": 45,
    "total_out": 26,
    "total": 19,
    "start_time": "1986-01-06T12:31:24.366Z",
    "end_time": "1986-01-14T00:23:49.470Z"
  },
  {
    "total_in": 27,
    "total_out": 4,
    "total": 23,
    "start_time": "1997-08-22T11:38:42.920Z",
    "end_time": "1997-08-29T22:36:28.990Z"
  },
  {
    "total_in": 87,
    "total_out": 80,
    "total": 7,
    "start_time": "1983-07-23T13:44:11.416Z",
    "end_time": "1983-07-30T11:37:58.831Z"
  },
  {
    "total_in": 65,
    "total_out": 65,
    "total": 0,
    "start_time": "2013-07-10T12:04:31.391Z",
    "end_time": "2013-07-19T05:11:16.010Z"
  },
  {
    "total_in": 35,
    "total_out": 34,
    "total": 1,
    "start_time": "2016-01-09T07:49:12.654Z",
    "end_time": "2016-01-13T13:42:59.275Z"
  },
  {
    "total_in": 73,
    "total_out": 28,
    "total": 45,
    "start_time": "2020-01-25T02:21:30.017Z",
    "end_time": "2020-02-03T12:58:02.609Z"
  },
  {
    "total_in": 5,
    "total_out": 5,
    "total": 0,
    "start_time": "2010-09-08T16:02:43.340Z",
    "end_time": "2010-09-10T05:29:47.114Z"
  },
  {
    "total_in": 89,
    "total_out": 8,
    "total": 81,
    "start_time": "1970-09-12T05:15:54.438Z",
    "end_time": "1970-09-20T07:11:50.271Z"
  },
  {
    "total_in": 85,
    "total_out": 41,
    "total": 44,
    "start_time": "1982-10-05T18:18:09.352Z",
    "end_time": "1982-10-12T16:28:08.014Z"
  },
  {
    "total_in": 43,
    "total_out": 41,
    "total": 2,
    "start_time": "1975-12-26T22:03:16.549Z",
    "end_time": "1975-12-30T17:59:24.032Z"
  },
  {
    "total_in": 82,
    "total_out": 72,
    "total": 10,
    "start_time": "1974-09-08T00:45:24.259Z",
    "end_time": "1974-09-13T14:22:38.727Z"
  },
  {
    "total_in": 23,
    "total_out": 1,
    "total": 22,
    "start_time": "2018-04-04T04:45:21.106Z",
    "end_time": "2018-04-12T19:32:28.304Z"
  },
  {
    "total_in": 90,
    "total_out": 38,
    "total": 52,
    "start_time": "1996-11-13T20:25:34.799Z",
    "end_time": "1996-11-19T23:29:08.325Z"
  },
  {
    "total_in": 31,
    "total_out": 17,
    "total": 14,
    "start_time": "2016-08-06T10:22:19.999Z",
    "end_time": "2016-08-12T23:41:42.756Z"
  },
  {
    "total_in": 16,
    "total_out": 7,
    "total": 9,
    "start_time": "1991-01-02T21:36:34.095Z",
    "end_time": "1991-01-07T09:49:11.928Z"
  },
  {
    "total_in": 94,
    "total_out": 51,
    "total": 43,
    "start_time": "1991-11-27T21:17:13.626Z",
    "end_time": "1991-11-30T16:06:52.753Z"
  },
  {
    "total_in": 8,
    "total_out": 2,
    "total": 6,
    "start_time": "1975-09-21T04:56:51.101Z",
    "end_time": "1975-09-27T04:12:10.905Z"
  },
  {
    "total_in": 43,
    "total_out": 15,
    "total": 28,
    "start_time": "1974-01-29T09:34:08.513Z",
    "end_time": "1974-01-30T18:31:29.465Z"
  },
  {
    "total_in": 68,
    "total_out": 47,
    "total": 21,
    "start_time": "1982-08-30T06:55:08.052Z",
    "end_time": "1982-09-08T20:03:54.606Z"
  },
  {
    "total_in": 75,
    "total_out": 52,
    "total": 23,
    "start_time": "1983-02-01T12:51:07.218Z",
    "end_time": "1983-02-02T03:18:12.215Z"
  },
  {
    "total_in": 63,
    "total_out": 8,
    "total": 55,
    "start_time": "1972-08-27T13:09:20.473Z",
    "end_time": "1972-09-01T12:25:34.396Z"
  },
  {
    "total_in": 51,
    "total_out": 50,
    "total": 1,
    "start_time": "1985-05-14T04:32:09.423Z",
    "end_time": "1985-05-18T07:38:24.645Z"
  },
  {
    "total_in": 11,
    "total_out": 9,
    "total": 2,
    "start_time": "2013-06-03T22:57:40.180Z",
    "end_time": "2013-06-04T03:10:08.074Z"
  },
  {
    "total_in": 14,
    "total_out": 11,
    "total": 3,
    "start_time": "1976-12-12T10:21:13.862Z",
    "end_time": "1976-12-16T16:27:47.836Z"
  },
  {
    "total_in": 2,
    "total_out": 1,
    "total": 1,
    "start_time": "2019-01-02T05:26:40.323Z",
    "end_time": "2019-01-07T13:43:01.858Z"
  },
  {
    "total_in": 21,
    "total_out": 2,
    "total": 19,
    "start_time": "1989-12-04T18:17:34.408Z",
    "end_time": "1989-12-05T03:23:19.700Z"
  },
  {
    "total_in": 100,
    "total_out": 57,
    "total": 43,
    "start_time": "2000-11-24T10:37:52.357Z",
    "end_time": "2000-11-28T19:18:19.061Z"
  },
  {
    "total_in": 73,
    "total_out": 28,
    "total": 45,
    "start_time": "1996-08-16T17:25:18.986Z",
    "end_time": "1996-08-17T04:36:39.302Z"
  },
  {
    "total_in": 59,
    "total_out": 42,
    "total": 17,
    "start_time": "1989-03-28T06:33:17.665Z",
    "end_time": "1989-04-04T20:16:01.734Z"
  },
  {
    "total_in": 87,
    "total_out": 24,
    "total": 63,
    "start_time": "2004-11-06T10:38:19.593Z",
    "end_time": "2004-11-14T07:57:12.594Z"
  },
  {
    "total_in": 96,
    "total_out": 73,
    "total": 23,
    "start_time": "1971-01-29T23:37:31.756Z",
    "end_time": "1971-02-02T13:20:19.907Z"
  },
  {
    "total_in": 28,
    "total_out": 17,
    "total": 11,
    "start_time": "1984-06-02T04:04:06.539Z",
    "end_time": "1984-06-10T10:26:20.082Z"
  },
  {
    "total_in": 93,
    "total_out": 37,
    "total": 56,
    "start_time": "2002-04-25T12:48:56.700Z",
    "end_time": "2002-05-04T17:28:57.633Z"
  },
  {
    "total_in": 99,
    "total_out": 6,
    "total": 93,
    "start_time": "2007-05-24T15:24:19.653Z",
    "end_time": "2007-05-30T15:32:53.540Z"
  },
  {
    "total_in": 32,
    "total_out": 2,
    "total": 30,
    "start_time": "1993-08-19T04:00:08.308Z",
    "end_time": "1993-08-19T13:02:28.246Z"
  },
  {
    "total_in": 81,
    "total_out": 76,
    "total": 5,
    "start_time": "1988-08-05T14:39:29.635Z",
    "end_time": "1988-08-06T17:02:52.637Z"
  },
  {
    "total_in": 14,
    "total_out": 11,
    "total": 3,
    "start_time": "2011-12-17T18:16:47.841Z",
    "end_time": "2011-12-24T22:12:21.908Z"
  },
  {
    "total_in": 79,
    "total_out": 54,
    "total": 25,
    "start_time": "1992-02-23T07:47:01.476Z",
    "end_time": "1992-02-29T16:46:43.224Z"
  },
  {
    "total_in": 76,
    "total_out": 41,
    "total": 35,
    "start_time": "1999-11-05T16:58:24.038Z",
    "end_time": "1999-11-14T23:43:00.565Z"
  },
  {
    "total_in": 58,
    "total_out": 20,
    "total": 38,
    "start_time": "2001-12-10T05:43:21.883Z",
    "end_time": "2001-12-12T12:52:28.346Z"
  },
  {
    "total_in": 39,
    "total_out": 6,
    "total": 33,
    "start_time": "2005-01-10T18:26:34.934Z",
    "end_time": "2005-01-11T07:21:56.185Z"
  },
  {
    "total_in": 43,
    "total_out": 26,
    "total": 17,
    "start_time": "1988-09-10T23:25:53.085Z",
    "end_time": "1988-09-16T01:11:45.646Z"
  },
  {
    "total_in": 88,
    "total_out": 52,
    "total": 36,
    "start_time": "1972-12-26T14:38:02.896Z",
    "end_time": "1972-12-26T21:04:04.577Z"
  },
  {
    "total_in": 71,
    "total_out": 21,
    "total": 50,
    "start_time": "2022-04-30T17:32:51.265Z",
    "end_time": "2022-05-05T21:22:13.619Z"
  },
  {
    "total_in": 15,
    "total_out": 4,
    "total": 11,
    "start_time": "2013-05-24T05:09:01.821Z",
    "end_time": "2013-05-29T23:26:29.178Z"
  },
  {
    "total_in": 37,
    "total_out": 10,
    "total": 27,
    "start_time": "2004-03-24T03:27:17.000Z",
    "end_time": "2004-03-26T15:31:25.802Z"
  },
  {
    "total_in": 18,
    "total_out": 5,
    "total": 13,
    "start_time": "2023-06-13T08:06:00.947Z",
    "end_time": "2023-06-18T06:02:10.007Z"
  },
  {
    "total_in": 54,
    "total_out": 52,
    "total": 2,
    "start_time": "2012-06-26T18:44:59.980Z",
    "end_time": "2012-06-27T05:41:18.160Z"
  },
  {
    "total_in": 63,
    "total_out": 12,
    "total": 51,
    "start_time": "2006-05-21T01:10:55.314Z",
    "end_time": "2006-05-23T14:11:56.209Z"
  },
  {
    "total_in": 28,
    "total_out": 9,
    "total": 19,
    "start_time": "2023-10-15T19:49:41.158Z",
    "end_time": "2023-10-17T06:28:16.161Z"
  },
  {
    "total_in": 46,
    "total_out": 41,
    "total": 5,
    "start_time": "1981-10-05T19:43:30.417Z",
    "end_time": "1981-10-07T18:59:25.489Z"
  },
  {
    "total_in": 74,
    "total_out": 65,
    "total": 9,
    "start_time": "1988-11-07T09:34:34.407Z",
    "end_time": "1988-11-13T01:47:26.837Z"
  },
  {
    "total_in": 21,
    "total_out": 6,
    "total": 15,
    "start_time": "2003-02-10T17:50:16.503Z",
    "end_time": "2003-02-16T13:44:06.808Z"
  },
  {
    "total_in": 57,
    "total_out": 14,
    "total": 43,
    "start_time": "1979-02-18T10:22:20.337Z",
    "end_time": "1979-02-24T22:38:31.442Z"
  },
  {
    "total_in": 35,
    "total_out": 5,
    "total": 30,
    "start_time": "2004-06-23T01:42:21.982Z",
    "end_time": "2004-06-29T20:36:22.948Z"
  },
  {
    "total_in": 77,
    "total_out": 32,
    "total": 45,
    "start_time": "2015-10-01T12:37:53.444Z",
    "end_time": "2015-10-07T16:42:21.981Z"
  },
  {
    "total_in": 81,
    "total_out": 24,
    "total": 57,
    "start_time": "1984-06-26T06:54:44.718Z",
    "end_time": "1984-07-04T10:17:45.582Z"
  },
  {
    "total_in": 26,
    "total_out": 8,
    "total": 18,
    "start_time": "1996-01-05T16:52:06.877Z",
    "end_time": "1996-01-08T20:10:25.891Z"
  },
  {
    "total_in": 77,
    "total_out": 39,
    "total": 38,
    "start_time": "1982-05-24T09:36:00.092Z",
    "end_time": "1982-05-31T20:57:13.086Z"
  },
  {
    "total_in": 42,
    "total_out": 15,
    "total": 27,
    "start_time": "1991-03-13T13:29:34.607Z",
    "end_time": "1991-03-15T13:32:53.437Z"
  },
  {
    "total_in": 39,
    "total_out": 14,
    "total": 25,
    "start_time": "1970-04-16T04:51:07.960Z",
    "end_time": "1970-04-24T18:29:15.744Z"
  },
  {
    "total_in": 47,
    "total_out": 6,
    "total": 41,
    "start_time": "2006-12-26T05:14:58.432Z",
    "end_time": "2007-01-02T03:56:36.566Z"
  },
  {
    "total_in": 7,
    "total_out": 2,
    "total": 5,
    "start_time": "1985-07-04T15:04:57.819Z",
    "end_time": "1985-07-09T16:32:24.579Z"
  },
  {
    "total_in": 11,
    "total_out": 1,
    "total": 10,
    "start_time": "1988-09-27T13:29:48.345Z",
    "end_time": "1988-10-04T09:15:43.512Z"
  },
  {
    "total_in": 20,
    "total_out": 13,
    "total": 7,
    "start_time": "1979-04-09T08:08:05.031Z",
    "end_time": "1979-04-14T00:45:49.318Z"
  },
  {
    "total_in": 50,
    "total_out": 35,
    "total": 15,
    "start_time": "2017-01-17T04:06:38.117Z",
    "end_time": "2017-01-20T21:52:15.228Z"
  },
  {
    "total_in": 79,
    "total_out": 49,
    "total": 30,
    "start_time": "2023-02-18T19:31:45.511Z",
    "end_time": "2023-02-21T03:04:43.154Z"
  },
  {
    "total_in": 55,
    "total_out": 24,
    "total": 31,
    "start_time": "2007-11-27T03:16:28.929Z",
    "end_time": "2007-12-04T09:34:57.338Z"
  },
  {
    "total_in": 4,
    "total_out": 1,
    "total": 3,
    "start_time": "1977-07-25T16:37:59.979Z",
    "end_time": "1977-07-27T22:45:31.967Z"
  },
  {
    "total_in": 28,
    "total_out": 21,
    "total": 7,
    "start_time": "2015-02-27T03:34:51.896Z",
    "end_time": "2015-03-08T13:53:05.010Z"
  },
  {
    "total_in": 1,
    "total_out": 1,
    "total": 0,
    "start_time": "2021-12-29T00:42:40.813Z",
    "end_time": "2021-12-30T07:03:16.946Z"
  },
  {
    "total_in": 63,
    "total_out": 52,
    "total": 11,
    "start_time": "2010-04-07T09:37:10.710Z",
    "end_time": "2010-04-17T06:21:20.478Z"
  },
  {
    "total_in": 18,
    "total_out": 17,
    "total": 1,
    "start_time": "2016-07-05T01:08:42.431Z",
    "end_time": "2016-07-08T02:23:42.680Z"
  },
  {
    "total_in": 20,
    "total_out": 2,
    "total": 18,
    "start_time": "2005-04-03T21:43:02.384Z",
    "end_time": "2005-04-08T03:10:50.519Z"
  },
  {
    "total_in": 87,
    "total_out": 9,
    "total": 78,
    "start_time": "2021-05-01T11:57:20.953Z",
    "end_time": "2021-05-07T12:25:20.794Z"
  },
  {
    "total_in": 66,
    "total_out": 29,
    "total": 37,
    "start_time": "2013-04-08T10:08:52.254Z",
    "end_time": "2013-04-11T05:08:36.108Z"
  },
  {
    "total_in": 21,
    "total_out": 11,
    "total": 10,
    "start_time": "1994-10-20T23:06:38.013Z",
    "end_time": "1994-10-26T18:06:59.358Z"
  },
  {
    "total_in": 22,
    "total_out": 16,
    "total": 6,
    "start_time": "2000-08-10T19:41:58.253Z",
    "end_time": "2000-08-12T02:14:20.991Z"
  },
  {
    "total_in": 71,
    "total_out": 61,
    "total": 10,
    "start_time": "2006-12-29T09:39:52.290Z",
    "end_time": "2007-01-04T08:15:36.600Z"
  },
  {
    "total_in": 98,
    "total_out": 64,
    "total": 34,
    "start_time": "2012-08-22T03:08:25.707Z",
    "end_time": "2012-08-29T14:30:11.227Z"
  },
  {
    "total_in": 76,
    "total_out": 76,
    "total": 0,
    "start_time": "2005-10-17T21:09:41.212Z",
    "end_time": "2005-10-18T08:39:06.421Z"
  },
  {
    "total_in": 99,
    "total_out": 26,
    "total": 73,
    "start_time": "2005-04-19T05:40:03.201Z",
    "end_time": "2005-04-24T07:04:12.454Z"
  },
  {
    "total_in": 84,
    "total_out": 76,
    "total": 8,
    "start_time": "2010-04-08T15:22:27.422Z",
    "end_time": "2010-04-13T08:57:43.271Z"
  },
  {
    "total_in": 74,
    "total_out": 24,
    "total": 50,
    "start_time": "1978-07-31T16:27:50.766Z",
    "end_time": "1978-08-07T08:24:23.688Z"
  },
  {
    "total_in": 68,
    "total_out": 27,
    "total": 41,
    "start_time": "1989-10-16T12:53:18.211Z",
    "end_time": "1989-10-23T18:38:17.578Z"
  },
  {
    "total_in": 33,
    "total_out": 20,
    "total": 13,
    "start_time": "2017-07-12T08:54:54.393Z",
    "end_time": "2017-07-16T15:52:18.781Z"
  },
  {
    "total_in": 8,
    "total_out": 8,
    "total": 0,
    "start_time": "1974-07-26T20:26:18.435Z",
    "end_time": "1974-07-28T17:47:33.617Z"
  },
  {
    "total_in": 79,
    "total_out": 21,
    "total": 58,
    "start_time": "1985-04-12T12:35:43.210Z",
    "end_time": "1985-04-18T12:18:12.721Z"
  },
  {
    "total_in": 69,
    "total_out": 42,
    "total": 27,
    "start_time": "1970-11-02T12:22:21.179Z",
    "end_time": "1970-11-10T19:09:24.703Z"
  },
  {
    "total_in": 19,
    "total_out": 2,
    "total": 17,
    "start_time": "1988-05-16T23:21:55.835Z",
    "end_time": "1988-05-20T16:08:52.817Z"
  },
  {
    "total_in": 49,
    "total_out": 12,
    "total": 37,
    "start_time": "1996-11-30T17:34:50.138Z",
    "end_time": "1996-12-06T04:15:04.945Z"
  },
  {
    "total_in": 43,
    "total_out": 34,
    "total": 9,
    "start_time": "1992-03-06T01:34:24.241Z",
    "end_time": "1992-03-09T04:15:55.982Z"
  },
  {
    "total_in": 44,
    "total_out": 13,
    "total": 31,
    "start_time": "1995-06-14T04:15:36.038Z",
    "end_time": "1995-06-18T18:29:25.328Z"
  },
  {
    "total_in": 75,
    "total_out": 30,
    "total": 45,
    "start_time": "2013-05-21T04:01:12.525Z",
    "end_time": "2013-05-28T03:05:48.457Z"
  },
  {
    "total_in": 92,
    "total_out": 41,
    "total": 51,
    "start_time": "2012-06-01T21:17:01.556Z",
    "end_time": "2012-06-03T21:23:44.889Z"
  },
  {
    "total_in": 42,
    "total_out": 22,
    "total": 20,
    "start_time": "1991-03-03T08:18:04.003Z",
    "end_time": "1991-03-08T21:27:48.044Z"
  },
  {
    "total_in": 8,
    "total_out": 4,
    "total": 4,
    "start_time": "1971-02-08T08:12:17.138Z",
    "end_time": "1971-02-11T05:53:33.835Z"
  },
  {
    "total_in": 88,
    "total_out": 64,
    "total": 24,
    "start_time": "1999-07-16T14:50:59.547Z",
    "end_time": "1999-07-23T06:28:40.823Z"
  },
  {
    "total_in": 42,
    "total_out": 1,
    "total": 41,
    "start_time": "1987-01-31T11:47:26.618Z",
    "end_time": "1987-02-01T00:03:12.949Z"
  },
  {
    "total_in": 86,
    "total_out": 42,
    "total": 44,
    "start_time": "2016-12-02T10:48:37.971Z",
    "end_time": "2016-12-11T03:40:07.725Z"
  },
  {
    "total_in": 5,
    "total_out": 3,
    "total": 2,
    "start_time": "2008-07-22T15:45:39.801Z",
    "end_time": "2008-07-26T22:59:36.789Z"
  }
]



        for dummy_data in dummy_data_list:
            # Randomly select a camera from the available cameras
            random_camera = random.choice(all_cameras)

            # Use the selected camera's data for the dummy data
            dummy_data["camera"] = random_camera.id
            dummy_data["sn"] = random_camera.sn

            # Create a CounterHistory instance
            counter_history_serializer = CreateCounterHistorySerializer(data=dummy_data)
            counter_history_serializer.is_valid(raise_exception=True)
            counter_history_serializer.save()

        self.stdout.write(self.style.SUCCESS('Successfully posted dummy camera data to the database'))
