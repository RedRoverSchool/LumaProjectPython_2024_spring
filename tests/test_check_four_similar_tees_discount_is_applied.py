import allure
import pytest

from pages import tees_page


# @pytest.mark.skip
@allure.title("Check four tees for three with similar tess is applied")
def test_four_tees_discount_is_apply_for_similar_tees(browser_management):
    tees_page.open_login_page()
    tees_page.click_on_four_tees_discount_banner()
    tees_page.add_four_same_model_tees()
    tees_page.click_on_add_to_cart_btn()
    tees_page.click_on_the_shopping_cart_icon()
    tees_page.check_discount_is_applied_for_four_similar_tees()
    tees_page.clear_cart_after_test()
