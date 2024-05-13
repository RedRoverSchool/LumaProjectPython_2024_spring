from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/collections/performance-new.html"


def visit():
    browser.open(url)


def items_count():
    return len(ss('.product-item-info'))




