import allure
from selene import browser

from pages.whats_new_page import WhatsNewPage


@allure.suite("US_006.007 | What`s new page > New Luma Yoga Collection")
class TestYoga:
    @allure.link("https://trello.com/c/G7Iz9eaQ")
    @allure.title("TC_006.007.001 | The New Luma Yoga Collection link and Shop New Yoga button links"
                  " are displayed on the What's New page")
    def test_new_luma_yoga_collection_link_visibility(self, browser_management):
            page = WhatsNewPage(browser=browser)
            page.open_page()
            page.is_yoga_link_visible()
            page.is_button_visible()