from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select



class AdvancedSearchPage:
    advanced_search_label_id = 'search-title'
    select_language_drop_box_id = 'search_language'
    with_so_many_stars_input_id = 'search_stars'
    with_license_drop_box_id = 'search_license'
    with_this_many_followers_id = 'search_followers'
    button_search_xpath = '//*[@id="search_form"]/div[2]/div/div/button'

    def __init__(self, driver):
        self.driver = driver

    def get_advanced_search_label(self):
        return self.driver.find_element_by_id(self.advanced_search_label_id).text

    def select_language(self, language):
        Select(self.driver.find_element_by_id(self.select_language_drop_box_id)).select_by_value(language)

    def set_stars(self, stars_criteria):
        self.driver.find_element_by_id(self.with_so_many_stars_input_id).send_keys(stars_criteria)

    def select_licence(self, licence):
        Select(self.driver.find_element_by_id(self.with_license_drop_box_id)).select_by_index(licence)

    def set_followers(self, followers_criteria):
        self.driver.find_element_by_id(self.with_this_many_followers_id).send_keys(followers_criteria)

    def click_button_search(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()
