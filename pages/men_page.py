from data.links import MEN_PAGE_URL
from selene.support.conditions import have
from selene.support.shared.jquery_style import s

from data.page_data import MenPageData
from pages.base_page import BasePage
from pages.locators import NavigatorLocators as Nav
from pages.locators import BaseLocators as Header
from selenium.webdriver.support.color import Color


class MenPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.open_page()

    def open_page(self):
        self.visit(MEN_PAGE_URL)

    def is_loaded(self):
        s(Header.PAGE_HEADER).should(have.text("Men"))
        is_current_page_men = self.get_current_url() == MEN_PAGE_URL
        assert is_current_page_men, MenPageData.error_message

    @staticmethod
    def is_active():
        underline = Color.from_string('#ff5501').rgb
        font = Color.from_string('#333').rgba
        assert s(Nav.NAV_MEN).should(have.css_property('color').value(font))
        assert s(Nav.NAV_MEN).should(have.css_property('border-color').value(underline))
