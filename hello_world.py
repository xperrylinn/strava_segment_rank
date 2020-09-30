from authenticate import authenticate
from stravaio import StravaIO
import datetime
import time
from collections import defaultdict
from swagger_client.api.segment_efforts_api import SegmentEffortsApi
import swagger_client

strava_client_id = '49662'
strava_client_secret = '5c7f82b7b67b632f7ab558ec290081915fa56962'

strava_access_token = '43b7d1b82edd7fdd6c48ca3af3b9023eaf1a4b21'
# strava_access_token = authenticate(
#     strava_client_id,
#     strava_client_secret
# )

client = StravaIO(access_token=strava_access_token)

list_activities = client.get_logged_in_athlete_activities(after=0)
list_activities_by_id = [summary_activity.id for summary_activity in list_activities]

total_num_activities = len(list_activities_by_id)
api_call_rate = 15.0 / 100.0    # units: API Calls per min
wait_time_in_min = total_num_activities * api_call_rate
wait_time_in_sec = wait_time_in_min / 60.0
approximate_time_per_get_activty_api_call_in_sec = 0.7
total_time_per_get_activity_api_call_in_sec = wait_time_in_sec + approximate_time_per_get_activty_api_call_in_sec + 10.0

detailed_activities = []
segment_frequencies = defaultdict(int)
for activity_id in list_activities_by_id:
    before_time = datetime.datetime.now()
    detailed_activity = client.get_activity_by_id(activity_id)
    after_time = datetime.datetime.now()
    delta_time = after_time - before_time
    print(delta_time)

    detailed_activities.append(detailed_activity)

    for detailed_segment_effort in detailed_activity.api_response.segment_efforts:
        segment = detailed_segment_effort.segment
        segment_frequencies[segment.id] += 1

    print(segment_frequencies)

    time.sleep(total_time_per_get_activity_api_call_in_sec)

segment_frequencies_items = segment_frequencies.items()
segment_frequencies_items_sorted = sorted(list(segment_frequencies_items), key=lambda x: x[1])
top_10_segment_frequencies_items = segment_frequencies_items_sorted

for item in top_10_segment_frequencies_items:
    print(item)

configuration = swagger_client.Configuration()
configuration.access_token = strava_access_token
segment_efforts_api = swagger_client.SegmentEffortsApi(swagger_client.ApiClient(configuration))

for item in top_10_segment_frequencies_items:
    segment_id = item[0]
    detailed_segment_efforts = segment_efforts_api.get_efforts_by_segment_id(segment_id)
    top_effort_segment_effort_kom_rank = detailed_segment_efforts[0].kom_rank
    top_effort_segment_effort_segment_name = detailed_segment_efforts[0].segment.name
    print(top_effort_segment_effort_kom_rank, top_effort_segment_effort_segment_name)

print(detailed_activities[0])
