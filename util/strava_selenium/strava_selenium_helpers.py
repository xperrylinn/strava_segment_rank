import datetime
import json
import time

# Constants and Params
strava_login_url = 'https://www.strava.com/login'
strava_segment_leaderboard_url = lambda x: ('https://www.strava.com/segments/' + x + '?filter=overall')
strava_login_button_xml = '//*[@type="submit"]'
strava_leaderboard_data_div_xml = '//div[@data-tracking]'


def strava_login(driver, login_url, username, password):
    """

    :param driver: selenium driver
    :param username: strava username
    :param password: strava password
    :return: None
    """

    driver.get(login_url)

    username_element = driver.find_element_by_id("email")
    password_element = driver.find_element_by_id("password")

    username_element.send_keys(username)
    password_element.send_keys(password)

    login_attempt = driver.find_element_by_xpath(strava_login_button_xml)
    login_attempt.submit()

    return


def strava_scrape_segment_leaderboard(driver, segment_id, segment_leaderboard_url):
    """

    :param segment_id: strava segment id
    :param segment_leaderboard_url: lambda fxn that accepts url as param
    :return: dict,
        keys:
            viewer_rank -> int,
            total_entries -> int,
            segment_id -> int,
            read_date -> datetime
    """

    driver.get(segment_leaderboard_url(segment_id))

    time.sleep(5)

    element = driver.find_element_by_xpath(strava_leaderboard_data_div_xml)

    data = json.loads(element.get_attribute('data-tracking'))

    data = {
        'segment_id': segment_id,
        'total_entries': data['leaderboard_state']['total_entries'],
        'viewer_rank': data['viewer_rank'],
        'read_date': datetime.datetime.now()
    }

    return data
