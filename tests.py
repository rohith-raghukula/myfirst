from selenium import webdriver


# Initialize the Chrome browser
browser = webdriver.Chrome()

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
