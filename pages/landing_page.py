from selenium.webdriver.common.by import By
import time

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def load_page(self, url):
        self.driver.get(url)
        time.sleep(3)  # Replace with WebDriverWait ideally

    def get_flight_html(self):
        return self.driver.page_source