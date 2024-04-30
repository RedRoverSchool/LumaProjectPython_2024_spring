import allure
from selene import browser
from selene.support.conditions import have, be

from pages.main_page import MainPage
from data.page_data import MainPageData


@allure.feature("Footer > Privacy and Cookie Policy")
class TestPrivacyAndCookiePolicy:
    @allure.title("TC_012.006.001 | Verify visibility of the 'Privacy and Cookie Policy' link")
    def test_visibility_privacy_and_cookie_policy(self):
        main_page = MainPage(browser=browser)
        main_page.open_page()
        main_page.scroll_to_privacy_cookie_policy_link()

        main_page.privacy_cookie_policy_link.should(be.visible)
        main_page.privacy_cookie_policy_link.should(
            have.text(MainPageData.privacy_cookie_policy_link_text)
        )
