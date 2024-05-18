import time
from data.page_data import SignInData
from pages import sign_in
from selene import be, have
from selene.support.shared.jquery_style import s
from pages.locators import *

email = SignInData()
password = SignInData()
discount_link = TeesPageLocators()
sale = SalePageLocators()
qty_tees = ProductLocators()
cart = HomeLocators()


def check_four_similar_tees_discount_is_applies():
    sign_in.visit()
    sign_in.login(SignInData.email, SignInData.password)
    s(SalePageLocators.SALE_TAB).click()
    s(TeesPageLocators.FOUR_TEES_DISCOUNT_TAB).click()
    s(TeesPageLocators.TEES).click()
    s(TeesPageLocators.TEES_SIZE).click()
    s(TeesPageLocators.TEES_COLORS).click()
    s(TeesPageLocators.TEES_QTY).clear()
    s(TeesPageLocators.TEES_QTY).type('4')
    s(ProductLocators.ADD_TO_CART_BUTTON).click()
    time.sleep(3)
    s(TeesPageLocators.COUNT_NUMBER).should(be.visible)
    s(HomeLocators.CART_ICON).click()
    s(TeesPageLocators.VIEW_AND_EDIT_CART_LINK).should(be.visible).click()
    s(TeesPageLocators.DISCOUNT_SUMM).should(have.text('-$24.00'))
    s(TeesPageLocators.REMOVE_TEES_BTN_FROM_CART_AFTER_TEST).click()







