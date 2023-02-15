from selenium import webdriver
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Open the app.stezy.io website
driver.get("https://app.stezy.io/")

# Find the email field element and enter the email address
email_field = driver.find_element_by_name("usernamee")
email_field.send_keys("example@email.com")

# Find the password field element and enter the password
password_field = driver.find_element_by_name("password")
password_field.send_keys("examplepassword")

# Find the sign in button and click it
signin_button = driver.find_element_by_css_selector(".sc-fznKkj.ljqwJN")
signin_button.click()

# Wait for the dashboard page to load
time.sleep(5)

# Verify that the user is logged in and the dashboard page is displayed
assert "Dashboard" in driver.title

# Close the browser
driver.quit()
