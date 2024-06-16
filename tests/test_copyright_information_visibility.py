import pytest
import allure
import data.links as l
from pages.copyright_info import scroll_to, is_copyright_info_visible
from selene import browser

links = [l.base_url,
         l.gear_bags_url,
         l.sale_page_url,
         l.whats_new_page_link,
         l.TRAINING_PAGE_URL,
         ]

footer = "small[class='copyright']"


# @pytest.mark.skip

@allure.feature("Footer > Self > Copyright>visibility")
@allure.title("Copyright information visibility")
@allure.link("https://trello.com/c/AmBznN3p")
@pytest.mark.parametrize('links', links)
def test_copyright_information_visibility(links):
    with allure.step("Navigate to the home page"):
        browser.open(links)
    with allure.step("Scroll down to the footer section"):
        scroll_to(browser)
    with allure.step("Find the copyright information"):
        is_copyright_info_visible(footer)
