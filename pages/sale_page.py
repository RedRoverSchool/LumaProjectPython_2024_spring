from selene import have
from data.links import SALE_PAGE_URL
from pages.base_page import BasePage


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
