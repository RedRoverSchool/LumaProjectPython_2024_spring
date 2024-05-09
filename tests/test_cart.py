import time

import allure

from selene import browser, have
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.locators import ProductLocators as PL

@allure.title("Test Checking the quantity of item in the cart is able to change")
class TestCart:
    def test_the_quantity_of_item_in_the_cart_is_able_to_change(self):
        page_cart = CartPage(browser=browser)
        page = MainPage(browser=browser)
        page.open_page()
        page.add_item_to_cart(PL.RADIANT_TEE_SIZE, PL.RADIANT_TEE_COLOR, PL.ADD_TO_CART_BUTTON_FROM_MAINPAGE)
        page_cart.open_page()
        page_cart.set_value_of_qty('2')
        time.sleep(3)
        page_cart.is_counter_number_present()
        page_cart.find_counter_number().should(have.text('2'))