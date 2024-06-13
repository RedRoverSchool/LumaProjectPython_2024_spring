import allure

from pages import whats_new


@allure.feature("What's new")
@allure.link('https://trello.com/c/jgLmzBZX')
@allure.feature("Eco Collection New")
def test_add_product_to_wishlist_as_non_logged_in_user():
    with allure.step("Assert current url == What's New Page url"):
        whats_new.open_page()
        whats_new.is_current_link()
    with allure.step("Click button new yoga"):
        whats_new.is_button_visible()
        whats_new.click_button_shop_new_yoga()
    with allure.step("Go to product item"):
        whats_new.hover_on_product()
    with allure.step("Add to Wish List"):
        whats_new.click_on_wish_list()
    with allure.step("Redirect to Customer Login and verify message"):
        whats_new.check_redirection_to_login()
