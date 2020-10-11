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

outputs:

| segment_id | frequency | total_entries | viewer_rank | read_date                  |
|------------|-----------|---------------|-------------|----------------------------|
| 1543168    | 1         | 285           | 22          | 2020-10-11 14:19:33.114967 |
| 6898591    | 1         | 408           | 3           | 2020-10-11 14:19:39.786555 |
| 20152485   | 1         | 1491          | 25          | 2020-10-11 14:19:46.426210 |
| 12524369   | 1         | 624           | 18          | 2020-10-11 14:19:52.618972 |
| 3883214    | 1         | 890           | 31          | 2020-10-11 14:19:58.928299 |
| 4267302    | 1         | 1371          | 129         | 2020-10-11 14:20:06.090870 |
| 2465427    | 4         | 1645          | 29          | 2020-10-11 14:20:12.714838 |
| 5458504    | 4         | 1551          | 112         | 2020-10-11 14:20:18.890575 |
| 668180     | 1         | 1795          | 400         | 2020-10-11 14:20:25.482631 |
| 15159613   | 1         | 1359          | 360         | 2020-10-11 14:20:32.139382 |
| 7331572    | 1         | 2345          | 406         | 2020-10-11 14:20:38.329158 |
| 1506641    | 1         | 1551          | 465         | 2020-10-11 14:20:44.637802 |
| 7475165    | 1         | 3174          | 414         | 2020-10-11 14:20:50.770559 |

