import allure
from selene import browser

from data.links import *
from pages.main_page import MainPage
from pages.erin_recommends_page import *

@allure.suite("US_001.002 | Testing Erin Recommends Page")
class TestErinRecommends:
    @allure.title("TC_001.002.002 | Check redirection to 'Shop Erin Recommends' page by clicking block")
    def test_erin_block_link_redirection(self, browser_management):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Assert Erin recommends block presence"):
            link = page.is_erin_block_present()
        with allure.step("Click on Erin recommends block"):
            link.click()
        page = ErinRecommendsPage(browser=browser)
        with allure.step("Assert current url == Erin Recommends Page url"):
            assert page.check_current_url() == ERIN_RECOMMENDS_URL
        with allure.step("Find header"):
            header = page.is_header_present()
        with allure.step("Assert header contains text 'Erin Recommends'"):
            page.is_element_text_correct(header, "Erin Recommends")
