import allure
from selene import browser
from selene.support.conditions import have, be

from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from data.page_data import MainPageData
from data.page_data import PrivacyPolicyPageData as PPPD
from data.links import PRIVACY_POLICY_PAGE_LINK


@allure.feature("Footer > Privacy and Cookie Policy > Redirect, Clickability, Visibility")
class TestPrivacyAndCookiePolicy:

    @allure.title("TC_012.006.001 | Verify visibility of the 'Privacy and Cookie Policy' link")
    def test_visibility_privacy_and_cookie_policy_link(self):
        main_page = MainPage(browser=browser)

        main_page.open_page()
        main_page.scroll_to_privacy_cookie_policy_link()

        main_page.privacy_cookie_policy_link.should(be.visible)
        main_page.privacy_cookie_policy_link.should(
            have.text(MainPageData.privacy_cookie_policy_link_text)
        )

    @allure.title("TC_012.006.002 | Verify redirect to the ‘Privacy and Cookie Policy’ page")
    def test_redirect_to_privacy_and_cookie_page(self):
        main_page = MainPage(browser=browser)
        privacy_policy_page = PrivacyPolicyPage(browser=browser)

        main_page.open_page()
        main_page.scroll_to_privacy_cookie_policy_link()
        main_page.click_privacy_cookie_policy_link()

        privacy_policy_page.get_privacy_policy_url == PRIVACY_POLICY_PAGE_LINK
        privacy_policy_page.page_main_header.should(
            have.text(PPPD.page_main_header)
        )
