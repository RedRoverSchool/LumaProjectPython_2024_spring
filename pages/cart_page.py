from selene import be, have
from selene.support.shared.jquery_style import s

from data.links import CART_LINK
from pages.base_page import BasePage
from pages.locators import CartLocators as Cart
from pages.locators import HomeLocators as HL
from pages.locators import ProductLocators as PL


class CartPage(BasePage):

    qty = s(Cart.QTY)

    def open_page(self):
        self.visit(CART_LINK)
        return self

    def is_qty_present(self):
        return self.qty.should(be.present)

    def set_value_of_qty(self, value):
        self.is_qty_present()
        self.qty.clear()
        self.qty.send_keys(value)

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


    def checking_product_name_are_correct_in_checkout_cart_page(self):
        s(PL.NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text("Argus All-Weather Tank"))

    def checking_size_are_correct_in_checkout_cart_page(self, size):
        s(PL.SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART).should(have.text(size))

    def checking_color_are_correct_in_checkout_cart_page(self, color):
        s(PL.COLOR_GRAY_ARGUS_CHECKOUT_CART).should(have.text(color))


    def check_price_present_in_checkout_cart_page(self, price):
        s(PL.PRICE_ITEM_CHECKOUT_CART).should(be.present).should(have.text(price))

    def check_qty_present_in_checkout_cart_page(self):
        s(PL.QTY_FIELD_CHECKOUT_CART).should(be.present)

    def check_subtotal_present_in_checkout_cart_page(self):
        s(PL.CART_SUBTOTAL_CHECKOUT_CART).should(be.present).should(have.text("$"))

