from selene import browser, be, have
from selene import browser, be, have, Element
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/collections/performance-new.html"


def visit():
    browser.open(url)


def items_count():
    return len(ss('.product-item-info'))


def check_buttons():
    for product_card in ss('.product-item'):
        product_card.hover()
        product_card.s(".actions-primary").should(be.visible)
        product_card.s(".actions-secondary").should(be.visible)
        product_card.s(".action.tocompare").should(be.visible)


