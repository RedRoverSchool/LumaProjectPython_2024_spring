from selene import browser, have
from selene.support.shared.jquery_style import s

url = "https://magento.softwaretestingboard.com/customer/account/"


def visit():
    browser.open(url)


def should_be_page_title(partial_text):
    s("h1.page-title").should(have.text(partial_text))
