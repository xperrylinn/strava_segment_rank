"""
    Configuration file for constants/parameters
"""
from selenium import webdriver

# Selenium
strava_login_url = 'https://www.strava.com/login'
strava_segment_leaderboard_url = lambda x: ('https://www.strava.com/segments/' + str(x) + '?filter=overall')
strava_login_button_xml = '//*[@type="submit"]'
strava_leaderboard_data_div_xml = '//div[@data-tracking]'
driver = webdriver.Chrome('../chromedriver')

# Strava API
api_call_limit_rate = 100.0 / 15.0    # calls per min imposed by Strava API
