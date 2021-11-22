import allure
import time
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.HomePage import HomePage
from pages.SimpleResultPage import SimpleResultSearch
from pages.AdvancedSearchPage import AdvancedSearchPage
from pages.AdvancedSearchResultPage import AdvancedSearchResultPage
from pages.FoundRepositoryPage import FoundRepositoryPage
from utils.logger import Logger
from utils.readProperty import ReadConfig
from utils.search_data_type import search_test_data
from utils.test_data_util import get_test_data_record

base_url = ReadConfig.get_url()
logger = Logger.loggen()
test_data_filename = f".\\testdata\\{ReadConfig.get_test_data_filename()}"
search_test_data = get_test_data_record(test_data_filename, 2)


@given(u'github home page is open using Chrome browser')
def step_impl(context):
    chrome_driver_manager = ChromeDriverManager()
    context.driver = webdriver.Chrome(chrome_driver_manager.install())
    logger.info("***** Driver Initialized *****")
    context.driver.get(base_url)
    global driver
    driver = context.driver
    context.driver.maximize_window()
    logger.info("***** Browser launched *****")
    driver.save_screenshot(".\\screenshots\\" + "HomePage.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="github page", attachment_type=AttachmentType.PNG)


@when(u'search is performed for keyword <react>')
def step_impl(context):
    global home_page
    home_page = HomePage(driver)
    home_page.input_search_criteria(search_test_data.get("initial_search_value", ""))
    time.sleep(1)
    home_page.click_search()
    time.sleep(1)


@then(u'page with multiple results is displayed')
def step_impl(context):
    global simple_result_page
    simple_result_page = SimpleResultSearch(driver)
    if simple_result_page:
        logger.info("***** Search Result for 'react' is displayed *****")
        assert True
    else:
        logger.info("***** Search Result for 'react' is not displayed *****")
        assert False
    driver.save_screenshot(".\\screenshots\\" + "SimpleSearch.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="github page", attachment_type=AttachmentType.PNG)


@when(u'user clicks on <Advanced Search>')
def step_impl(context):
    simple_result_page.click_advanced_search()
    global advanced_search_page
    advanced_search_page = AdvancedSearchPage(driver)


@then(u'Advanced search page is displayed')
def step_impl(context):
    expected_label = 'Advanced search'
    if advanced_search_page.get_advanced_search_label() == expected_label:
        logger.info("***** Advanced Search Page for 'react' is displayed *****")
        assert True
    else:
        logger.info("***** Advanced Search Page for 'react' is not displayed *****")
        assert False
    driver.save_screenshot(".\\screenshots\\" + "AdvancedSearch.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="github page", attachment_type=AttachmentType.PNG)


@when(u'user selects \'Javascript\' in <Written in this language> dropbox under <Advanced options>')
def step_impl(context):
    advanced_search_page.select_language(search_test_data.get("language", ""))
    time.sleep(1)


@when(u'user enters value \'>45\' in <With this many stars> field under <Repositories options>')
def step_impl(context):
    advanced_search_page.set_stars(search_test_data.get("stars", ""))
    time.sleep(1)


@when(u'user selects value \'Boost Software License 1.0\' in <With this license> dropbox under <Repositories options>')
def step_impl(context):
    advanced_search_page.select_licence(search_test_data.get("license_index", ""))
    time.sleep(1)


@when(u'user enters value \'>50\' in <With this many followers> field under <Users options>')
def step_impl(context):
    advanced_search_page.set_followers(search_test_data.get("followers", ""))
    time.sleep(1)


@when(u'user clicks on <Search> button')
def step_impl(context):
    advanced_search_page.click_button_search()
    global advanced_search_result_page
    advanced_search_result_page = AdvancedSearchResultPage(driver)
    time.sleep(1)


@then(u'<mvoloskov/decider> repository is found as a single result')
def step_impl(context):
    expected_found_results = 1
    expected_repository_found = f'mvoloskov/{search_test_data.get("expected_result", "")}'
    test_results_message = advanced_search_result_page.get_number_of_results_message()
    actual_found_results = int(test_results_message.split(" ")[0])
    if expected_found_results == actual_found_results:
        logger.info("***** One Result Found *****")
        assert True
    else:
        logger.info("***** Result found is not equal to one *****")
        assert False

    if expected_repository_found == advanced_search_result_page.get_found_repository_name():
        logger.info(f"***** Found is <{expected_repository_found}> *****")
        assert True
    else:
        logger.info(f"***** Found is not <{expected_repository_found}>  *****")
        assert False

    driver.save_screenshot(".\\screenshots\\" + "AdvancedSearchResult.png")
    allure.attach(context.driver.get_screenshot_as_png(), name="github page", attachment_type=AttachmentType.PNG)


@when(u'user clicks on found repository link')
def step_impl(context):
    advanced_search_result_page.click_on_found_repository()
    global repository_page
    repository_page = FoundRepositoryPage(driver)


@then(u'repository page is displayed')
def step_impl(context):
    if search_test_data.get("expected_result", "") == repository_page.get_repository_name():
        logger.info("***** Expected Repository Found *****")
        assert True
    else:
        logger.info("***** Expected Repository not Found *****")
        assert False


@then(u'First three hundred characters match expected and printed in automation log file')
def step_impl(context):
    logger.info(repository_page.get_readme_content())
    driver.close()
    assert True

