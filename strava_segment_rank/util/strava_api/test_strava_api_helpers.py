from strava_segment_rank.util.strava_api import authenticate
from strava_segment_rank.util.strava_api import compute_athlete_segment_frequency
import os
from stravaio import StravaIO


client = StravaIO(
    access_token=authenticate(
        os.environ['STRAVA_CLIENT_ID'],
        os.environ['STRAVA_CLIENT_SECRET']
    )
)


def test_compute_athlete_segment_frequency():
    print(compute_athlete_segment_frequency(client, 1600211729))
    return


if __name__ == '__main__':
    print('Hello World!')
    test_compute_athlete_segment_frequency()
