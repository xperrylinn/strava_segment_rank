from util.strava_api.strava_api_helpers import authenticate
from util.strava_api.strava_api_helpers import compute_athlete_segment_frequency
import os
from stravaio import StravaIO


client = StravaIO(
    access_token=authenticate(
        os.environ['STRAVA_CLIENT_ID'],
        os.environ['STRAVA_CLIENT_SECRET']
    )
)


def test_compute_athlete_segment_frequency():
    print(compute_athlete_segment_frequency(client, 0))
    return


if __name__ == '__main__':
    print('Hello World!')
    test_compute_athlete_segment_frequency()
