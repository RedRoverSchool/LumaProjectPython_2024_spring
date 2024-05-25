from selene.support.conditions import be
from selene.support.shared.jquery_style import s

product_qty = s('#qty')
add_to_cart_button = s('#product-addtocart-button')
add_to_cart_success_msg = s("//div[contains(text(), 'You added')]")


def add_product_to_cart_with_qty(size, color, qty):
    s(f'[option-label={size}]').click()
    s(f'[option-label={color}]').click()
    product_qty.click() \
        .clear() \
        .type(qty)
    add_to_cart_button.click()
    add_to_cart_success_msg.wait_until(be.visible)

    
def assert_reviews_title_is_visible():
    s("#tab-label-reviews-title").should(be.visible)

