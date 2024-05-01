import allure
from selene import browser, by, be, have, support
from selene.support.shared.jquery_style import s
#from selene.api import s, ss

base_url = "https://magento.softwaretestingboard.com/"
TITLE_ITEM = ("xpath", "//a[@title='Breathe-Easy Tank']")
SIZE_BTN = ("xpath", "//*[@id='option-label-size-143-item-167']")
COLOR_BTN = ("xpath", "//*[@id='option-label-color-93-item-59']")
ADD_TO_CATT_BTN = ("xpath", "//*[@id='product-addtocart-button']/span")
#SUCCESS_MESSAGE = ("xpath", "//span[contains(text(), 'You added Breathe-Easy Tank to your shopping cart.')]")
CART_ICON = ("//*[@class='action showcart']")
VIEW_AND_EDIT_CART_BLUE_TEXT = ("xpath", "//*[@id='minicart-content-wrapper']/div[2]/div[5]/div/a/span")
a = '//*[@class="action showcart"]'

LINK_CHECKOUT = "https://magento.softwaretestingboard.com/checkout/cart/"


def open_main_page():
    browser.open(base_url)


def click_title_item():
    s("//a[@title='Breathe-Easy Tank']").click()

def click_size_button():
    s("//*[@id='option-label-size-143-item-167']").click()


def click_color_button():
    s("//*[@id='option-label-color-93-item-59']").click()


def click_add_to_cart_button():
    s("#product-addtocart-button").click()
    browser.config.timeout = 5


# def click_cart_icon():
#     #s(CART_ICON).should(be.visible)
#     s("//*[@class='action showcart']").click()

def click_cart_icon2():
    browser.wait_until(s("//*[@class='action showcart']"))
    s("//*[@class='action showcart']").click()


# def assert_view_and_edit_cart_blue_text():
#     s(by.xpath(VIEW_AND_EDIT_CART_BLUE_TEXT)).should(be.present)
#     assert_view_and_edit_cart_blue_text()

# def assert_view_and_edit_cart_blue_text():
#     s(by.xpath(VIEW_AND_EDIT_CART_BLUE_TEXT)).should(be.present)


def assert_view_and_edit_cart_blue_text():
    # s(by.xpath(VIEW_AND_EDIT_CART_BLUE_TEXT[1])).should(be.present)
    browser.wait_until(s(VIEW_AND_EDIT_CART_BLUE_TEXT[1]))
    s(VIEW_AND_EDIT_CART_BLUE_TEXT[1]).click()


def move_to_cart():
    s(a).hover()
