from selene import query
from selene.support.shared.jquery_style import s
from selene.support.conditions import be
from selenium.webdriver import Keys

from pages.locators import ProductLocators as PL, HomeLocators as HL


def select_product_size(size):
    s(f'[option-label={size}]').click()


def select_product_color(color):
    s(f'[option-label={color}]').click()


def check_radiant_tee_name_in_minicart_is_visible():
    s(HL.MINICART_RADIANT_TEE_NAME).should(be.visible)


def select_product_quantity(qty):
    s(PL.RADIANT_TEE_QTY).click()
    s(PL.RADIANT_TEE_QTY).type(Keys.DELETE)
    s(PL.RADIANT_TEE_QTY).type(qty)


def add_product_to_cart():
    s(PL.ADD_TO_CART_BUTTON).click()
    s(PL.ADDING_TO_CART_SUCCESSFULL_MSG).wait_until(be.visible)


def check_minicart_subtotal(qty):
    product_price = float(s(PL.PRODUCT_PRICE).get(query.text).strip('$'))
    subtotal = float(s(HL.MINICART_SUBTOTAL).get(query.text).strip('$'))
    assert subtotal == round(product_price * int(qty), 2)

def find_reviews_tab():
    return s(PL.PRODUCT_REVIEW_TAB)

def is_reviews_tab_visible():
    return find_reviews_tab().should(be.visible)

def open_reviews_tab():
    if is_reviews_tab_visible():
        s(PL.PRODUCT_REVIEW_TAB).click()

def is_customer_reviews_present():
    return s(PL.CUSTOMER_REVIEWS).should(be.existing)

def is_review_details_visible(review):
    return review.s(PL.REVIEW_DETAILS).should(be.visible)

def is_rating_visible(review):
    return review.s(".rating-result").should(be.visible)
