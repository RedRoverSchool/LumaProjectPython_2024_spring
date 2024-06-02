import time

import allure
import pytest
from pages import men_sale_page


@pytest.mark.xfail
@allure.link('https://trello.com/c/j98xpncK/402-tc011012001-sale-mens-deals-verify-bread-crumbs-display')
@allure.title('Verify Bread Crumbs display')
def test_verify_bread_crumbs_display():
    page = men_sale_page
    page.open()
    page.bread_crumbs_present_should_be_present()
    breadcrumbs = page.get_bread_crumbs()
    assert breadcrumbs == men_sale_page.breadcrumbs_path


@allure.link('https://trello.com/c/2hWLV7Cf')
@allure.title('Verify page title')
def test_verify_page_title():
    page = men_sale_page
    page.open()
    page.page_title_should_be_present()
    page.page_title_should_have_correct_text()


@allure.link("https://trello.com/c/wnMvuIUl")
@allure.title("Verify total number of items on the page")
def test_verify_total_number_of_items():
    page = men_sale_page
    page.open()
    page.page_title_should_be_present()
    page.page_title_should_have_correct_text()
    page.product_list_should_be_present()
    page.number_of_items_in_toolbar_should_correspond_to_amount_in_list()


@allure.link("https://trello.com/c/PDdDAwh1")
@allure.title("Verify only cards with products for men are present on the page")
def test_verify_only_cards_with_men_products_are_present():
    page = men_sale_page
    page.open()
    page.product_list_should_be_present()
    page.only_product_cards_for_men_should_be_present()


@allure.link("https://trello.com/c/XCyyXog8")
@allure.title("Check card arrangement according to chosen option")
def test_check_card_arrangement():
    page = men_sale_page
    page.open()
    page.product_list_should_be_present()
    page.selected_view_option_should_be("grid")
    page.products_in_list_arrangement_should_correspond_to_option("grid")
    page.switch_to_display_option("list")
    page.products_in_list_arrangement_should_correspond_to_option("list")


@allure.link("https://trello.com/c/bDV6XGTp")
@allure.title("Verify sorting product cards by position")
def test_verify_sorting_product_cards_by_position():
    page = men_sale_page
    page.open()
    page.product_list_should_be_present()
    page.selected_sorting_option_should_be("Position")
    page.switch_to_sorting_option("Price")
    page.switch_to_sorting_option("Position")
    page.product_arrangement_should_correspond_to_sort_option("Position")


@allure.link("https://trello.com/c/CRFlZq0S")
@allure.title("Verify sorting product cards by price")
def test_verify_sorting_product_cards_by_price():
    page = men_sale_page
    page.open()
    page.product_list_should_be_present()
    page.selected_sorting_option_should_be("Position")
    page.switch_to_sorting_option("Price")
    page.product_arrangement_should_correspond_to_sort_option("Price")


@allure.link("https://trello.com/c/B85RrqMm")
@allure.title("Verify sorting product cards by product name")
def test_verify_sorting_product_cards_by_name():
    page = men_sale_page
    page.open()
    page.product_list_should_be_present()
    page.selected_sorting_option_should_be("Position")
    page.switch_to_sorting_option("Product Name")
    page.product_arrangement_should_correspond_to_sort_option("Product Name")


@allure.link("https://trello.com/c/f30xVqo3")
@allure.title("Verify the contents of each product's card")
def test_verify_contents_of_each_product_card():
    page = men_sale_page
    page.open()
    page.product_list_should_be_present()
    page.product_cards_should_have_correct_content()
    # page.product_cards_should_have_title()
    # page.product_cards_should_have_price()
    # page.product_cards_should_have_image()
    # page.product_cards_should_have_available_sizes_list()
    # page.product_cards_should_have_available_colors_list()
