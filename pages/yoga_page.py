from selene import browser
from selene.support.conditions import be
from selene.support.shared.jquery_style import s

yoga_url = 'https://magento.softwaretestingboard.com/collections/yoga-new.html'
yoga_list_url = 'https://magento.softwaretestingboard.com/collections/yoga-new.html?product_list_mode=list'

list_button = s('.modes-mode.mode-list')
grid_button = s('.modes-mode.mode-grid')


def open_page():
    browser.open(yoga_url)


def is_list_button_visible():
    list_button.should(be.visible)


def list_button_click():
    list_button.click()


def is_current_url_yoga():
    return browser.driver.current_url == yoga_url


def is_current_url_list():
    return browser.driver.current_url == yoga_list_url


def open_list_view_page():
    browser.open(yoga_list_url)


def is_grid_button_visible():
    grid_button.should(be.visible)


def grid_button_click():
    grid_button.click()


def is_wrapper_list_view_visible():
    s('.products.wrapper.list').should(be.present).should(be.visible)


def is_wrapper_grid_view_visible():
    s('.products.wrapper.grid').should(be.visible)
