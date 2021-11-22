from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class AdvancedSearchResultPage:
    results_found_xpath = '//*[@id="js-pjax-container"]/div/div[3]/div/div[2]/h3'
    found_repository_xpath = '//*[@id="js-pjax-container"]/div/div[3]/div/ul/li/div[2]/div[1]/div[1]/a'

    def __init__(self, driver):
        self.driver = driver

    def get_number_of_results_message(self):
        return self.driver.find_element_by_xpath(self.results_found_xpath).text

    def get_found_repository_name(self):
        return self.driver.find_element_by_xpath(self.found_repository_xpath).text

    def click_on_found_repository(self):
        self.driver.find_element_by_xpath(self.found_repository_xpath).click()
