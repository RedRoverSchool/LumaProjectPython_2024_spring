from selene.support.shared.jquery_style import s
from pages.locators import Shipping
from data.links import *
from selene import browser, have, be


def check_if_this_is_page_for_shipping():
    browser.should(have.url(LINK_SHIPPING))


def fill_field_email():
    s(Shipping.FIELD_EMAIL).type("email@mail.aaa")


def fill_field_first_name():
    s(Shipping.FIELD_FIRST_NAME).type("f_name")


def fill_field_last_name():
    s(Shipping.FIELD_LAST_NAME).type("l_name")


def fill_field_street():
    s(Shipping.FIELD_STREET).type("street")


def fill_field_city():
    s(Shipping.FIELD_CITY).type("city")


def fill_field_region():
    s(Shipping.FIELD_REGION).press("Alabama")


def fill_field_zipcode():
    s(Shipping.FIELD_ZIPCODE).type("MD2060")


def fill_field_country():
    s(Shipping.FIELD_COUNTRY).press("Tanzania")


def fill_field_phone():
    s(Shipping.FIELD_PHONE).type("1234567890")


def choose_shipping_method():
    s(Shipping.SHIPPING_METHOD).should(be.clickable).click()


def go_to_order():
    s(Shipping.CONTINUE_BUTTON).should(be.clickable).click()
