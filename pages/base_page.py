from selene import have, be, Element
from selene.core import command, query
from selene.core.exceptions import ConditionNotMatchedError
from selene.support.shared.jquery_style import s, ss
from data.links import CART_LINK
from pages.components.mini_card import MiniCard
from pages.components.nav_wigdet import NavComponent
from pages.locators import BaseLocators, ProductItemLocators, HomeLocators, ProductLocators as PL, CartLocators as Cart, \
    CreateAccountLocators


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent()
        self.mini_card = MiniCard()

    def visit(self, url):
        self.browser.open(url)

    def assert_text_of_element(self, locator, expected_text):
        s(locator).should(have.text(expected_text))

    def assert_visible_of_element(self, locator):
        s(locator).should(be.visible)

    def assert_present_of_element(self, locator):
        s(locator).should(be.present)

    def get_current_url(self):
        return self.browser.driver.current_url

    def find_cart_icon(self):
        return s(HomeLocators.CART_ICON)

    def find_counter_number(self):
        return s(HomeLocators.MINICART_COUNTER)

    def is_cart_icon_present(self):
        return self.find_cart_icon().should(be.present)

    def is_cart_icon_clickable(self):
        return self.find_cart_icon().should(be.clickable)

    def is_counter_number_present(self):
        return self.find_counter_number().should(be.present)

    def is_counter_number_visible(self):
        return self.find_counter_number().should(be.visible)

    def add_product_to_cart(self, product: Element):
        product.hover()
        self.set_color(product)
        self.set_size(product)
        product.s(HomeLocators.TO_CART_BUTTON).should(be.visible).should(be.clickable).click()
        self.is_visible_success_message()
        self.find_cart_icon().hover().click()

    def add_item_to_cart(self, size, color, add_to_cart_button):
        s(size).click()
        s(color).click()
        s(add_to_cart_button).click()

    def goto_card_page(self):
        self.is_cart_icon_present()
        self.find_cart_icon().hover().click()
        self.mini_card.is_minicart_visible()
        self.mini_card.find_minicart().hover().click()

    def scroll_to_hot_sellers(self):
        self.scroll_to(s(ProductItemLocators.PRODUCTS_GRID))

    def get_subtotal(self):
        self.is_cart_icon_clickable().hover().click()
        amount_price = s(HomeLocators.AMOUNT_PRICE).s(HomeLocators.MINI_CART_PRICE)
        price = amount_price.get(query.attribute('innerText'))
        return float(price.replace('$', ''))

    @staticmethod
    def set_size(product: Element):
        size_options = product.ss(HomeLocators.SIZES)
        if len(size_options) > 0:
            size_options.first.click()

    @staticmethod
    def set_color(product: Element):
        color_options = product.ss(HomeLocators.COLORS)
        if len(color_options) > 0:
            color_options.first.click()

    @staticmethod
    def is_visible_success_message():
        message = s(BaseLocators.SUCCESS_MESSAGE)
        message.should(be.visible)
        message.should(have.text('You added')).should(have.text('to your shopping cart'))

    @staticmethod
    def scroll_to(element: Element):
        element.perform(command.js.scroll_into_view)

    @staticmethod
    def find_products():
        return ss(ProductItemLocators.ITEM_INFO)

    @staticmethod
    def get_text(selector):
        return s(selector).get(query.attribute('innerText'))

    @staticmethod
    def click_on_link(locator):
        s(locator).click()

    def clear_cart(self):
        self.visit(CART_LINK)
        try:
            self.delete_product_from_cart()
        except:
            pass

    def delete_product_from_cart(self):
        self.visit(CART_LINK)
        s(Cart.REMOVE_ITEM_ICON).click()
        s(Cart.NO_ITEMS_MESSAGE).wait_until(be.visible)

    def add_product_to_cart_with_qty(self, size, color, qty):
        s(f'[option-label={size}]').click()
        s(f'[option-label={color}]').click()
        s(PL.PRODUCT_QTY).click()
        s(PL.PRODUCT_QTY).clear()
        s(PL.PRODUCT_QTY).type(qty)
        s(PL.ADD_TO_CART_BUTTON).click()
        self.is_visible_success_message()

    def is_minicart_subtotal_correct(self, qty):
        s(HomeLocators.MINICART).wait_until(be.visible)
        product_price = float(s(PL.PRODUCT_PRICE).get(query.text).strip('$'))
        subtotal = self.get_subtotal()
        assert subtotal == product_price * int(qty)

    @staticmethod
    def is_minicart_quantity_correct(qty):
        s(HomeLocators.MINICART).wait_until(be.visible)
        minicart_qty = s(HomeLocators.MINICART_PRODUCT_QTY).get(query.attribute("data-item-qty"))
        assert minicart_qty == qty

    def is_cart_counter_shows_correct_number(self, qty):
        cart_icon_qty = self.find_counter_number().get(query.text)
        assert cart_icon_qty == qty

    def is_create_account_link_visible(self) -> bool:
        try:
            s(CreateAccountLocators.CREATE_AN_ACCOUNT_LINK).should(have.text('Create an Account')).should(be.visible)
            return True
        except AssertionError:
            return False
