from selene.support.shared.jquery_style import s
from selene import be
from pages.locators import CartLocators as Cart
from pages.components.nav_wigdet import NavComponent

class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent(browser)

    def find_qty(self):
        return s(Cart.QTY)

    def is_qty_present(self):
        return s(Cart.QTY).should(be.present)

    def set_value_of_qty(self):
        self.is_qty_present()
        self.find_qty().clear()
        self.find_qty().send_keys('2')

    def find_update_shopping_cart_button(self):
        return s(Cart.UPDATE_SHOPPING_CART_BUTTON)

    def is_update_shopping_cart_button_present(self):
        return s(Cart.UPDATE_SHOPPING_CART_BUTTON).should(be.present)

