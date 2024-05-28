from selene import browser, have, be, command, by, query
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
RESULTS_PAGE_TITLE = by.class_name("page-title")
ITEM_FOUND = by.class_name('product-item-link')
ITEM_NAME = by.class_name('page-title')
ITEM_SKU = by.class_name('value')
ITEM_DESCRIPTION = '#description'
ITEM_PRICE = '#product-price-414'


def open():
    browser.open(url)

def click_search_button():
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

def search_by_product_name():
    product_name = 'Jacket'
    s(FIELD_PRODUCT_NAME).type(product_name)

def check_search_result():
    product_name = 'Jacket'
    for item in ss(ITEM_FOUND):
        item.should(have.text(product_name))

def fill_in_all_input_fields(product_name, sku, desc, short_desc, price_from, price_to):
    s(FIELD_PRODUCT_NAME).type(product_name)
    s(FIELD_SKU).type(sku)
    s(FIELD_DESCRIPTION).type(desc)
    s(FIELD_SHORT_DESC).type(short_desc)
    s(FIELD_PRICE_FROM).type(price_from)
    s(FIELD_PRICE_TO).type(price_to)

def check_full_search_results(product_name, sku, desc, price_from, price_to):
    browser.should(have.title('Advanced Search Results'))
    s(RESULTS_PAGE_TITLE).should(have.text('Catalog Advanced Search'))
    s(ITEM_FOUND).click()
    s(ITEM_NAME).should(have.text(product_name))
    s(ITEM_SKU).should(have.text(sku))
    s(ITEM_DESCRIPTION).should(have.text(desc))
    assert price_from <= int(s(ITEM_PRICE).get(query.text).split('.')[0][1:]) <= price_to