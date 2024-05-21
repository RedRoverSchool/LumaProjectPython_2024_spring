from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import LoginLocators, BaseLocators

url = "https://magento.softwaretestingboard.com/customer/account/login"


def visit():
    browser.open(url)


def login(user, password):
    s("div.login-container #email").type(user)
    s("div.login-container #pass").type(password)
    s("div.login-container #send2").click()


def message_unsuccessful():
    s(LoginLocators.MESSAGE_UNSUCCESSFUL).should(have.text("This is a required field."))


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


def page_title(partial_text):
    s("h1.page-title").should(have.text(partial_text))


def registered_customers_blog(text):
    s("div.login-container #block-customer-login-heading").should(have.text(text))


def new_customers_blog(text):
    s("div.login-container #block-new-customer-heading").should(have.text(text))
