from pages.base_page import BasePage
from selene import browser, have
from selene.support.shared.jquery_style import s

url = 'https://magento.softwaretestingboard.com/search/term/popular/'


def open():
    browser.open(url)


def jacket_link():
    return s('//*[@id="maincontent"]/div[3]/div/ul/li[32]/a')


def card_titles_should_be_matching_to_link():
    s('[class=product-item-link]').should(have.text('Jacket'))


class PopularSearchTerms(BasePage):

    def __init__(self, browser):
        super().__init__(browser)