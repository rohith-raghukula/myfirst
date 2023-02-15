from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Initialize the Chrome browser with the headless options and the path to the Chrome driver
browser = webdriver.Chrome('/path/to/chromedriver', options=chrome_options)

# Navigate to the website login page
browser.get('https://profile.w3schools.com/')

# Find the email and password fields and enter the login credentials
wait = WebDriverWait(browser, 10)
email_field = wait.until(EC.presence_of_element_located((By.ID, 'modalusername')))
email_field.send_keys('rohithr9701@gmail.com')

password_field = wait.until(EC.presence_of_element_located((By.ID, 'current-password')))
password_field.send_keys('Rohith@123')

# Submit the login form
password_field.submit()

# Wait for the dashboard page to load
wait.until(EC.url_contains('dashboard'))

# Verify that the user is logged in and perform other actions on the dashboard page
# ...

# Close the browser
browser.quit()
