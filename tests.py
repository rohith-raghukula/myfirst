from selenium import webdriver

# Create a new Chrome browser instance
browser = webdriver.Chrome()
cls.driver.implicitly_wait(10)


# Navigate to the website
browser.get('https://example.com')

# Find the form fields and fill them in
name_field = browser.find_element_by_name('name')
name_field.send_keys('John Doe')
email_field = browser.find_element_by_name('email')
email_field.send_keys('johndoe@example.com')
message_field = browser.find_element_by_name('message')
message_field.send_keys('This is a test message')

# Submit the form
submit_button = browser.find_element_by_css_selector('button[type="submit"]')
submit_button.click()

# Wait for the response page to load
browser.implicitly_wait(10)

# Verify that the response page contains a success message
assert 'Thank you for your message' in browser.page_source

# Close the browser
browser.quit()
