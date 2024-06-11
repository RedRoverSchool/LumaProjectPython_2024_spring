import allure
from pages import privacy_policy_page


@allure.feature('Privacy and Cookie Policy > Contact us link')
@allure.title('Confirmation of the "Contact Us" Link Redirection Functionality')
@allure.link("https://trello.com/c/9qBktOT6")
def test_contact_us_link_redirects_to_contact_us_page():
    privacy_policy_page.open_page()
    privacy_policy_page.click_to_contact_us_link()
    privacy_policy_page.check_redirect_to_contact_us_page('Whoops, our bad...')
