from selene import browser, have, command
from selene.support.shared.jquery_style import s
from selenium.webdriver.support.color import Color

url = "https://magento.softwaretestingboard.com/catalogsearch/advanced/"

BUTTON_SEARCH = '//button[contains(@class, "primary")]'
error_message = s('//div[contains(@class, "error")]/div')
FIELD_PRODUCT_NAME = '#name'
FIELD_SKU = '#sku'
FIELD_DESCRIPTION = '#description'
FIELD_SHORT_DESC = '#short_description'

field_price_from = s('#price')
field_price_to = s('#price_to')
price_error_message = s('#price-error')
price_to_error_message = s('#price_to-error')


def open():
    browser.open(url)

def click_search_button():
    s(BUTTON_SEARCH).perform(command.js.click)

def message_text():
    error_message.should(have.text("Enter a search term and try again."))
    font = Color.from_string('#e02b27').rgba
    error_message.should(have.css_property('color').value(font))

def fill_wrong_price_range():
    price_from = 50
    price_to = 20
    field_price_from.type(price_from)
    field_price_to.type(price_to)

def price_range_error_message():
    price_error_message.should(have.text('Please enter a valid price range.'))
    price_to_error_message.should(have.text('Please enter a valid price range.'))

def fill_prohibited_characters_in_price():
    chars = 'test'
    field_price_from.type(chars)
    field_price_to.type(chars)

def invalid_number_price_error_message():
    price_error_message.should(have.text('Please enter a valid number.'))
    price_to_error_message.should(have.text('Please enter a valid number.'))

def search_by_product_name():
    product_name = 'Jacket'
    s(FIELD_PRODUCT_NAME).type(product_name)

def check_search_result():
    product_name = 'Jacket'
    for item in ss('product-item-link'):
        item.should(have.text(product_name))
