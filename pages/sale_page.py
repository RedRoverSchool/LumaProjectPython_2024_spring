from selene import have
from selene.support.shared.jquery_style import ss

from data.links import SALE_PAGE_URL
from pages.base_page import BasePage
from pages.locators import SalePageLocators as SPL, BaseLocators as BL
from selene import browser, have
from selene.support.shared.jquery_style import s, ss


def visit():
    browser.open(SPL.LINK_WOMEN_SALE)


def check_if_breadcrumbs_have_all_parts():
    ss(BL.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale'))


class SalePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_page(self):
        self.visit(SALE_PAGE_URL)

    def check_page_title(self):
        self.assert_text_of_element("h1.page-title", 'Sale')

    def redirect(self):
        self.browser.should(have.url(SALE_PAGE_URL))
