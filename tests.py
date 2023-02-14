from selenium import webdriver
class TestGoogleSearch():
    @classmethod
    def setup_class(cls):
        # Create a new Chrome browser instance
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
  
# Navigate to the website
browser.get('https://app.stezy.in/login')

# Find the form fields and fill them in
name_field = browser.find_element_by_name('username')
name_field.send_keys('John Doe')
email_field = browser.find_element_by_name('password')
email_field.send_keys('johndoe@example.com')


# Submit the form
submit_button = browser.find_element_by_css_selector('button[type="submit"]')
submit_button.click()

# Wait for the response page to load
browser.implicitly_wait(10)



# Close the browser
browser.quit()
