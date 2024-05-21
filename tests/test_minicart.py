import allure
from selene import browser
from selene.support.shared.jquery_style import s

from pages.main_page import MainPage
from pages.locators import ProductLocators as PL


@allure.title("Test MiniCart has link View and edit cart")
class TestMiniCart:

    def test_minicart_has_link(self):
        page = MainPage(browser=browser)
        page.open_page()
        s(PL.RADIANT_TEE_SIZE).click()
        s(PL.RADIANT_TEE_COLOR).click()
        s(PL.ADD_TO_CART_BUTTON_FROM_MAINPAGE).click()
        page.is_cart_icon_present()
        page.click_cart_icon()
        page.mini_card.is_mini_cart_present()
        page.mini_card.is_minicart_have_link()

    @allure.link('https://trello.com/c/WVaLK93g')
    def test_add_to_cart_from_main(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()

    @allure.link('https://trello.com/c/WVaLK93g')
    def test_color_and_clickability_of_view_and_edit_cart_link_in_the_mini_cart_tc_005_001_011(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        page.mini_card.check_color_of_in_the_mini_cart("#006bb4")
        page.mini_card.check_edit_cart_link_in_the_mini_cart()

    @allure.link('https://trello.com/c/w8Of4GYe')
    def test_checking_the_link_opens_the_cart_page_tc_005_001_012(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        page.mini_card.check_the_link_opens_checkout_cart_page()

    @allure.link("https://trello.com/c/v4hVrwzq")
    def test_size_color_and_product_name_are_correct_tc_005_001_013(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        page.mini_card.checking_the_size_color_and_product_name_are_correct()

    @allure.link("https://trello.com/c/p6iExP1c")
    def test_checking_present_price_item_and_cart_subtotal_in_the_mini_cart_tc_005_001_014(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        page.mini_card.should_be_change_subtotal("$22.00", "$22.00")

    @allure.link("https://trello.com/c/uCZZgQks")
    def test_change_quantity_of_an_item_and_changes_price_in_cart_subtotal_mini_cart_tc_005_001_015(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.add_to_cart_from_main_page()
        page.is_counter_number_visible()
        page.go_to_mini_cart()
        page.mini_card.should_be_success_message()
        page.mini_card.change_qty("7")
        page.mini_card.should_be_quantity_change("7")
        page.mini_card.should_be_change_subtotal("$22.00", "$154.00")
