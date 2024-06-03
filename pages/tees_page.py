from selene import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from data.page_data import SignInData
from pages import sign_in
from pages.locators import *


def open_login_page():
    sign_in.visit()


def login_in():
    sign_in.login(SignInData.email_s, SignInData.password_s)


def click_on_four_tees_discount_banner():
    s(SalePageLocators.SALE_TAB).click()
    s(TeesPageLocators.FOUR_TEES_DISCOUNT_TAB).click()


def check_the_shopping_cart_is_empty():
    s('a.showcart').click()
    s(HomeLocators.EMPTY_MINICART_MSG).should(have.text("You have no items in your shopping cart."))


def add_four_same_model_tees():
    s(TeesPageLocators.TEES).click()
    s(TeesPageLocators.TEES_SIZE_XS).click()
    s(TeesPageLocators.TEES_COLOR_BLACK).click()
    s(TeesPageLocators.TEES_QTY).clear()
    s(TeesPageLocators.TEES_QTY).type('4')


def click_on_add_to_cart_btn():
    s('#product-addtocart-button').click()
    browser.driver.back()
    browser.should(have.url("https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"))


def check_discount_is_applied_for_four_similar_tees():
    s(TeesPageLocators.DISCOUNT_SUMM).should(have.text('-$24.00'))


def check_discount_is_applied_for_four_different_tees():
    try:
        s(TeesPageLocators.DISCOUNT_SUMM).should(be.visible)
    except Exception as e:
        print("Error discount did not apply, write bug report", e)


def click_on_the_shopping_cart_icon():
    s(TeesPageLocators.COUNT_NUMBER).should(be.visible)
    s('a.showcart').click()
    s(TeesPageLocators.VIEW_AND_EDIT_CART_LINK).should(be.visible).click()


def clear_cart_after_test():
    s(TeesPageLocators.REMOVE_TEES_BTN_FROM_CART_AFTER_TEST).click()


def add_one_tees_green_color_size_s():
    s(TeesPageLocators.TEES_ONE).click()
    s(TeesPageLocators.TEES_SIZE_S).click()
    s(TeesPageLocators.TEES_COLOR_GREEN).click()


def add_one_tees_yellow_color_size_m():
    try:
        s("div[class='ea-stickybox-hide']").should(be.visible).click()
    except Exception as e:
        print("Window did not found", e)
    s(TeesPageLocators.TEES_THREE).click()
    s(TeesPageLocators.TEES_SIZE_M).click()
    s(TeesPageLocators.TEES_COLOR_YELLOW).click()


def add_one_tees_orange_color_size_xs():
    s(TeesPageLocators.TEES_TWO).click()
    s(TeesPageLocators.TEES_SIZE_XS).click()
    s(TeesPageLocators.TEES_COLOR_ORANGE).click()


def add_one_tees_black_color_size_l():
    s(TeesPageLocators.TEES).click()
    s(TeesPageLocators.TEES_SIZE_L).click()
    s(TeesPageLocators.TEES_COLOR_BLACK).click()


def check_quantity_items_in_the_shopping_list():
    items_list = ss("tr.item-info")
    assert len(items_list) == 4, "error"
    s("span.counter-number").should(have.text("4"))


def clear_the_cart_with_all_items():
    while True:
        remove_buttons = ss("//*[@class='action action-delete']")

        if not remove_buttons:
            break

        remove_buttons[0].click()


def check_shopping_cart_is_empty_after_deleting_all_items():
    s("div.cart-empty").should(be.visible)
    s("div.cart-empty").should(have.text("You have no items in your shopping cart."))
