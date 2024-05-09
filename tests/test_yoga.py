import allure
from selene import browser, be, by, have
from selene.support.shared.jquery_style import s
from pages.whats_new_page import WhatsNewPage
from pages.yoga_page import YogaPage
from pages.locators import WhatsNewPageLocators as WNL, YogaPageLocators as YPL
from data.links import YOGA_URL, YOGA_LIST_URL


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

    @allure.link("https://trello.com/c/jqrXmRkR")
    @allure.title("TC_006.007.002| What`s new page > New Luma Yoga Collection > "
                  "The \"New Luma Yoga Collection\" link redirects to New Luma Yoga Collection page")
    def test_yoga_link_redirection(self, browser_management):
        page = WhatsNewPage(browser=browser)
        page.open_page()
        page.new_yoga_link_click()
        assert page.check_current_url() == YOGA_URL
        assert s(YPL.PAGE_TITLE).should(have.text('New Luma Yoga Collection'))

    @allure.link("https://trello.com/c/oTH09O30")
    @allure.title("TC_006.007.003| What`s new page > New Luma Yoga Collection "
                  "> The \"Shop New Yoga\" button link redirects to New Luma Yoga Collection page")
    def test_yoga_button_redirection(self, browser_management):
        page = WhatsNewPage(browser=browser)
        page.open_page()
        page.click_button_shop_new_yoga()
        assert page.check_current_url() == YOGA_URL
        assert s(YPL.PAGE_TITLE).should(have.text('New Luma Yoga Collection'))

    @allure.link("https://trello.com/c/jRy1WrCH")
    @allure.title("TC_006.007.004| What`s new page > New Luma Yoga Collection > "
                  "The \"List\" button is displayed and changes a page view type")
    def test_yoga_list_button_visibility_and_redirection(self, browser_management):
        page = YogaPage(browser=browser)
        page.open_page()
        page.is_list_button_visible()
        page.list_button_click()
        assert page.check_current_url() == YOGA_LIST_URL
        assert s(YPL.WRAPPER_LIST_VIEW).should(be.visible)