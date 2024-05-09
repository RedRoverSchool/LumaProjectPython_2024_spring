from selene import have, browser
from selene.support.shared.jquery_style import s


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def visit(self, url):
        return self.browser.open(url)

    def assert_text_of_element(self, locator, expected_text):
        s(locator).should(have.text(expected_text))
