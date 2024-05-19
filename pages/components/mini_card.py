from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color

from data.links import CART_URL
from pages.locators import HomeLocators as Home, ProductLocators as PL


class MiniCard:

    action = s('a.action')
    quantity = s(PL.QTY_FIELD)
    message = s(".message-success")
    mini_cart = s(Home.MINICART)
    mini_cart_view = s(Home.MINICART_VIEW)

    def is_minicart_present(self):
        return self.mini_cart.should(be.present)

    def is_minicart_visible(self):
        return self.mini_cart.should(be.visible)

    def is_minicart_view_present(self):
        self.mini_cart_view.should(be.present)

    def is_minicart_view_visible(self):
        self.mini_cart_view.should(be.visible)

    def is_minicart_have_link(self):
        self.mini_cart_view.should(have.attribute('href').value(CART_URL))

    def check_color_of_in_the_mini_cart(self, color):
        self.action.should(have.css_property("color").value(Color.from_string(color).rgba))

    def check_edit_cart_link_in_the_mini_cart(self):
        s(PL.VIEW_AND_EDIT_CART_HREF).should(have.attribute("href"))

    def check_the_link_opens_checkout_cart_page(self):
        s(PL.VIEW_AND_EDIT_CART_LINK).click()

    def checking_the_size_color_and_product_name_are_correct(self):
        s(PL.SEE_DETAILS).click()
        s(PL.SIZE_M).should(have.text("M"))
        s(PL.COLOR_GRAY).should(have.text("Gray"))
        s(PL.NAME_ITEM).should(have.text("Argus All-Weather Tank"))

    def change_qty(self, qty):
        self.quantity.should(be.clickable).send_keys(Keys.BACKSPACE + qty)
        s(PL.UPDATE).click()

    def should_be_quantity_change(self, qty):
        self.quantity.should(have.value(qty))

    def should_be_success_message(self):
        self.message.should(be.visible)

    def should_be_change_subtotal(self, price, total):
        s(PL.PRICE_ITEM).should(have.text(price))
        s(PL.CART_SUBTOTAL).should(have.text(total))

    def click_mini_cart(self):
        self.mini_cart.should(be.clickable).click()
