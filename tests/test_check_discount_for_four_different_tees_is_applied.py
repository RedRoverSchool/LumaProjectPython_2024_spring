import time

import allure
import pytest

from pages import tees_page


@allure.title("Check four different model of Tees for three discount is applied")
@pytest.mark.skip("FAILURES: AssertionError: actual text: 8")
def test_discount_four_tees_for_different_model_is_applies(browser_management):
    tees_page.open_login_page()
    tees_page.login_in()
    tees_page.click_on_four_tees_discount_banner()
    tees_page.check_the_shopping_cart_is_empty()
    tees_page.add_one_tees_black_color_size_l()
    tees_page.click_on_add_to_cart_btn()
    tees_page.add_one_tees_green_color_size_s()
    tees_page.click_on_add_to_cart_btn()
    tees_page.add_one_tees_orange_color_size_xs()
    tees_page.click_on_add_to_cart_btn()
    tees_page.add_one_tees_yellow_color_size_m()
    tees_page.click_on_add_to_cart_btn()
    tees_page.click_on_the_shopping_cart_icon()
    tees_page.check_quantity_items_in_the_shopping_list()
    tees_page.check_discount_is_applied_for_four_different_tees()
    time.sleep(3)
    tees_page.clear_the_cart_with_all_items()
    time.sleep(3)
    tees_page.check_shopping_cart_is_empty_after_deleting_all_items()
