from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color

from pages.locators import ProductLocators as PL

CART_URL = 'https://magento.softwaretestingboard.com/checkout/cart/'

action = s('a.action')
quantity = s(".details-qty input")
message = s(".message-success")
mini_cart = s('#ui-id-1')
mini_cart_view = s('.action.viewcart')

def is_mini_cart_present():
    return mini_cart.should(be.present)

def is_mini_cart_visible():
    return mini_cart.should(be.visible)

def is_minicart_view_present():
    mini_cart_view.should(be.present)

def is_minicart_view_visible():
    mini_cart_view.should(be.visible)

def is_minicart_have_link():
    mini_cart_view.should(have.attribute('href').value(CART_URL))

def check_color_of_in_the_mini_cart(self, color):
    action.should(have.css_property("color").value(Color.from_string(color).rgba))

def check_edit_cart_link_in_the_mini_cart():
    s(PL.VIEW_AND_EDIT_CART_HREF).should(have.attribute("href"))

def check_the_link_opens_checkout_cart_page():
    s(PL.VIEW_AND_EDIT_CART_LINK).click()

def checking_the_size_color_and_product_name_are_correct():
    see_details = s('[data-role="title"]')
    see_details.click()
    s(PL.SIZE_M).should(have.text("M"))
    s(PL.COLOR_GRAY).should(have.text("Gray"))
    s(PL.NAME_ITEM).should(have.text("Argus All-Weather Tank"))

def change_qty(self, qty):
    quantity.should(be.clickable).send_keys(Keys.BACKSPACE + qty)
    s(PL.UPDATE).click()

def should_be_quantity_change(self, qty):
    quantity.should(have.value(qty))

def should_be_success_message():
    message.should(be.visible)

def should_be_change_subtotal(self, price, total):
    s(PL.PRICE_ITEM).should(have.text(price))
    s(PL.CART_SUBTOTAL).should(have.text(total))

def click_mini_cart():
    mini_cart.should(be.clickable).click()
