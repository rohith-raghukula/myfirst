import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestStezyLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new Chrome browser instance
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

    def test_stezy_login(self):
        # Navigate to the app.stezy.io homepage
        self.driver.get("https://app.stezy.io")

        # Find the email and password input fields and enter login credentials
        email_input = self.driver.find_element(By.NAME, "username")
        email_input.send_keys("rohit@stezy.io")

        password_input = self.driver.find_element(By.NAME, "Password")
        password_input.send_keys("Stezy@123")

        # Find the login button and click it
        login_button = self.driver.find_element(By.NAME, "LogIn")
        login_button.click()

        print("hi")
        time.sleep(10)

        # Check if login was successful
        self.assertIn("dashboard", self.driver.current_url, "Login failed")
        
        if __name__ == '__main__':
    unittest.main()
