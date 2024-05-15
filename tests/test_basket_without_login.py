import time

import allure

from data.links import *
from pages.locators import WomenLocators, Shipping, Order
from selene import browser, be, have
from selene.support.shared.jquery_style import s
from selene.support.conditions import be, have


@allure.link("https://trello.com/c/6IIncPjn")
def test_004_001_002_guest_user_checkout_from_minicart():
    browser.open(LINK_WOMEN)
    # choose item
    s(WomenLocators.TANK_SIZE).click()
    s(WomenLocators.TANK_COLOR).click()
    s(WomenLocators.TANK_BUTTON_ADD).click()
    time.sleep(4)
    s(WomenLocators.MESSAGE_SUCCESS_ADD).should(have.text("You added"))
    # open minicart
    s(WomenLocators.SHOW_BASKET).should(be.clickable).click()
    s(WomenLocators.CHECKOUT_BUTTON).should(be.visible)
    s(WomenLocators.CHECKOUT_BUTTON).should(be.clickable).click()
    # fill address
    browser.should(have.url(LINK_SHIPPING))
    s(Shipping.FIELD_EMAIL).type("email@mail.aaa")
    s(Shipping.FIELD_FIRST_NAME).type("f_name")
    s(Shipping.FIELD_LAST_NAME).type("l_name")
    s(Shipping.FIELD_STREET).type("street")
    s(Shipping.FIELD_CITY).type("city")
    s(Shipping.FIELD_REGION).press("Alabama")
    s(Shipping.FIELD_ZIPCODE).type("MD2060")
    s(Shipping.FIELD_COUNTRY).press("Tanzania")
    s(Shipping.FIELD_PHONE).type("1234567890")
    s(Shipping.SHIPPING_METHOD).should(be.clickable).click()
    s(Shipping.CONTINUE_BUTTON).should(be.clickable).click()
    browser.should(have.url(LINK_PAYMENT))
    # check data and place order
    s(Order.BUTTON_PLACE_ORDER).click()
    s(Order.MESSAGE_SUCCEES).should(have.text("Your order # is"))
    s(Order.ORDER_PAGE_TITLE).should(have.text("Thank you for your purchase!"))

