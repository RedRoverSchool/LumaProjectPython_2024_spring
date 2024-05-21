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