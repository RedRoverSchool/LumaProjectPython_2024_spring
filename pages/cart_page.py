from selene import be, have, browser
from selene.core import query
from selene.support.shared.jquery_style import s

from pages.locators import ProductLocators as PL

CART_LINK = 'https://magento.softwaretestingboard.com/checkout/cart/'

qty = s('.input-text.qty')
counter_number = s('.counter-label')
remove_item_icon = s('.action.action-delete')
click_message = s('//p[contains(text(), "Click")]')
no_items_message = s('//p[text()="You have no items in your shopping cart."]')
update_shopping_cart_button = s('.action.update')
tax = s('tr.totals-tax .amount .price')
discount = s('tr.totals .amount .price')
subtotal = s('tr.totals.sub .amount .price')
total = s('tr.grand.totals .amount .price')


def open_page():
    browser.open(CART_LINK)


def is_qty_present():
    qty.should(be.present)


def set_value_of_qty(value):
    is_qty_present()
    qty.clear()
    qty.send_keys(value)


def click_update_shopping_cart_button():
    is_update_shopping_cart_button_present()
    update_shopping_cart_button.click()


def is_update_shopping_cart_button_present():
    update_shopping_cart_button.should(be.present)


def is_counter_number_present():
    counter_number.should(be.present)


def is_counter_number_visible():
    counter_number.should(be.visible)


def is_find_remove_item_icon_present():
    remove_item_icon.should(be.present)


def should_be_message_no_items(text):
    no_items_message.should(have.text(text))


def should_be_message_click(text):
    click_message.should(have.text(text))


def get_cart_totals():
    return f"total:{get_text(total)}, price:{get_text(discount)}, tax:{get_text(tax)}, subtotal:{get_text(subtotal)}"


def checking_product_name_are_correct_in_checkout_cart_page():
    s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text("Argus All-Weather Tank"))


def checking_size_are_correct_in_checkout_cart_page(size):
    s(PL.SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text(size))


def checking_color_are_correct_in_checkout_cart_page(color):
    s(PL.COLOR_GRAY_ARGUS_CHECKOUT_CART).should(have.text(color))


def check_price_present_in_checkout_cart_page(price):
    s(PL.PRICE_ITEM_CHECKOUT_CART).should(be.present).should(have.text(price))


def check_qty_present_in_checkout_cart_page():
    s(PL.QTY_FIELD_CHECKOUT_CART).should(be.present)


def check_subtotal_present_in_checkout_cart_page():
    s(PL.CART_SUBTOTAL_CHECKOUT_CART).should(be.present).should(have.text("$"))


def get_text(selector):
    return selector.get(query.attribute('innerText'))
