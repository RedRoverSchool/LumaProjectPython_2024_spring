from selene import have, be, Element
from selene.core import command
from selene.support.shared.jquery_style import s

from pages.components.mini_card import MiniCard
from pages.components.nav_wigdet import NavComponent
from pages.locators import BaseLocators


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent()
        self.mini_card = MiniCard()

    def visit(self, url):
        return self.browser.open(url)

    def assert_text_of_element(self, locator, expected_text):
        s(locator).should(have.text(expected_text))

    def assert_visible_of_element(self, locator):
        s(locator).should(be.visible)

    def assert_present_of_element(self, locator):
        s(locator).should(be.present)

    def get_current_url(self):
        return self.browser.driver.current_url

    @staticmethod
    def is_visible_success_message():
        message = s(BaseLocators.SUCCESS_MESSAGE)
        message.should(be.visible)
        message.should(have.text('You added')).should(have.text('to your shopping cart'))

    @staticmethod
    def scroll_to(element: Element):
        element.perform(command.js.scroll_into_view)
