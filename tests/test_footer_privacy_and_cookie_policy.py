import allure
from selene import browser
from selene.support.conditions import have, be

from pages.main_page import MainPage
from pages import privacy_policy_page
from data.page_data import MainPageData


@allure.feature("Footer > Privacy and Cookie Policy > Redirect, Clickability, Visibility")
class TestPrivacyAndCookiePolicy:

    @allure.link("https://trello.com/c/MGEOisOH")
    @allure.title("TC_012.006.001 | Verify visibility of the 'Privacy and Cookie Policy' link")
    def test_visibility_privacy_and_cookie_policy_link(self):
        main_page = MainPage(browser=browser)

        main_page.open_page()
        main_page.scroll_to_privacy_cookie_policy_link()

        main_page.privacy_cookie_policy_link.should(be.visible)
        main_page.privacy_cookie_policy_link.should(
            have.text(MainPageData.privacy_cookie_policy_link_text)
        )

    @allure.link("https://trello.com/c/9stTdv0S")
    @allure.title("TC_012.006.002 | Verify redirect to the ‘Privacy and Cookie Policy’ page")
    def test_redirect_to_privacy_and_cookie_page(self):
        main_page = MainPage(browser=browser)

        main_page.open_page()
        main_page.scroll_to_privacy_cookie_policy_link()
        main_page.click_privacy_cookie_policy_link()

        assert privacy_policy_page.is_current_url()
        privacy_policy_page.is_header_has_text(MainPageData.header)
