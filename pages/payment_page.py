from selene.support.shared.jquery_style import s
from pages.locators import Order
from data.links import *
from selene import browser, have


def check_if_this_is_page_for_payment():
    browser.should(have.url(LINK_PAYMENT))


def click_button_place_order():
    s(Order.BUTTON_PLACE_ORDER).click()


def check_message_about_oder_nr():
    s(Order.MESSAGE_SUCCEES).should(have.text("Your order # is"))


def check_success_message():
    s(Order.ORDER_PAGE_TITLE).should(have.text("Thank you for your purchase!"))