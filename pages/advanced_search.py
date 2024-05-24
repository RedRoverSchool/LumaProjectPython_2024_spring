from selene import browser, have, be, command
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support.color import Color


url = "https://magento.softwaretestingboard.com/catalogsearch/advanced/"

BUTTON_SEARCH = '//button[contains(@class, "primary")]'
ERROR_MESSAGE = '//div[contains(@class, "error")]/div'
FIELD_PRODUCT_NAME = '#name'
FIELD_SKU = '#sku'
FIELD_DESCRIPTION = '#description'
FIELD_SHORT_DESC = '#short_description'
FIELD_PRICE_FROM = '#price'
FIELD_PRICE_TO = '#price_to'
PRICE_ERROR_MESSAGE = '#price-error'
PRICE_TO_ERROR_MESSAGE = '#price_to-error'


def open():
    browser.open(url)

def click_button():
    s(BUTTON_SEARCH).perform(command.js.click)

def message_text():
    s(ERROR_MESSAGE).should(have.text("Enter a search term and try again."))
    font = Color.from_string('#e02b27').rgba
    s(ERROR_MESSAGE).should(have.css_property('color').value(font))

def fill_wrong_price_range():
    price_from = 50
    price_to = 20
    s(FIELD_PRICE_FROM).type(price_from)
    s(FIELD_PRICE_TO).type(price_to)

def price_range_error_message():
    s(PRICE_ERROR_MESSAGE).should(have.text('Please enter a valid price range.'))
    s(PRICE_TO_ERROR_MESSAGE).should(have.text('Please enter a valid price range.'))

def fill_prohibited_characters_in_price():
    chars = 'test'
    s(FIELD_PRICE_FROM).type(chars)
    s(FIELD_PRICE_TO).type(chars)

def invalid_number_price_error_message():
    s(PRICE_ERROR_MESSAGE).should(have.text('Please enter a valid number.'))
    s(PRICE_TO_ERROR_MESSAGE).should(have.text('Please enter a valid number.'))