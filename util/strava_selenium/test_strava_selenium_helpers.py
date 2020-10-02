import os
from util.strava_selenium.strava_selenium_helpers import strava_login
from util.strava_selenium.strava_selenium_helpers import strava_scrape_segment_leaderboard
from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome('../../chromedriver')
strava_login_url = 'https://www.strava.com/login'
strava_segment_leaderboard_url = lambda x: 'https://www.strava.com/segments/' + x + '?filter=overall'
strava_login_button_xml = '//*[@type="submit"]'
strava_leaderboard_data_div_xml = '//div[@data-tracking]'


def test_strava_login():
    strava_login(
        driver,
        strava_login_url,
        os.environ['STRAVA_USERNAME'],
        os.environ['STRAVA_PASSWORD']
    )
    return


def test_strava_scrape_segment_leaderboard():

    strava_segment_id = '6659598'
    strava_leaderboard_url_lambda = \
        lambda x: 'https://www.strava.com/segments/' + \
                  x + '?filter=overall'

    leaderboard_data = strava_scrape_segment_leaderboard(
        driver,
        strava_segment_id,
        strava_leaderboard_url_lambda
    )

    assert leaderboard_data['segment_id'] == strava_segment_id

    return leaderboard_data


def test_scrape_data():
    test_strava_login()
    time.sleep(2) # Need to give time for javascript to load (or something like that)
    print(test_strava_scrape_segment_leaderboard())


if __name__ == '__main__':
    try:
        test_scrape_data()
    finally:
        driver.close()
