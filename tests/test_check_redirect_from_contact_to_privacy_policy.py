import allure
from selene import have
from pages.locators import *
from pages import privacy_policy_page


@allure.feature('Privacy and Cookie > Contact us link')
@allure.title('Verify redirect to the previous page using go back link')
@allure.link('https://trello.com/c/6z9X1Uzp')
def test_redirect_from_contact_to_privacy_policy():
    privacy_policy_page.open_page()
    browser.element(ContactUsLocators.CONTACT_US_LINK).click()
    browser.element(PrivacyPolicy.GO_BACK_LINK).click()
    browser.element(PrivacyPolicy.PRIVACY_POLICY_TITLE).should(have.text('Privacy Policy'))
