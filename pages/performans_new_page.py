from selene import browser, be, have
from selene import browser, be, have, Element
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/collections/performance-new.html"


def visit():
    browser.open(url)


def items_count():
    return len(ss('.product-item-info'))


def product_card_buttons():
    global product_card
    product_cards = ss('.product-image-container')
    for i, product_card in enumerate(product_cards[:5]):
        product_card.hover()
    add_to_cart_button = product_card.s(".actions-primary")
    add_to_wishlist_button = product_card.s(".actions-secondary")
    add_to_comparison_button = product_card.s(".action.tocompare")


