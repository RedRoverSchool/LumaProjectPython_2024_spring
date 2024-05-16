from pages.locators import *
from pages import sign_in
from selene import browser, be, have, by
from selene.support.shared.jquery_style import s
from data.page_data import *

login_url = LoginLocators()
user_email = SignInData()
user_password = SignInData()
sale_page_section = SalePageLocators()
jacket_sale_women_section = SaleWomenDealsLocators()


def compare_items_values_in_empty_compare_items_section():
    browser.open(LoginLocators.LINK_LOGIN)
    sign_in.login(SignInData.email, SignInData.password)
    browser.element(SalePageLocators.SALE_TAB).click()
    s(by.text("You have no items to compare.")).should(be.visible)
    s(SaleWomenDealsLocators.JACKETS).click()
    s(SaleWomenDealsLocators.ELEMENT_ONE).hover()
    s(SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE).hover().click()
    s(SaleWomenDealsLocators.ELEMENT_TWO).should(be.visible)
    s(SaleWomenDealsLocators.ELEMENT_TWO).hover()
    s(SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).should(be.visible)
    s(SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).hover().click()
    s(SaleWomenDealsLocators.QUANTITY_ITEMS).should(have.text("2 items"))


def clear_compare_product_section_after_test():
    s(by.id("compare-clear-all")).should(be.visible).click()
    s(by.css("button[class='action-primary action-accept']")).should(be.visible)
    s(by.css("button[class='action-primary action-accept']")).click()
    s(by.text("You cleared the comparison list.")).should(be.visible)
    s(by.text("You cleared the comparison list.")).should(have.text("You cleared the comparison list."))
