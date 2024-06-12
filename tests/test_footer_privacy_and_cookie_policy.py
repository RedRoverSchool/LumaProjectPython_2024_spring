import allure
from pages import main_page


@allure.feature("Footer > Privacy and Cookie Policy > Redirect, Clickability, Visibility")
@allure.title("Verify visibility of the 'Privacy and Cookie Policy' link")
@allure.link("https://trello.com/c/MGEOisOH")
def test_visibility_privacy_and_cookie_policy_link():
    main_page.open_page()
    main_page.scroll_to_privacy_cookie_policy_link()
    main_page.link_name_is_visible('Privacy and Cookie Policy')


@allure.feature("Footer > Privacy and Cookie Policy > Redirect, Clickability, Visibility")
@allure.title("Verify redirect to the ‘Privacy and Cookie Policy’ page")
@allure.link("https://trello.com/c/9stTdv0S")
def test_redirect_to_privacy_and_cookie_page():
    main_page.open_page()
    main_page.scroll_to_privacy_cookie_policy_link()
    main_page.click_privacy_cookie_policy_link()
    main_page.should_be_redirected_to('Privacy Policy')
