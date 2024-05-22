import time
import allure
from pages import women_page, shipping_page, payment_page


@allure.link("https://trello.com/c/6IIncPjn")
def test_004_001_002_guest_user_checkout_from_minicart_RF():
    women_page.visit()
    # choose item
    women_page.choose_size_for_tank()
    women_page.choose_color_for_tank()
    women_page.button_add_to_cart_tank()
    time.sleep(4)
    women_page.success_msg_is_present()
    # open minicart
    women_page.open_minicart()
    women_page.open_checkout()
    # fill address
    shipping_page.check_if_this_is_page_for_shipping()
    shipping_page.fill_field_email()
    shipping_page.fill_field_first_name()
    shipping_page.fill_field_last_name()
    shipping_page.fill_field_street()
    shipping_page.fill_field_city()
    shipping_page.fill_field_region()
    shipping_page.fill_field_zipcode()
    shipping_page.fill_field_country()
    shipping_page.fill_field_phone()
    shipping_page.choose_shipping_method()
    shipping_page.go_to_order()
    payment_page.check_if_this_is_page_for_payment()
    # check data and place order
    payment_page.click_button_place_order()
    payment_page.check_message_about_oder_nr()
    payment_page.check_success_message()

