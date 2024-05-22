import allure

from pages import whats_new_page


@allure.link('https://trello.com/c/jgLmzBZX')
@allure.suite("US_006.004 | What's new > Eco Collection New")
@allure.feature("TC_006.004.005 | What's new > Eco Collection New")
def test_add_product_to_wishlist_as_non_logged_in_user():
    with allure.step("Assert current url == What's New Page url"):
        whats_new_page.open_page()
        whats_new_page.is_current_link()
    with allure.step("Click button new yoga"):
        whats_new_page.is_button_visible()
        whats_new_page.click_button_shop_new_yoga()
    with allure.step("Go to product item"):
        whats_new_page.hover_on_product()
    with allure.step("Add to Wish List"):
        whats_new_page.click_on_wish_list()
    with allure.step("Redirect to Customer Login and verify message"):
        whats_new_page.check_redirection_to_login()
