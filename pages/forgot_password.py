from selene import browser
from selene.support.shared.jquery_style import s

url = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"

user_email_input = s("#email_address")


def visit():
    browser.open(url)


def reset(user_email):
    user_email_input.type(user_email).press_enter()
