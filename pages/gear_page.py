from data.links import GEAR_PAGE_URL
from pages.base_page import BasePage


class GearPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_page(self):
        self.visit(GEAR_PAGE_URL)


