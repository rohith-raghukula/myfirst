from selenium import webdriver

class TestYouTubeSearch():
    @classmethod
    def setup_class(cls):
        # Create a new Chrome browser instance
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        # Close the browser
        cls.driver.quit()

    def test_youtube_search(self):
        # Navigate to the YouTube homepage
        self.driver.get("https://www.youtube.com")

        # Find the search input element and enter a search query
        search_box = self.driver.find_element_by_name("search_query")
        search_box.send_keys("python selenium tutorial")
        search_box.submit()

        # Assert that the search results page was loaded successfully
        assert "python selenium tutorial - YouTube" in self.driver.title
