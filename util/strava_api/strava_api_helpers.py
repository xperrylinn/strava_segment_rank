from stravaio import strava_oauth2
import time
from collections import defaultdict
from config import (
    api_call_limit_rate
)


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


def compute_athlete_segment_frequency(client, start_date, end_date):
    """

    Get's all user activites after an epoch time stamp and computes the
    number of times each segment was created and returns the result as
    a dict

    :param client: stravaio client
    :param start_date: epoch timestamp. gets activites after start_date
    :type start_date: int
    :param end_date: epoch timestamp. gets activites on and before end_date
    :type end_date: int
    :return: dict,
        keys:
            segment_id --> int
    """

    list_activities = client.get_logged_in_athlete_activities(after=start_date)
    list_activities_by_id = [summary_activity.id for summary_activity in list_activities]

    wait_time = api_call_limit_rate / 60.0 * (1 + 0.5)  # add a 50% time buffer

    detailed_activities = []
    for activity_id in list_activities_by_id:
        time.sleep(wait_time)
        print('Getting activity_id ', str(activity_id), 'detailed activity.')
        detailed_activity = client.get_activity_by_id(activity_id)
        detailed_activities.append(detailed_activity)

    segment_frequencies = defaultdict(int)
    for detailed_activity in detailed_activities:
        for detailed_segment_effort in detailed_activity.api_response.segment_efforts:
            segment = detailed_segment_effort.segment
            segment_frequencies[segment.id] += 1

    return segment_frequencies
