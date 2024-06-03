from selene import browser, be, have
from selene.support.shared.jquery_style import s

show_cart = s("a[class='action showcart']")
subtitle_empty = s("strong[class='subtitle empty']")
base_url = "https://magento.softwaretestingboard.com"


def open_main_page():
    browser.open(base_url)


def check_the_cart_icon_is_visible():
    browser.open(base_url)

    show_cart.should(be.visible)
    show_cart.click()

    subtitle_empty.should(be.visible)
    subtitle_empty.should(have.text("You have no items in your shopping cart."))


def check_the_cart_icon_is_clickable():
    browser.open(base_url)
    show_cart.should(be.clickable)


def check_open_new_window_after_click_on_the_cart_icon():
    browser.open(base_url)
    show_cart.click()
    subtitle_empty.should(be.visible)
    subtitle_empty.should(have.text("You have no items in your shopping cart."))
