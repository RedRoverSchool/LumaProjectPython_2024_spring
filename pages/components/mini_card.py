from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color

from pages.locators import HomeLocators as Home, ProductLocators as PL


class MiniCard:

    def find_minicart(self):
        return s(Home.MINICART)

    def is_minicart_present(self):
        return self.find_minicart().should(be.present)

    def is_minicart_visible(self):
        return self.find_minicart().should(be.visible)

    @staticmethod
    def find_minicart_view():
        return s(Home.MINICART_VIEW)

    @property
    def is_minicart_view_present(self):
        return self.find_minicart_view().should(be.present)

    def is_minicart_view_enable(self):
        return self.find_minicart_view().should(be.enabled)

    def is_minicart_view_visible(self):
        return self.find_minicart_view().should(be.visible)

    def is_minicart_have_link(self):
        return self.find_minicart_view().should(
            have.attribute('href').value('https://magento.softwaretestingboard.com/checkout/cart/'))

    def check_color_of_view_and_edit_cart_link_in_the_mini_cart(self):
        s('a.action').should(have.css_property("color").value(Color.from_string("#006bb4").rgba))

    def check_clickability_of_view_and_edit_cart_link_in_the_mini_cart(self):
        edit = s(PL.VIEW_AND_EDIT_CART_HREF)
        edit.should(have.attribute("href"))

    def checking_the_link_opens_checkout_cart_page(self):
        s(PL.VIEW_AND_EDIT_CART_LINK).click()

    def checking_the_size_color_and_product_name_are_correct(self):
        s(PL.SEE_DETAILS).click()
        s(PL.SIZE_M).should(have.text("M"))
        s(PL.COLOR_GRAY).should(have.text("Gray"))
        s(PL.NAME_ITEM).should(have.text("Argus All-Weather Tank"))

    def checking_present_price_item_and_cart_subtotal_in_the_mini_cart(self, price, total):
        s(PL.PRICE_ITEM).should(have.text(price))
        s(PL.CART_SUBTOTAL).should(have.text(total))

    def change_qty(self):
        s(PL.QTY_FIELD).should(be.clickable).send_keys(Keys.BACKSPACE + "7")
        s(PL.UPDATE).click()

    def should_be_quantity_change(self):
        s(PL.QTY_FIELD).should(have.value("7"))


    def should_be_success_message(self):
        s(".message-success").should(be.visible)

    def should_be_change_subtotal(self, price, total):
        s(PL.PRICE_ITEM).should(have.text(price))
        s(PL.CART_SUBTOTAL).should(have.text(total))