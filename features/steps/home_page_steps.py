import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.HomePage import HomePage
from pages.SimpleResultPage import SimpleResultSearch
from utils.logger import Logger
from utils.readProperty import ReadConfig
import time

base_url = ReadConfig.get_url()
logger = Logger.loggen()


@given(u'Launch the browser and navigate to Github web site')
def step_impl(context):
    chrome_driver_manager = ChromeDriverManager()
    context.driver = webdriver.Chrome(chrome_driver_manager.install())
    logger.info("***** Driver Initialized *****")
    context.driver.get(base_url)
    global driver
    driver = context.driver
    context.driver.maximize_window()
    logger.info("***** Browser launched *****")


@then(u'verify the page title')
def step_impl(context):
    actual_title = context.driver.title
    expected_title = 'GitHub: Where the world builds software'
    logger.info(f"\nActual title: {actual_title[0:39]} \nExpected title: {expected_title}")
    if actual_title[0:39] == expected_title:
        assert True
        logger.info("**** Title Matched ****")
        time.sleep(2)
    else:
        logger.error("**** Title not Matched ****")
        assert False
        time.sleep(2)


@given(u'GitHub Search Page is open')
def step_impl(context):
    global home_page
    home_page = HomePage(driver)
    home_page.input_search_criteria('react')
    time.sleep(2)


@when(u'search for value <react>')
def step_impl(context):
    home_page.click_search()
    time.sleep(2)
    global simple_result_page
    simple_result_page = SimpleResultSearch(driver)
    simple_result_page.click_advanced_search()


@then(u'expected result page is displayed')
def step_impl(context):
    time.sleep(2)
    driver.close()
    assert True

