from selene import browser, have
from selene.support.shared.jquery_style import s
from data.links import *


def visit():
    browser.open(SALE_PAGE_LINK)


def page_title():
    s("h1.page-title").should(have.text('Sale'))


def redirect():
    browser.should(have.url(SALE_PAGE_LINK))