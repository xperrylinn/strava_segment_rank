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

`strava_segment_rank(start_date, end_date, top_k)` in strava_segment_rank.py
