from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import LoginLocators

url = "https://magento.softwaretestingboard.com/customer/account/login"
LINK_ACCOUNT = 'https://magento.softwaretestingboard.com/customer/account/'
user_email = s("div.login-container #email")
user_password = s("div.login-container #pass")
sign_in_button = s("div.login-container #send2")
AUTHORIZATION_LINK = 'authorization-link'
USER_NAME_IN_WELCOME = '.logged-in'
MANY_URL = ["https://magento.softwaretestingboard.com/",
           "https://magento.softwaretestingboard.com/what-is-new.html",
           "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html,"
           "https://magento.softwaretestingboard.com/training.html"
           ]


def visit():
    browser.open(url)


def login(user, password):
    user_email.type(user)
    user_password.type(password)
    sign_in_button.click()


def message_unsuccessful(text):
    s(LoginLocators.MESSAGE_UNSUCCESSFUL).should(have.text(text))


def check_if_this_is_account_url():
    browser.should(have.url(LINK_ACCOUNT))


def check_user_name_is_present(name):
    s(USER_NAME_IN_WELCOME).should(have.text(name))


def check_msg_signin_is_missing():
    s(AUTHORIZATION_LINK).should(have.no.text("Sign In"))


def check_all_pages_have_user_name(name):
    for lnk in MANY_URL:
        browser.open(lnk)
        s(USER_NAME_IN_WELCOME).should(have.text(name))
