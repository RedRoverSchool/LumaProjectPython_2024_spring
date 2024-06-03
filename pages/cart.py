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
cart_icon = s('a.showcart')
mini_cart = s('#ui-id-1')
mini_cart_qty = s('input[class="item-qty cart-item-qty"]')
product_price = s('//div[@class="product-info-price"]//span[@data-price-type="finalPrice"]')
minicart_subtotal = s('//*[@id="minicart-content-wrapper"]/div[2]/div[2]/div/span/span')
product_price_cart = s('//td[@class="col price"]/span/span/span')
subtotal_price_cart = s('//td[@class="col subtotal"]/span/span/span')

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


def clear_cart():
    open_page()
    try:
        delete_product_from_cart()
    except:
        pass


def delete_product_from_cart():
    open_page()
    remove_item_icon.click()
    no_items_message.wait_until(be.visible)


def click_cart_icon():
    cart_icon.click()
    mini_cart.wait_until(be.visible)


def product_in_minicart_should_have_name(name):
    s(f"//*[@id='mini-cart']/li/div/div/strong/a[contains(text(), '{name}')]").should(be.visible)


def minicart_quantity_should_be_equal(quantity):
    mini_cart.wait_until(be.visible)
    cart_qty = mini_cart_qty.get(query.attribute("data-item-qty"))
    assert cart_qty == quantity


def minicart_subtotal_should_be_calculated_with_qty_equal(quantity):
    price = int(product_price.get(query.attribute('data-price-amount')))
    cart_subtotal = float(minicart_subtotal.get(query.text).strip('$'))
    assert cart_subtotal == price * int(quantity)


def cart_subtotal_should_be_calculated_with_qty_equal(quantity):
    price = float(product_price_cart.get(query.text).strip('$'))
    cart_subtotal = float(subtotal_price_cart.get(query.text).strip('$'))
    assert cart_subtotal == price * int(quantity)


def counter_should_be_equal(quantity):
    counter_number.should(have.text(quantity))
