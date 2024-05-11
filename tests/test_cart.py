import allure

from selene import browser, have, be
from pages.main_page import MainPage
from pages.cart_page import CartPage


@allure.title("Test Checking the quantity of item in the cart is able to change")
class TestCart:
    def test_the_quantity_of_item_in_the_cart_is_able_to_change(self):
        value_of_qty = '2'
        page_cart = CartPage(browser=browser)
        page = MainPage(browser=browser)

        page.open_page()
        page.add_item_to_cart('[option-label="XS"]', '[option-label="Orange"]', 'form[data-product-sku="WS12"] button')

        page_cart.open_page()
        page_cart.set_value_of_qty(value_of_qty)
        page_cart.click_update_shopping_cart_button()
        page_cart.find_counter_number().should(be.visible)
        page_cart.find_counter_number().should(have.text(value_of_qty))
