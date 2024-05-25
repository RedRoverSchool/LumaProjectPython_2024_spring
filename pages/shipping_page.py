from selene.support.shared.jquery_style import s
# from pages.locators import Shipping
from data.links import *
from selene import browser, have, be


LINK_WOMEN = "https://magento.softwaretestingboard.com/women.html"
LINK_SHIPPING = "https://magento.softwaretestingboard.com/checkout/#shipping"
LINK_PAYMENT = "https://magento.softwaretestingboard.com/checkout/#payment"
#shipping
FIELD_EMAIL = '#customer-email-fieldset #customer-email'
FIELD_FIRST_NAME = '[name="firstname"]'
FIELD_LAST_NAME = '[name="lastname"]'
FIELD_STREET = '[name="street[0]"]'
FIELD_CITY = '[name="city"]'
FIELD_REGION = '[name="region_id"]'
FIELD_COUNTRY = '[name="country_id"]'
FIELD_ZIPCODE = '[name="postcode"]'
FIELD_PHONE = '[name="telephone"]'
SHIPPING_METHOD = '#checkout-shipping-method-load input'
CONTINUE_BUTTON = '.continue'
# payment
BUTTON_PLACE_ORDER = '.primary.checkout'
MESSAGE_SUCCEES = '.checkout-success'
ORDER_PAGE_TITLE = '.page-title'
TANK_SIZE = '//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="M"]'
TANK_COLOR = '//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="Yellow"]'
TANK_BUTTON_ADD = '//*[@title="Breathe-Easy Tank"]/../..//*[@title="Add to Cart"]'
MESSAGE_SUCCESS_ADD = "div.messages [data-bind ^='html']"
SHOW_BASKET = ".action.showcart"
CHECKOUT_BUTTON = '#top-cart-btn-checkout'


def visit():
    browser.open(LINK_WOMEN)


def check_if_this_is_page_for_shipping():
    browser.should(have.url(LINK_SHIPPING))


def fill_field_email():
    s(FIELD_EMAIL).type("email@mail.aaa")


def fill_field_first_name():
    s(FIELD_FIRST_NAME).type("f_name")


def fill_field_last_name():
    s(FIELD_LAST_NAME).type("l_name")


def fill_field_street():
    s(FIELD_STREET).type("street")


def fill_field_city():
    s(FIELD_CITY).type("city")


def fill_field_region():
    s(FIELD_REGION).press("Alabama")


def fill_field_zipcode():
    s(FIELD_ZIPCODE).type("MD2060")


def fill_field_country():
    s(FIELD_COUNTRY).press("Tanzania")


def fill_field_phone():
    s(FIELD_PHONE).type("1234567890")


def choose_shipping_method():
    s(SHIPPING_METHOD).should(be.clickable).click()


def go_to_order():
    s(CONTINUE_BUTTON).should(be.clickable).click()


def check_if_this_is_page_for_payment():
    browser.should(have.url(LINK_PAYMENT))


def click_button_place_order():
    s(BUTTON_PLACE_ORDER).click()


def check_message_about_oder_nr():
    s(MESSAGE_SUCCEES).should(have.text("Your order # is"))


def check_success_message():
    s(ORDER_PAGE_TITLE).should(have.text("Thank you for your purchase!"))


def choose_size_for_tank():
    s(TANK_SIZE).click()


def choose_color_for_tank():
    s(TANK_COLOR).click()


def button_add_to_cart_tank():
    s(TANK_BUTTON_ADD).click()


def success_msg_is_present():
    s(MESSAGE_SUCCESS_ADD).should(have.text("You added"))


def open_minicart():
    s(SHOW_BASKET).should(be.clickable).click()


def open_checkout():
    s(CHECKOUT_BUTTON).should(be.visible)
    s(CHECKOUT_BUTTON).should(be.clickable).click()
