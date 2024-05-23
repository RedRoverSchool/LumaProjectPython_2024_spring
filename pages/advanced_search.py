from selene import browser, have, be, command
from selene.support.shared.jquery_style import s, ss
from pages.locators import AdvancedSearchLocators as AS
from selenium.webdriver.support.color import Color


url = "https://magento.softwaretestingboard.com/catalogsearch/advanced/"


def open():
    browser.open(url)

def click_button():
    s(AS.BUTTON_SEARCH).perform(command.js.click)

def message_text():
    s(AS.ERROR_MESSAGE).should(have.text("Enter a search term and try again."))
    font = Color.from_string('#e02b27').rgba
    s(AS.ERROR_MESSAGE).should(have.css_property('color').value(font))

def fill_wrong_price_range():
    price_from = 50
    price_to = 20
    s(AS.FIELD_PRICE_FROM).type(price_from)
    s(AS.FIELD_PRICE_TO).type(price_to)

def price_range_error_message():
    s(AS.PRICE_ERROR_MESSAGE).should(have.text('Please enter a valid price range.'))
    s(AS.PRICE_TO_ERROR_MESSAGE).should(have.text('Please enter a valid price range.'))

def fill_prohibited_characters_in_price():
    chars = 'test'
    s(AS.FIELD_PRICE_FROM).type(chars)
    s(AS.FIELD_PRICE_TO).type(chars)

def invalid_number_price_error_message():
    s(AS.PRICE_ERROR_MESSAGE).should(have.text('Please enter a valid number.'))
    s(AS.PRICE_TO_ERROR_MESSAGE).should(have.text('Please enter a valid number.'))