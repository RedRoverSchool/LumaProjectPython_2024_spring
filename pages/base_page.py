from selene import have, be
from selene.support.shared.jquery_style import s

from pages.components.nav_wigdet import NavComponent


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent(browser)

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
