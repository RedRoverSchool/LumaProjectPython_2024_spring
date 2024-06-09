from selene import browser, be, have
from selene.support.shared.jquery_style import s

from pages.locators import FooterLocators

practice_api_url = 'https://softwaretestingboard.com/practice-api-testing-using-magento-2/'
practice_api_link = s('//a[text()="PRACTICE API TESTING USING MAGENTO 2"]')
header = s('//h1[text()="Practice API Testing using Magento 2"]')


def visit(url):
    browser.open(url)


def practice_api_link_click():
    practice_api_link.should(be.clickable)
    practice_api_link.click()


def is_current_url_practice_api(url):
    browser.should(have.url(url))


def verify_header_text(text):
    header.should(have.text(text))


def magento_should_have_text(text):
    s(FooterLocators.MAGENTO).should(have.text(text))