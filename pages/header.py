from selene import browser
from selene.support.shared.jquery_style import s
from selene import query

product_url = 'https://magento.softwaretestingboard.com/desiree-fitness-tee.html'
cart_counter = s('.counter-label')


def open_product_url():
    browser.open(product_url)


def counter_should_be_equal(qty):
    assert cart_counter.get(query.text) == qty
