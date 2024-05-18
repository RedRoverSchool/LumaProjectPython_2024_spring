from data.links import GEAR_PAGE_URL
from pages.base_page import BasePage

class GearPage(BasePage):

    def open_page(self):
        self.visit(GEAR_PAGE_URL)
