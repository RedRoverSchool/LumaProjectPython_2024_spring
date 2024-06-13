import allure
from pages import header, product
from pages import empty_cart_icon_page


@allure.feature('Header > Cart')
@allure.link('https://trello.com/c/76HixPum')
@allure.title('Verify counter number')
def test_003_003_004_verify_cart_counter_number():
    header.open_product_url()
    product.add_to_cart_with_qty('M', 'Orange', '1')
    header.counter_should_be_equal('1')


@allure.feature('Header > Cart')
@allure.link('https://trello.com/c/L5CT9TYK')
@allure.title('Verify the cart icon is visible and clickable on main page')
def test_the_cart_icon():
    empty_cart_icon_page.open_main_page()
    empty_cart_icon_page.check_the_cart_icon_is_visible()
    empty_cart_icon_page.check_the_cart_icon_is_clickable()
    empty_cart_icon_page.check_open_new_window_after_click_on_the_cart_icon()
