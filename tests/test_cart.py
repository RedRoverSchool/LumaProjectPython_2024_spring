import allure

from selene import browser, have
from pages.main_page import MainPage
from pages import cart
from pages import bags


@allure.title("Test Checking the quantity of item in the cart is able to change")
class TestCart:
    def test_the_quantity_of_item_in_the_cart_is_able_to_change(self):
        value_of_qty = '2'
        page_cart = cart
        page = MainPage(browser=browser)

        page.open_page()
        page.add_item_to_cart('[option-label="XS"]', '[option-label="Orange"]', 'form[data-product-sku="WS12"] button')

        page_cart.open_page()
        page_cart.set_value_of_qty(value_of_qty)
        page_cart.click_update_shopping_cart_button()
        page_cart.is_counter_number_visible()
        page_cart.counter_number.should(have.text(value_of_qty))


    def test_the_product_is_deleted_from_the_cart(self):

        page_cart = cart
        page = MainPage(browser=browser)

        page.open_page()
        page.add_item_to_cart('[option-label="XS"]', '[option-label="Orange"]', 'form[data-product-sku="WS12"] button')

        page_cart.open_page()
        page_cart.is_find_remove_item_icon_present()
        page_cart.remove_item_icon().click()
        page_cart.should_be_message_no_items('You have no items in your shopping cart.')
        page_cart.should_be_message_click('Click here to continue shopping.')


    @allure.link("https://trello.com/c/lvLslLGD")
    def test_size_color_and_product_name_are_correct_in_the_checkout_cart_page_tc_005_001_016(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        cart_page = page.go_to_checkout_cart()
        cart_page.checking_product_name_are_correct_in_checkout_cart_page()
        cart_page.checking_size_are_correct_in_checkout_cart_page("M")
        cart_page.checking_color_are_correct_in_checkout_cart_page("Gray")

    @allure.link("https://trello.com/c/SQ3op4DX")
    def test_check_price_qty_and_cart_subtotal_present_in_checkout_cart_page_tc_005_001_017(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        cart_page = page.go_to_checkout_cart()
        cart_page.check_price_present_in_checkout_cart_page("$22.00")
        cart_page.check_subtotal_present_in_checkout_cart_page()
        cart_page.check_qty_present_in_checkout_cart_page()

    @allure.link('https://trello.com/c/YNtpKcN1')
    @allure.title('TC_004.001.004 | Sign in & Registration, Account > Anonym User can change item quantity in the cart')
    def test_item_quantity_updating_by_anonym_user(self):
        bags.open()
        bags.add_item_to_cart()
        cart.click_cart_icon()
        bags.view_and_edit_card_button().click()
        cart.counter_should_be_equal('1')
        cart.set_value_of_qty('2')
        cart.update_shopping_cart_button().click()
        cart.counter_should_be_equal('2')
        cart.cart_subtotal_should_be_calculated_with_qty_equal(2)
