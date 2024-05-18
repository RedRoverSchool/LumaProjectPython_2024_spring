from selene import be, have, browser
from data import links
from pages.base_page import BasePage
from selene.support.shared.jquery_style import s
from pages.locators import SetYogaStrapsLocators, ProductLocators, BaseLocators, HomeLocators


class SetYogaStraps(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def add_to_cart_more(self, count):
        s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_10_FOOT).click().send_keys(count)
        s(ProductLocators.ADD_TO_CART_BUTTON).click()


def add_to_cart_set_8_foot(count):
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_8_FOOT).click().send_keys(count)
    s(ProductLocators.ADD_TO_CART_BUTTON).click()


def is_visible_success_message():
    s(BaseLocators.SUCCESS_MESSAGE).should(be.visible)
    s(BaseLocators.SUCCESS_MESSAGE).should(have.text('You added')).should(have.text('to your shopping cart'))


def visit():
    browser.open(links.SET_YOGA_STRAPS_URL)


def check_nr_of_items_in_cart(nr):
    s(BaseLocators.QTY_OF_ITEMS_IN_MINICART).should(have.text((str(nr))))
