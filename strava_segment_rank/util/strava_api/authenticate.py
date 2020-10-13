from stravaio import strava_oauth2
import os


def authenticate(strava_client_id, strava_client_secret):
    """
    :param strava_client_id:
    :param strava_client_secret:
    :return:
    """
    response = strava_oauth2(
        client_id=strava_client_id,
        client_secret=strava_client_secret
    )
    access_token = response['access_token']

    return access_token


if __name__ == '__main__':
    strava_client_id = os.environ['STRAVA_CLIENT_ID']
    strava_client_secret = os.environ['STRAVA_CLIENT_SECRET']
    access_token = authenticate(
        strava_client_id,
        strava_client_secret
    )
    print(access_token)
