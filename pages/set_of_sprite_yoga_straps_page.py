from selene import be, have, browser, query
from data import links
from pages.base_page import BasePage
from selene.support.shared.jquery_style import s
from pages.locators import SetYogaStrapsLocators, ProductLocators, BaseLocators, ProductPageLocators, HomeLocators


class SetYogaStraps(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def add_to_cart_more(self, count):
        s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_10_FOOT).click().send_keys(count)
        s(ProductLocators.ADD_TO_CART_BUTTON).click()


def add_to_cart_set_8_foot(count):
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_8_FOOT).clear()
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_8_FOOT).click().send_keys(count)
    s(ProductLocators.ADD_TO_CART_BUTTON).click()


def is_visible_success_message():
    s(BaseLocators.SUCCESS_MESSAGE).should(be.visible)
    s(BaseLocators.SUCCESS_MESSAGE).should(have.text('You added')).should(have.text('to your shopping cart'))


def visit():
    browser.open(links.SET_YOGA_STRAPS_URL)


def check_nr_of_items_in_cart(nr):
    s(BaseLocators.QTY_OF_ITEMS_IN_MINICART).should(have.text((str(nr))))


def open_window_more_info():
    s(ProductPageLocators.WINDOW_MORE_INFO).click()


def check_details_about_material(material):
    s(ProductPageLocators.DESCRIBE_MATERIAL).should(have.text(material))


def add_to_cart_set_6_foot(count):
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_6_FOOT).clear()
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_6_FOOT).click().send_keys(count)
    s(ProductLocators.ADD_TO_CART_BUTTON).click()


def add_to_cart_set_10_foot(count):
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_10_FOOT).clear()
    s(SetYogaStrapsLocators.SPRITE_YOGA_STRAP_10_FOOT).click().send_keys(count)
    s(ProductLocators.ADD_TO_CART_BUTTON).click()


def open_link_view_and_edit_cart():
    s('.actions .viewcart').click()


def find_amount_whole():
    return s('#cart-totals tr.totals.sub span')


def find_discount():
    return s('#cart-totals tr:nth-child(2) span > span')


def find_tax():
    return s('#cart-totals tr.totals-tax span')


def find_sum_total():
    return s('#cart-totals tr.grand.totals span')


def check_discount_amount_more_200():
    tax = s(HomeLocators.TAX_AMOUNT).get(query.attribute('innerText')).replace("$", "")
    discount = s(HomeLocators.DISCOUNT).get(query.attribute('innerText')).replace("$", "")
    total = s(HomeLocators.SUB_TOTAL).get(query.attribute('innerText')).replace("$", "")
    subtotal = s(HomeLocators.GRAND_TOTALS).get(query.attribute('innerText')).replace("$", "")
    # print(f"Total: {total}, Discount: {discount}, tax: {tax}, To pay: {subtotal}")
    return float(discount) == (float(total) / 5) and subtotal == (total - discount + tax)
