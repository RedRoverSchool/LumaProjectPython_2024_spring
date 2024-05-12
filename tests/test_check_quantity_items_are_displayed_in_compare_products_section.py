import data.page_data
import data.links
import pages
from pages import locators
from pages import sign_in
import allure
from selene import browser, be, have, by
from selene.support.shared.jquery_style import s
import pytest


@pytest.mark.skip
@allure.title("check value of selected items to compare products section")
def test_check_quantity_value_in_compare_product_section(browser_management):
    browser.open(pages.locators.LoginLocators.LINK_LOGIN)
    sign_in.login(data.page_data.SignInData.email, data.page_data.SignInData.password)
    browser.element(pages.locators.SalePageLocators.SALE_TAP).click()
    browser.should(have.url(data.links.SALE_SECTION_LINK))
    browser.element(pages.locators.SaleWomenDealsLocators.JACKETS).click()
    s(pages.locators.SaleWomenDealsLocators.ELEMENT_ONE).hover()
    s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE).hover().click()
    s(pages.locators.SaleWomenDealsLocators.ELEMENT_TWO).wait_until(be.present)
    s(pages.locators.SaleWomenDealsLocators.ELEMENT_TWO).hover()
    s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).wait_until(be.present)
    s(pages.locators.SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).hover().click()
    s(pages.locators.SaleWomenDealsLocators.QUANTITY_ITEMS).should(have.text("2 items"))
    s(by.id("compare-clear-all")).click()
    s(by.css("button[class='action-primary action-accept']")).wait_until(be.present)
    s(by.css("button[class='action-primary action-accept']")).click()
