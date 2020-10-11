from util.strava_api.strava_api_helpers import compute_athlete_segment_frequency
from util.strava_selenium.strava_selenium_helpers import strava_scrape_segment_leaderboard
from util.strava_selenium.strava_selenium_helpers import strava_login
from util.strava_api.authenticate import authenticate
from stravaio import StravaIO
from selenium import webdriver
import os
import pandas


strava_login_url = 'https://www.strava.com/login'
strava_segment_leaderboard_url = lambda x: ('https://www.strava.com/segments/' + str(x) + '?filter=overall')
strava_login_button_xml = '//*[@type="submit"]'
strava_leaderboard_data_div_xml = '//div[@data-tracking]'

driver = webdriver.Chrome('../chromedriver')

strava_login(
    driver,
    strava_login_url,
    os.environ['STRAVA_USERNAME'],
    os.environ['STRAVA_PASSWORD']
)

client = StravaIO(
    access_token=authenticate(
        os.environ['STRAVA_CLIENT_ID'],
        os.environ['STRAVA_CLIENT_SECRET']
    )
)

segment_frequencies = compute_athlete_segment_frequency(client, 1600211729)

segment_frequencies_df = pandas.DataFrame(
    {
    'segment_id': segment_frequencies.keys(),
    'frequency': segment_frequencies.values()
    }
)

segment_leadboard_datas = []
for segment_id, frequency in segment_frequencies.items():
    print('Scrapping segment ', str(segment_id))
    segment_leaderboard_data = strava_scrape_segment_leaderboard(
        driver,
        segment_id,
        strava_segment_leaderboard_url
    )
    segment_leadboard_datas.append(segment_leaderboard_data)

segment_leaderboard_df = pandas.DataFrame(segment_leadboard_datas)

final_table = segment_frequencies_df.merge(
    segment_leaderboard_df,
    left_on='segment_id',
    right_on='segment_id'
)

print(final_table.to_string())
