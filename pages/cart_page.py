from selene.support.shared.jquery_style import s
from selene import be

from data.links import CART_LINK
from pages.locators import CartLocators as Cart
from pages.locators import HomeLocators as HL
from pages.components.nav_wigdet import NavComponent


class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent(browser)

    def open_page(self):
        self.browser.open(CART_LINK)

    def find_cart_icon(self):
        return s(HL.CART_ICON)

    def is_cart_icon_clickable(self):
        return self.find_cart_icon().should(be.clickable)

    def find_qty(self):
        return s(Cart.QTY)

    def is_qty_present(self):
        return self.find_qty().should(be.present)

    def set_value_of_qty(self, value):
        self.is_qty_present()
        self.find_qty().clear()
        self.find_qty().send_keys(value)

    def click_update_shopping_cart_button(self):
        self.is_update_shopping_cart_button_present()
        self.find_update_shopping_cart_button().click()

    def find_update_shopping_cart_button(self):
        return s(Cart.UPDATE_SHOPPING_CART_BUTTON)

    def is_update_shopping_cart_button_present(self):
        return self.find_update_shopping_cart_button().should(be.present)

    def find_counter_number(self):
        return s(HL.MINICART_COUNTER)

    def is_counter_number_present(self):
        return self.find_counter_number().should(be.present)

    def is_counter_number_visible(self):
        return self.find_counter_number().should(be.visible)