from selene import browser, by, be
from selene.support.shared.jquery_style import s
from pages.locators import PrivacyPolicyPageLocators as PPPL


def open_page_with_navigate_block(url):
    browser.open(url)


def move_to_elements(text_data):
    elements = []
    for i in text_data:
        element = s(by.link_text(i))
        element.hover()
        element.should(be.existing)
        elements.append(element)
    return elements


class PrivacyPolicyPage:

    def __init__(self, browser):
        self.browser = browser

    @property
    def get_privacy_policy_url(self):
        return self.browser.driver.current_url

    @property
    def page_main_header(self):
        return s(PPPL.PAGE_MAIN_HEADER_LOCATOR)
