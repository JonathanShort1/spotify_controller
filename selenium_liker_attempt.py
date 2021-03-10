from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import config
# Spotify URL
SPOTIFY_URL = "https://open.spotify.com/collection/playlists"

# Using Chrome to access the web
driver = webdriver.Safari()
driver.implicitly_wait(10)

# Open the website
driver.get(SPOTIFY_URL)

time.sleep(5)

#Login Procedure
wait = WebDriverWait(driver, 10)
login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[2]")))
#login=driver.find_element_by_xpath("//button[@data-testid='login-button']")
print(login.get_attribute('data-testid'))
login.click()
sleep(1)
email=driver.find_element_by_id('login-username').send_keys(config.EMAIL)
password=driver.find_element_by_id('login-password').send_keys(config.PASSWORD)
login=driver.find_element_by_id('login-button').click()

# Close driver
driver.close()