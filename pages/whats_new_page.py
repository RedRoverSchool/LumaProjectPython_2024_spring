from selene import browser
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from pages.locators import WhatsNewPageLocators as WNL


class WhatsNewPage:
    def __init__(self, browser):
        self.browser = browser

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def is_header_present(self):
        return s(WNL.HEADER).should(be.present)

    def is_lumas_latest_present(self):
        return s(WNL.LUMAS_LATEST_LIST).should(be.present)

    def get_lumas_latest_items(self):
        return s(WNL.LUMAS_LATEST_ITEMS)

    def check_current_url(self):
        return browser.driver.current_url
