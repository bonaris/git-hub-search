from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HomePage:
    search_box_xpath = "/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]"
    search_button_path = '//*[@id="jump-to-suggestion-search-global"]/a/div[3]/span[2]'

    def __init__(self, driver):
        self.driver = driver

    def input_search_criteria(self, searchValue):
        self.driver.find_element_by_xpath(self.search_box_xpath).send_keys(searchValue)

    def click_search(self):
        self.driver.find_element_by_xpath(self.search_button_path).click()
