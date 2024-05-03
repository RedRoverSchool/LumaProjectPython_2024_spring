from selene import browser, have
from selene.support.shared.jquery_style import s

from pages.locators import CreateAccountLocators

url = "https://magento.softwaretestingboard.com/customer/account/create/"


def visit():
    browser.open(url)


def new_one(first_name, last_name, user_email, password):
    s(".form-create-account #firstname").type(first_name)
    s(".form-create-account #lastname").type(last_name)
    s(".form-create-account #email_address").type(user_email)
    s(".form-create-account #password").type(password)
    s(".form-create-account #password-confirmation").type(password).press_enter()


def first_name_error(partial_text):
    s(".form-create-account #firstname-error").should(have.text(partial_text))


def last_name_error(partial_text):
    s(".form-create-account #lastname-error").should(have.text(partial_text))


def user_email_error(partial_text):
    s(".form-create-account #email_address-error").should(have.text(partial_text))


def password_error(partial_text):
    s(".form-create-account #password-error").should(have.text(partial_text))


def password_strength_meter(color):
    s(".form-create-account #password-strength-meter").should(have.css_property("color"))


def password_strength_meter_label(partial_text):
    s(".form-create-account #password-strength-meter-label").should(have.text(partial_text))


def password_confirmation_error(partial_text):
    s(".form-create-account #password-confirmation-error").should(have.text(partial_text))


def click_the_create_account_link():
    s(CreateAccountLocators.CREATE_AN_ACCOUNT_LINK).click()


def page_title():
    s("h1.page-title").should(have.text('Create New Customer Account'))


def redirect():
    browser.should(have.url(url))