from selene.support.shared.jquery_style import s
from selene import be, have
from selene.core import query
from selene.support.shared.jquery_style import s

from data.links import CART_LINK
from pages.base_page import BasePage
from pages.locators import CartLocators as Cart
from pages.locators import HomeLocators as HL


class CartPage(BasePage):

    def open_page(self):
        self.visit(CART_LINK)
        return self

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

    def find_remove_item_icon(self):
        return s(Cart.REMOVE_ITEM_ICON)

    def is_find_remove_item_icon_present(self):
        return self.find_remove_item_icon().should(be.present)

    def find_no_items_message(self):
        return s(Cart.NO_ITEMS_MESSAGE)

    def should_be_message_no_items(self, text):
        return s(Cart.NO_ITEMS_MESSAGE).should(have.text(text))

    def find_click_message(self):
        return s(Cart.CLICK_MESSAGE)

    def should_be_message_click(self, text):
        return s(Cart.CLICK_MESSAGE).should(have.text(text))

    def get_cart_totals(self):
        tax = self.get_text(HL.TAX_AMOUNT)
        discount = self.get_text(HL.TOTALS)
        subtotal = self.get_text(HL.SUB_TOTAL)
        total = self.get_text(HL.GRAND_TOTALS)
        return f"Total: {total}, Price: {discount}, tax: {tax}, subtotal: {subtotal}"

