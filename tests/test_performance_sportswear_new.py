import allure
from data.links import *
from pages.locators import BaseLocators, LoginLocators, PerformanceSportswear, ProductLocators
from selene import browser, have, command
from selene.support.shared.jquery_style import s, ss
from selene.support.conditions import be, have
from pages import performans_new_page
from selenium.webdriver.common.by import By


@allure.feature(" What's new > Performance Sportswear New > Check count of products")
@allure.link("https://trello.com/c/REIhcQnq")
def test_check_count_of_products(login):
    performans_new_page.visit()
    assert performans_new_page.items_count() == 5


def test_006_008_001_visibility_of_price_photo_name():
    browser.open(LINK_SPORT)
    nr_of_items_on_page = len(ss(BaseLocators.PRODUCT_ITEM_IN_CATALOG))
    ss(BaseLocators.PRODUCT_NAME).should(have.size(nr_of_items_on_page))
    ss(BaseLocators.PRODUCT_PRICE).should(have.size(nr_of_items_on_page))
    ss(BaseLocators.PRODUCT_IMAGE).should(have.size(nr_of_items_on_page))


def test_006_008_002_add_to_cart_from_catalog_without_color_and_size():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    # кликнуть невидимую кнопку - она за пределами экрана и/или не отрисована
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).perform(command.js.click)
    s(PerformanceSportswear.SUCCESS_MESSAGE).should(have.no.text(PerformanceSportswear.TEXT_SUCCESS_MESSAGE))


def test_006_008_002_add_to_cart_from_catalog_without_color_and_size_with_hover():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    # s(PerformanceSportswear.IMAGE_2).should(be.visible).perform(command.js.scroll_into_view)
    s(PerformanceSportswear.IMAGE_2).should(be.visible).hover()
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).should(be.clickable).click()
    s(PerformanceSportswear.SUCCESS_MESSAGE).should(have.no.text(PerformanceSportswear.TEXT_SUCCESS_MESSAGE))


def test_006_008_003_color_and_size_can_be_checked():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    s(PerformanceSportswear.IMAGE_2).click()
    s(ProductLocators.SIZE_XS).click()
    s(ProductLocators.COLOR_BLUE).click()
    selected = ss('[aria-checked="true"]')
    assert len(selected) == 2


def test_006_008_004_add_to_cart_from_product_page_without_color_and_size():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    s(PerformanceSportswear.IMAGE_2).click()
    s(ProductLocators.ADD_TO_CART_BUTTON).click()
    chooses = ss(ProductLocators.SHOULD_CHOOSE_SIZE_AND_COLOR)
    for choose in chooses:
        assert choose.text == ProductLocators.TEXT_REQUIRED_FIELD
