import allure
import pytest

from pages import performans_new_page, sign_in, product


@allure.feature("What's new > Performance Sportswear New")
@allure.title('Check count of products')
@allure.link("https://trello.com/c/REIhcQnq")
def test_check_count_of_products(login):
    performans_new_page.visit()
    assert performans_new_page.items_count() == 5


@allure.feature("What's new > Performance Sportswear")
@allure.title('Verify that each product card includes buttons for adding to the cart, wishlist, and comparison list')
@allure.link("https://trello.com/c/YuNxu4x4")
def test_product_card_buttons(login):
    performans_new_page.visit()
    performans_new_page.check_buttons()


@allure.feature('Whats new > Performance Sportswear New')
@allure.title('Visibility of Product name, its Price and Photo')
@allure.link("https://trello.com/c/9B5bXFEP")
def test_visibility_of_price_photo_name():
    performans_new_page.visit()
    nr = performans_new_page.items_count()
    performans_new_page.compare_nr_of_items_and_nr_of_names(nr)
    performans_new_page.compare_nr_of_items_and_nr_of_images(nr)
    performans_new_page.compare_nr_of_items_and_nr_of_prices(nr)


@allure.feature("What's new > Performance Sportswear New")
@allure.link("https://trello.com/c/cmwZ3A6P")
@allure.title(
    'Clicking on the button "Add to Cart" in the catalog without selecting the color and size of the product previously')
def test_add_to_cart_from_catalog_without_color_and_size():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.click_button_add_to_cart_with_js()
    performans_new_page.check_no_success_message()


@allure.feature("What's new > Performance Sportswear New")
@allure.link("https://trello.com/c/cmwZ3A6P")
@allure.title(
    'Clicking on button "Add to Cart" in the catalog without selecting the color and size of the product previously')
def test_add_to_cart_from_catalog_without_color_and_size_with_hover():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.click_button_add_to_cart_with_hover()
    performans_new_page.check_no_success_message()


@allure.feature("What's new > Performance Sportswear New")
@allure.link("https://trello.com/c/WjUokO7r")
@allure.title('Color and measure can be chosen')
def test_color_and_size_can_be_checked():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.go_to_product_helios_endurance_tank()
    performans_new_page.select_size_xs()
    performans_new_page.select_color_blue()
    performans_new_page.verify_if_color_and_size_were_selected()


@allure.feature("What's new > Performance Sportswear New")
@allure.title('Click the button "Add to Cart" in the product card without selecting color and measure')
@allure.link("https://trello.com/c/dYQgmbfJ")
def test_add_to_cart_from_product_page_without_color_and_size():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    performans_new_page.visit()
    performans_new_page.go_to_product_helios_endurance_tank()
    performans_new_page.press_button_add_to_cart()
    performans_new_page.check_msg_no_required_field_color()
    performans_new_page.check_msg_no_required_field_size()


@allure.feature("What's new > Performance Sportswear New")
@allure.link("https://trello.com/c/mjKfokpO")
@allure.title('Each product card displays the product rating and the number of reviews')
@pytest.mark.parametrize("product_name", ["Hyperion Elements Jacket", "Helios Endurance Tank", "Ingrid Running Jacket",
                                          "Juliana Short-Sleeve Tee", "Gwen Drawstring Bike Short"])
def test_product_review_section(login, product_name):
    performans_new_page.visit()
    performans_new_page.click_product_review(product_name)
    product.assert_reviews_title_is_visible()
