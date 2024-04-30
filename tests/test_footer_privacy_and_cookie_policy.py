from selene import browser
from selene.support.conditions import have, be

from pages.main_page import MainPage
from data.page_data import MainPageData


class TestPrivacyAndCookiePolicy:
    def test_visibility_privacy_and_cookie_policy(self):
        main_page = MainPage(browser=browser)
        main_page.open_page()
        main_page.scroll_to_privacy_cookie_policy_link()

        main_page.privacy_cookie_policy_link.should(be.visible)
        main_page.privacy_cookie_policy_link.should(have.text(MainPageData.privacy_cookie_policy_link_text))
