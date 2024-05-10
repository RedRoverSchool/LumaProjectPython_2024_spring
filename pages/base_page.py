from selene import have, be
from selene.support.shared.jquery_style import s


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def visit(self, url):
        return self.browser.open(url)

    def assert_text_of_element(self, locator, expected_text):
        s(locator).should(have.text(expected_text))

    def assert_visible_of_element(self, locator):
        s(locator).should(be.visible)

