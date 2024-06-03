from selene import browser, have, be, command, by, query
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support.color import Color

url = "https://magento.softwaretestingboard.com/catalogsearch/advanced/"

button_search = s('//button[contains(@class, "primary")]')
error_message = s('//div[contains(@class, "error")]/div')
field_product_name = s('#name')
field_sku = s('#sku')
field_description = s('#description')
field_short_desc = s('#short_description')
field_price_from = s('#price')
field_price_to = s('#price_to')
price_from_error_message = s('#price-error')
price_to_error_message = s('#price_to-error')
results_page_title = s('.page-title')
item_found = s('.product-item-link')
all_items_found = ss('.product-item-link')
item_name = s('.page-title')
item_sku = s('.value')
item_description = s('#description')
item_price = s('#product-price-414')
results_error_message = s('.error')


def open():
    browser.open(url)

def click_search_button():
    button_search.perform(command.js.click)

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
    price_from_error_message.should(have.text('Please enter a valid price range.'))
    price_to_error_message.should(have.text('Please enter a valid price range.'))

def fill_prohibited_characters_in_price():
    chars = 'test'
    field_price_from.type(chars)
    field_price_to.type(chars)

def invalid_number_price_error_message():
    price_from_error_message.should(have.text('Please enter a valid number.'))
    price_to_error_message.should(have.text('Please enter a valid number.'))

def search_by_product_name():
    product_name = 'Jacket'
    field_product_name.type(product_name)

def check_search_result():
    product_name = 'Jacket'
    for item in all_items_found:
        item.should(have.text(product_name))

def fill_in_all_input_fields(product_name, sku, desc, short_desc, price_from, price_to):
    field_product_name.type(product_name)
    field_sku.type(sku)
    field_description.type(desc)
    field_short_desc.type(short_desc)
    field_price_from.type(price_from)
    field_price_to.type(price_to)

def check_full_search_results(product_name, sku, desc, price_from, price_to):
    browser.should(have.title('Advanced Search Results'))
    results_page_title.should(have.text('Catalog Advanced Search'))
    item_found.click()
    item_name.should(have.text(product_name))
    item_sku.should(have.text(sku))
    item_description.should(have.text(desc))
    assert price_from <= int(item_price.get(query.text).split('.')[0][1:]) <= price_to

def fill_non_existent_product_name():
    product_name = 'Sweet potato'
    field_product_name.type(product_name)

def check_search_results_for_non_existent_product():
    results_page_title.should(have.text('Catalog Advanced Search'))
    results_error_message.should(have.text("We can't find any items matching these search criteria. Modify your search."))
    font = Color.from_string('#e02b27').rgba
    results_error_message.should(have.css_property('color').value(font))
    results_error_message.should(be.clickable)
    results_error_message.click()
    browser.should(have.url_containing(url))