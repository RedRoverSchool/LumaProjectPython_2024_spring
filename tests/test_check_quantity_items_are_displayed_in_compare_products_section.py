from pages import compare_items_page
import allure
import pytest

@pytest.mark.skip
@allure.title("check value of selected items to compare products section when compare product section is empty")
def test_check_quantity_value_in_empty_compare_product_section(browser_management):
    compare_items_page.compare_items_values_in_empty_compare_items_section()

@pytest.mark.skip
@allure.title("check selected items from compare products section are deleted after clicking on clear all btn")
def test_check_compare_product_item_section_is_empty_after_click_on_clear_all_btn(browser_management):
    compare_items_page.compare_items_values_in_empty_compare_items_section()
    compare_items_page.clear_compare_product_section_after_test()
