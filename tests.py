from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# Set any desired options on the ChromeOptions object
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver_path = '/path/to/chromedriver'  # Update this with the path to your chromedriver executable
# Specify the version of ChromeDriver to use
driver_version = '92.0.4515.43'

# Create a new ChromeOptions object
chrome_options = webdriver.ChromeOptions()



# Create a new ChromeDriver instance with the specified options and executable path
browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Initialize the Chrome browser with the headless options
#browser = webdriver.Chrome(options=chrome_options)

# Navigate to the YouTube website
browser.get('https://www.youtube.com/')

# Find the search bar element and enter a search query
search_bar = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'search_query')))
search_bar.send_keys('Python programming')
search_bar.submit()

# Wait for the search results page to load
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'search')))

# Verify that the search results contain relevant videos
# ...

# Close the browser
print("end of the code ..")
browser.quit()
