import allure

from pages import privacy_policy_page


@allure.feature('Privacy and Cookie Policy > Contact us link')
@allure.title("Verify redirect from Privacy Policy to Contact Us link")
@allure.link('https://trello.com/c/JMia3A7B')
def test_redirect_to_contact_form_from_private_policy():
    privacy_policy_page.open_page()
    privacy_policy_page.should_be_open_contact_us_page()
