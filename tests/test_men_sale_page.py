import allure
import pytest
from pages import men_sale_page


@pytest.mark.xfail
@allure.feature('Sale > Men’s Deals')
@allure.link('https://trello.com/c/j98xpncK')
@allure.title('Verify Bread Crumbs display')
def test_verify_bread_crumbs_display():
    men_sale_page.open()
    men_sale_page.bread_crumbs_present_should_be_present()
    breadcrumbs = men_sale_page.get_bread_crumbs()
    assert breadcrumbs == men_sale_page.breadcrumbs_path


@allure.feature('Sale > Men’s Deals')
@allure.link('https://trello.com/c/2hWLV7Cf')
@allure.title('Verify page title')
def test_verify_page_title():
    men_sale_page.open()
    men_sale_page.page_title_should_be_present()
    men_sale_page.page_title_should_have_correct_text()


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/wnMvuIUl")
@allure.title("Verify total number of items on the page")
def test_verify_total_number_of_items():
    men_sale_page.open()
    men_sale_page.page_title_should_be_present()
    men_sale_page.page_title_should_have_correct_text()
    men_sale_page.product_list_should_be_present()
    men_sale_page.number_of_items_in_toolbar_should_correspond_to_amount_in_list()


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/PDdDAwh1")
@allure.title("Verify only cards with products for men are present on the page")
def test_verify_only_cards_with_men_products_are_present():
    men_sale_page.open()
    men_sale_page.product_list_should_be_present()
    men_sale_page.only_product_cards_for_men_should_be_present()


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/XCyyXog8")
@allure.title("Check card arrangement according to chosen option")
def test_check_card_arrangement():
    men_sale_page.open()
    men_sale_page.product_list_should_be_present()
    men_sale_page.selected_view_option_should_be("grid")
    men_sale_page.products_in_list_arrangement_should_correspond_to_option("grid")
    men_sale_page.switch_to_display_option("list")
    men_sale_page.products_in_list_arrangement_should_correspond_to_option("list")


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/bDV6XGTp")
@allure.title("Verify sorting product cards by position")
def test_verify_sorting_product_cards_by_position():
    men_sale_page.open()
    men_sale_page.product_list_should_be_present()
    men_sale_page.selected_sorting_option_should_be("Position")
    men_sale_page.switch_to_sorting_option("Price")
    men_sale_page.switch_to_sorting_option("Position")
    men_sale_page.product_arrangement_should_correspond_to_sort_option("Position")


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/CRFlZq0S")
@allure.title("Verify sorting product cards by price")
def test_verify_sorting_product_cards_by_price():
    men_sale_page.open()
    men_sale_page.product_list_should_be_present()
    men_sale_page.selected_sorting_option_should_be("Position")
    men_sale_page.switch_to_sorting_option("Price")
    men_sale_page.product_arrangement_should_correspond_to_sort_option("Price")


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/B85RrqMm")
@allure.title("Verify sorting product cards by product name")
def test_verify_sorting_product_cards_by_name():
    men_sale_page.open()
    men_sale_page.product_list_should_be_present()
    men_sale_page.selected_sorting_option_should_be("Position")
    men_sale_page.switch_to_sorting_option("Product Name")
    men_sale_page.product_arrangement_should_correspond_to_sort_option("Product Name")


@allure.feature('Sale > Men’s Deals')
@allure.link("https://trello.com/c/f30xVqo3")
@allure.title("Verify the contents of each product's card")
def test_verify_contents_of_each_product_card():
    men_sale_page.open()
    men_sale_page.product_list_should_be_present()
    men_sale_page.product_cards_should_have_correct_content()
