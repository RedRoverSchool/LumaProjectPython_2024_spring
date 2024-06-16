from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s
from selenium.webdriver.support.color import Color

from pages.components.nav import men_top_urls, men_bottoms_urls

base_url = 'https://magento.softwaretestingboard.com'
men_page_url = base_url + '/men.html'
men_top_url = base_url + '/men/tops-men.html'
men_bottoms_url = base_url + '/men/bottoms-men.html'

nav_men = s('#ui-id-5')
page_header = s("#page-title-heading")
error_message = "Men's page did not load successfully"


def get_current_url():
    return browser.driver.current_url


def open_page():
    browser.open(men_page_url)


def check_current_page():
    page_header.should(have.text("Men"))
    assert get_current_url() == men_page_url, error_message


def is_active():
    underline = Color.from_string('#ff5501').rgb
    font = Color.from_string('#333').rgba
    assert nav_men.should(have.css_property('color').value(font))
    assert nav_men.should(have.css_property('border-color').value(underline))


def verify_top_urls(name):
    assert get_current_url() == men_top_urls[name]


def verify_bottoms_urls(name):
    assert get_current_url() == men_bottoms_urls[name]


def visit_men_top_page():
    browser.open(men_top_url)


def visit_bottoms_page():
    browser.open(men_bottoms_url)