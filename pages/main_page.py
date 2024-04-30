from selene.support.shared.jquery_style import s
from data.links import MAIN_PAGE_LINK
from pages.locators import BaseLocators as BL


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(MAIN_PAGE_LINK)

    @property
    def privacy_cookie_policy_link(self):
        return s(BL.PRIVACY_COOKIE_POLICY_LOCATOR)

    def scroll_to_privacy_cookie_policy_link(self):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.privacy_cookie_policy_link())
