import allure
from selene.support.shared.jquery_style import s
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
        s(PL.RADIANT_TEE_SIZE).click()
        s(PL.RADIANT_TEE_COLOR).click()
        s(PL.ADD_TO_CART_BUTTON_FROM_MAINPAGE).click()
        page.is_cart_icon_present()
        page.find_cart_icon().click()
        page.is_minicart_present()
        page.is_minicart_view_present()
        page.is_minicart_view_enable()
        page.find_minicart_view().click()
        page_cart.set_value_of_qty()
        page_cart.is_update_shopping_cart_button_present()
        page_cart.find_update_shopping_cart_button().click()
        page.is_counter_number_present()
        page.find_counter_number().should(have.text('2'))