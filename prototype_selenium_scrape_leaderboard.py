from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os

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

driver.get("https://www.strava.com/segments/902554?filter=overall")
print('driver.current_url: ', driver.current_url)

element = driver.find_element_by_id('segment-leaderboard')

print(element)

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

for element in elements:
    print(element)
elements.clear()

driver.close()
