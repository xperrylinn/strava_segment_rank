from stravaio import strava_oauth2


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
    strava_client_id = '49662'
    strava_client_secret = '5c7f82b7b67b632f7ab558ec290081915fa56962'
    access_token = authenticate(
        strava_client_id,
        strava_client_secret
    )
    print(access_token)
