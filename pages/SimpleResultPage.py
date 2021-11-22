from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SimpleResultSearch:
    advanced_search_link = '//*[@id="js-pjax-container"]/div/div[2]/div[4]/a'

    def __init__(self, driver):
        self.driver = driver

    def click_advanced_search(self):
        self.driver.find_element_by_xpath(self.advanced_search_link).click()

    def is_advanced_search_available(self):
        if self.driver.find_element_by_xpath(self.advanced_search_link):
            return True
        else:
            return False

