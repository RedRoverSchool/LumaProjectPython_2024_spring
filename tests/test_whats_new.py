import allure
from selene import browser

from data.links import WHATS_NEW_PAGE_LINK
from pages.main_page import MainPage
from pages.whats_new_page import WhatsNewPage


@allure.suite("US_006.006 | Testing What's New Page")
class TestWhatsNew:
    @allure.title("TC_006.006.001 | Test visibility of What's New link on the home page")
    def test_whats_new_link_visibility(self, browser_management):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Assert home page menu presence"):
            page.is_menu_present()
        with allure.step("Assert there is the What's New link in the menu"):
            page.is_whats_new_link_present()

    @allure.title("TC_006.006.002 | Check redirection to What's New page by clicking a link")
    def test_redirection_to_whats_new_page(self, browser_management):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Find What's New link in  the menu"):
            link = page.find_whats_new_link()
        with allure.step("Click on What's New link"):
            link.click()
        page = WhatsNewPage(browser=browser)
        with allure.step("Assert current url == What's New Page url"):
            assert page.check_current_url() == WHATS_NEW_PAGE_LINK
        with allure.step("Find header"):
            header = page.is_header_present()
        with allure.step("Assert header contains text \'What's New\'"):
            page.is_element_text_correct(header, "What's New")
