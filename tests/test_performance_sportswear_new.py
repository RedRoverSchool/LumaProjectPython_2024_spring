import allure
from data.links import *
from pages.locators import BaseLocators
from selene import browser, have
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

