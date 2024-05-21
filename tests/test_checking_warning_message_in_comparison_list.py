import time
import allure
from selene import browser
from pages.locators import ComparisonListLocators as CompListLocators
from pages.comparison_list import has_success_message

from pages.whats_new_page import WhatsNewPage

@allure.link('https://trello.com/c/ojlwLkH0')
@allure.suite("US_013.001|Compare products > From any catalog's page")
@allure.feature("TC_013.001.001|Compare products > From any catalog's page > Checking the warning message that a product has been added to the comparison list")
def test_if_item_was_added_in_comparison_list():
    page = WhatsNewPage(browser=browser)
    page.open_page()
    
    # Find first item card in Luma section
    with allure.step("Click 'Add to Compare' button"):
        page.get_lumas_latest_items()[0].hover().s(CompListLocators.ADD_TO_COMPARE_LIST).click()

    # Checks that the message string appears
    with allure.step("Checks of the warning message appears"):
        has_success_message()


