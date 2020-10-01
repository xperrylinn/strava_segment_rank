from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import time

driver = webdriver.Chrome('./chromedriver')

# wait = WebDriverWait(driver, 5)

# Authenticate user
driver.get('https://www.strava.com/login')
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("password")
username.send_keys(os.environ['STRAVA_USERNAME'])
password.send_keys(os.environ['STRAVA_PASSWORD'])

login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

time.sleep(5)

driver.get("https://www.strava.com/segments/902554?filter=overall")
print('driver.current_url: ', driver.current_url)

# element = driver.find_element_by_id('segment-results')
element = driver.find_element_by_xpath('//div[@data-tracking]')

print(element.get_attribute('data-tracking'))

# try:
#     elements = wait.until(
#         expected_conditions.presence_of_element_located(
#             (
#                 By.ID,
#                 'segment-leaderboard'
#             )
#         ),
#     )
# finally:
#     driver.close()

driver.close()
