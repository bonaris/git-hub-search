from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class FoundRepositoryPage:
    repository_name_xpath = '//*[@id="repository-container-header"]/div[1]/div/h1/strong/a'
    readme_text_box_xpath = '//*[@id="readme"]/div[3]/article/p[1]'
    readme_text_box_second_xpath = '//*[@id="readme"]/div[3]/article/div[1]/pre'

    def __init__(self, driver):
        self.driver = driver

    def get_repository_name(self):
        return self.driver.find_element_by_xpath(self.repository_name_xpath).text

    def get_readme_content(self):
        full_readme_content = self.driver.find_element_by_xpath(self.readme_text_box_xpath).text + '\n'
        full_readme_content += self.driver.find_element_by_xpath(self.readme_text_box_second_xpath).text
        return full_readme_content[0:300]

