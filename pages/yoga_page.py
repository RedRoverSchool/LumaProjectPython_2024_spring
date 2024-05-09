from selene import browser, command, Element
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss

from data.links import YOGA_URL, YOGA_LIST_URL
from pages.locators import WhatsNewPageLocators as WNL, YogaPageLocators as YPL


class YogaPage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(YOGA_URL)

    def is_list_button_visible(self):
        return s(YPL.LIST_BUTTON).should(be.visible)

    def list_button_click(self):
        return s(YPL.LIST_BUTTON).click()

    def check_current_url(self):
        return browser.driver.current_url

    def open_list_view_page(self):
        self.browser.open(YOGA_LIST_URL)

    def is_grid_button_visible(self):
        return s(YPL.GRID_BUTTON).should(be.visible)

    def grid_button_click(self):
        return s(YPL.GRID_BUTTON).click()
