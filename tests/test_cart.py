import allure
from selene import browser, have
from pages.main_page import MainPage
from pages import main_page, cart, bags


@allure.feature('Main Page>Cart')
@allure.title("TC_005.001.004 Checking the quantity is able to change")
@allure.link('https://trello.com/c/tGCH9Kif')
def test_the_quantity_of_item_in_the_cart_is_able_to_change():
    main_page.open_page()
    main_page.add_item_to_cart()
    cart.open_page()
    cart.set_value_of_qty('2')
    cart.click_update_shopping_cart_button()
    cart.is_counter_number_visible()
    cart.counter_number.should(have.text('2'))


@allure.feature('Main Page>Cart')
@allure.title('TC_005.001.005 Checking the product is deleted from the cart')
@allure.link('https://trello.com/c/L4n3T6W3')
def test_the_product_is_deleted_from_the_cart():
    main_page.open_page()
    main_page.add_item_to_cart()
    cart.open_page()
    cart.is_find_remove_item_icon_present()
    cart.delete_product_from_cart()
    cart.should_be_message_no_items('You have no items in your shopping cart.')
    cart.should_be_message_click('Click here to continue shopping.')


@allure.feature('Main Page>Cart')
@allure.title('ТС_005.001.016 View and edit cart>Checking that the size color product-image and product name')
@allure.link("https://trello.com/c/lvLslLGD")
def test_size_color_and_product_name_are_correct_in_the_checkout_cart_page():
    page = MainPage(browser=browser)
    page.open_page()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    cart_page = page.go_to_checkout_cart()
    cart_page.checking_product_name_are_correct_in_checkout_cart_page()
    cart_page.checking_size_are_correct_in_checkout_cart_page("M")
    cart_page.checking_color_are_correct_in_checkout_cart_page("Gray")


@allure.feature('Main Page>Cart')
@allure.title('ТС_005.001.017 View and edit cart>Check price Quantity and Cart Subtotal present in Cart page')
@allure.link("https://trello.com/c/SQ3op4DX")
def test_check_price_qty_and_cart_subtotal_present_in_checkout_cart_page():
    page = MainPage(browser=browser)
    page.open_page()
    page.add_to_cart_from_main_page()
    page.is_counter_number_visible()
    page.go_to_mini_cart()
    cart_page = page.go_to_checkout_cart()
    cart_page.check_price_present_in_checkout_cart_page("$22.00")
    cart_page.check_subtotal_present_in_checkout_cart_page()
    cart_page.check_qty_present_in_checkout_cart_page()


@allure.feature('Sign in & Registration')
@allure.link('https://trello.com/c/YNtpKcN1')
@allure.title('TC_004.001.004 Sign in & Registration, Account > Anonym User can change item quantity in the cart')
def test_item_quantity_updating_by_anonym_user():
    bags.open()
    bags.add_item_to_cart()
    cart.click_cart_icon()
    bags.view_and_edit_card_button().click()
    cart.counter_should_be_equal('1')
    cart.set_value_of_qty('2')
    cart.update_shopping_cart_button().click()
    cart.counter_should_be_equal('2')
    cart.cart_subtotal_should_be_calculated_with_qty_equal(2)
