from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/customer/account/login"


def visit():
    browser.open(url)


def login(user, password):
    s("div.login-container #email").type(user)
    s("div.login-container #pass").type(password)
    s("div.login-container #send2").click()


def page_title(partial_text):
    s("h1.page-title").should(have.text(partial_text))


def registered_customers_blog(text):
    s("div.login-container #block-customer-login-heading").should(have.text(text))


def new_customers_blog(text):
    s("div.login-container #block-new-customer-heading").should(have.text(text))
