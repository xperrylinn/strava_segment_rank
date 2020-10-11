# strava_segment_rank

Strava segment rank is a Python module for scarping Strava segment leaderboard data. 

Using the Strava API and Selenium, the module outputs a table of an athlete's rank on 
a subset of attempted segments.

Segment subsets may be determined through the following parameters:
- start_date - start date to mark collecting attempted segments from
- end_date - end to date to collect attempted segment up until
- top k attempt count - select on the top k number of attempts segments

Requirements:
- Strava account with summit membership
- Strava developer account
- Google Chrome
- ChromeDriver (for Selenium)
- See requirements.txt for required Python modules

Environment Variables:
- STRAVA_CLIENT_SECRET - from Strava developer account
- STRAVA_CLIENT_ID - from Strava developer account
- STRAVA_USERNAME - username for Strava account
- STRAVA_PASSWORD - password for Strava account 
- CHROMEDRIVER_PATH - path to ChromeDriver

Usage:

`strava_segment_rank('10/8/2020', '10/10/2020', 10)` in strava_segment_rank.py --> dataframe

`print(dataframe.to_string())` 

-->

| segment_id | frequency | total_entries | viewer_rank | read_date                      |
|------------|-----------|---------------|-------------|--------------------------------|
| 0          | 1543168   | 1             | 285         | 22 2020-10-11 13:34:33.103041  |
| 1          | 6898591   | 1             | 408         | 3 2020-10-11 13:34:39.887113   |
| 2          | 20152485  | 1             | 1491        | 25 2020-10-11 13:34:46.897710  |
| 3          | 12524369  | 1             | 624         | 18 2020-10-11 13:34:53.996905  |
| 4          | 3883214   | 1             | 890         | 31 2020-10-11 13:35:00.377438  |
| 5          | 4267302   | 1             | 1371        | 129 2020-10-11 13:35:07.083325 |
| 6          | 2465427   | 4             | 1645        | 29 2020-10-11 13:35:13.897077  |
| 7          | 5458504   | 4             | 1551        | 112 2020-10-11 13:35:20.867946 |
| 8          | 668180    | 1             | 1794        | 400 2020-10-11 13:35:27.041816 |
| 9          | 15159613  | 1             | 1359        | 360 2020-10-11 13:35:33.905752 |
| 10         | 7331572   | 1             | 2344        | 406 2020-10-11 13:35:40.863978 |
