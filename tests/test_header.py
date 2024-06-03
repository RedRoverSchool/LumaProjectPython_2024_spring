import allure
from pages import header, product


@allure.link('https://trello.com/c/76HixPum')
@allure.title('TC_003.003.004 | Header > Cart> Verify counter number')
def test_003_003_004_verify_cart_counter_number():
    header.open_product_url()
    product.add_to_cart_with_qty('M', 'Orange', '1')
    header.counter_should_be_equal('1')
