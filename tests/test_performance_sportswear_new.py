import allure
import pytest

from pages import performans_new_page, sign_in, product


@allure.feature(" What's new > Performance Sportswear New > Check count of products")
@allure.link("https://trello.com/c/REIhcQnq")
def test_check_count_of_products(login):
    performans_new_page.visit()
    assert performans_new_page.items_count() == 5

@allure.feature("What's new > Performance Sportswear> NewEach product card contains buttons for adding to cart, adding to wishlist and adding to comparison list")
@allure.link("https://trello.com/c/YuNxu4x4")
def test_product_card_buttons(login):
    performans_new_page.visit()
    performans_new_page.check_buttons()


@allure.link("https://trello.com/c/9B5bXFEP")
def test_006_008_001_visibility_of_price_photo_name():
    performans_new_page.visit()
    nr = performans_new_page.items_count()
    performans_new_page.compare_nr_of_items_and_nr_of_names(nr)
    performans_new_page.compare_nr_of_items_and_nr_of_images(nr)
    performans_new_page.compare_nr_of_items_and_nr_of_prices(nr)


@allure.link("https://trello.com/c/cmwZ3A6P")
def test_006_008_002_add_to_cart_from_catalog_without_color_and_size():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.click_button_add_to_cart_with_js()
    performans_new_page.check_no_success_message()


@allure.link("https://trello.com/c/cmwZ3A6P")
def test_006_008_002_add_to_cart_from_catalog_without_color_and_size_with_hover():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.click_button_add_to_cart_with_hover()
    performans_new_page.check_no_success_message()


@allure.link("https://trello.com/c/WjUokO7r")
def test_006_008_003_color_and_size_can_be_checked():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.go_to_product_helios_endurance_tank()
    performans_new_page.select_size_xs()
    performans_new_page.select_color_blue()
    performans_new_page.verify_if_color_and_size_were_selected()


@allure.link("https://trello.com/c/dYQgmbfJ")
def test_006_008_004_add_to_cart_from_product_page_without_color_and_size():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.go_to_product_helios_endurance_tank()
    performans_new_page.press_button_add_to_cart()
    performans_new_page.check_msg_no_required_field_color()
    performans_new_page.check_msg_no_required_field_size()


@allure.feature("TC_006.008.10 | What's new > Performance Sportswear New > Each product card displays the product rating and the number of reviews")
@allure.link("https://trello.com/c/mjKfokpO")
@pytest.mark.parametrize("product_name", ["Hyperion Elements Jacket", "Helios Endurance Tank", "Ingrid Running Jacket", "Juliana Short-Sleeve Tee", "Gwen Drawstring Bike Short"])
def test_product_review_section(login, product_name):
    performans_new_page.visit()
    performans_new_page.click_product_review(product_name)
    product.assert_reviews_title_is_visible()


