from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/wishlist/"


def visit():
    browser.open(url)


def click_update():
    s(".update").click()


def should_be_clickable():
    s(".update").should(be.clickable)


def url_should_contain(param):
    browser.should(have.url_containing(param))
