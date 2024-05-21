from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import LoginLocators, BaseLocators

url = "https://magento.softwaretestingboard.com/customer/account/login"

user_email = s("div.login-container #email")
user_password = s("div.login-container #pass")
sign_in_button = s("div.login-container #send2")


def visit():
    browser.open(url)


def login(user, password):
    user_email.type(user)
    user_password.type(password)
    sign_in_button.click()


def message_unsuccessful(text):
    s(LoginLocators.MESSAGE_UNSUCCESSFUL).should(have.text(text))


def check_if_this_is_account_url():
    browser.should(have.url(LoginLocators.LINK_ACCOUNT))


def check_user_name_is_present(name):
    s(LoginLocators.USER_NAME_IN_WELCOME).should(have.text(name))


def check_msg_signin_is_missing():
    s(LoginLocators.AUTHORIZATION_LINK).should(have.no.text("Sign In"))


def check_all_pages_have_user_name(name):
    for lnk in BaseLocators.ALL_URL:
        browser.open(lnk)
        s(LoginLocators.USER_NAME_IN_WELCOME).should(have.text(name))
