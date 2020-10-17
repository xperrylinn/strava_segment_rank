from strava_segment_rank.util.strava_api.strava_api_helpers import compute_athlete_segment_frequency
from strava_segment_rank.util.strava_selenium.strava_selenium_helpers import strava_scrape_segment_leaderboard
from strava_segment_rank.util.strava_selenium.strava_selenium_helpers import strava_login
from strava_segment_rank.util.strava_api.strava_api_helpers import authenticate
from config import (
    strava_login_url,
    strava_segment_leaderboard_url,
)
from stravaio import StravaIO
from selenium import webdriver
import os
import pandas
import datetime


def strava_segment_rank(start_date, end_date, top_k):
    """

    :param start_date: MM/DD/YYYY
    :type start_date: str
    :param end_date: MM/DD/YYYY
    :type end_date: str
    :param top_k: top k attempted segments
    :type top_k: int
    :return: Pandas DataFrame
    """
    driver = webdriver.Chrome(os.environ['CHROMEDRIVER_PATH'])
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

    start_date = datetime.datetime(
        int(start_date.split('/')[2]),
        int(start_date.split('/')[0]),
        int(start_date.split('/')[1]),
    ).timestamp()

    end_date = datetime.datetime(
        int(end_date.split('/')[2]),
        int(end_date.split('/')[0]),
        int(end_date.split('/')[1]),
    ).timestamp()

    segment_frequencies = compute_athlete_segment_frequency(client, int(start_date), int(end_date))

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

    driver.close()

    return final_table


if __name__ == '__main__':
    print('Hello World!')
    df = strava_segment_rank('10/8/2020', '10/10/2020', 10)
    print(df.to_string(index=False))
    df.to_csv('./output_table_example.csv', index=False)
