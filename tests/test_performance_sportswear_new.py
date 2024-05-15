import allure

from pages import performans_new_page


@allure.feature(" What's new > Performance Sportswear New > Check count of products")
@allure.link("https://trello.com/c/REIhcQnq")
def test_check_count_of_products(login):
    performans_new_page.visit()
    assert performans_new_page.items_count() == 5

@allure.feature("What's new > Performance Sportswear> NewEach product card contains buttons for adding to cart, adding to wishlist and adding to comparison list")
@allure.link("https://trello.com/c/YuNxu4x4")
def test_product_card_buttons(login, product_card_button:
    performans_new_page.visit()
    add_to_cart_button.should(be.visible)
    add_to_wishlist_button.should(be.visible)
    add_to_comparison_button.should(be.visible)


