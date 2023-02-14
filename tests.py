from selenium import webdriver

class TestGoogleSearch():
    @classmethod
    def setup_class(cls):
        # Create a new Chrome browser instance
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        # Close the browser
        cls.driver.quit()

    browser.get('https://profile.w3schools.com/')

      # Close the browser
browser.quit()
