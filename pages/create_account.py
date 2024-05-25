from selene import browser, have
from selene.support.shared.jquery_style import s

from pages.locators import CreateAccountLocators

url = "https://magento.softwaretestingboard.com/customer/account/create/"

firstname_input = s("#firstname")
lastname_input = s("#lastname")
email_address_input = s("#email_address")
password_input = s("#password")
password_confirmation_input = s("#password-confirmation")
firstname_error_message = s("#firstname-error")
lastname_error_message = s("#lastname-error")
email_address_error_message = s("#email_address-error")
password_error_message = s("#password-error")
password_strength_meter = s("#password-strength-meter")
password_strength_meter_label = s("#password-strength-meter-label")
password_confirmation_error = s("#password-confirmation-error")
page_title = s("h1.page-title")


def visit():
    browser.open(url)


def create_account(first_name, last_name, user_email, password):
    firstname_input.type(first_name)
    lastname_input.type(last_name)
    email_address_input.type(user_email)
    password_input.type(password)
    password_confirmation_input.type(password).press_enter()


def should_be_first_name_error(partial_text):
    firstname_error_message.should(have.text(partial_text))


def should_be_last_name_error(partial_text):
    lastname_error_message.should(have.text(partial_text))


def should_be_user_email_error(partial_text):
    email_address_error_message.should(have.text(partial_text))


def should_be_password_error(partial_text):
    password_error_message.should(have.text(partial_text))


def should_be_password_strength_meter_color(color):
    password_strength_meter.should(have.css_property("color").value(color))


def should_be_password_strength_meter_label_text(partial_text):
    password_strength_meter_label.should(have.text(partial_text))


def should_be_password_confirmation_error(partial_text):
    password_confirmation_error.should(have.text(partial_text))


def click_the_create_account_link():
    s(CreateAccountLocators.CREATE_AN_ACCOUNT_LINK).click()


def should_have_page_title(text):
    page_title.should(have.text(text))


def should_be_create_account_url():
    browser.should(have.url(url))
