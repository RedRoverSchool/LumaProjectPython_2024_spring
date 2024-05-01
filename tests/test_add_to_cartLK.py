import time
from selene import browser, have
from pages import add_to_cartLK
from pages.add_to_cartLK import *

def test_add_to_cart():
    add_to_cartLK.open_main_page()
    add_to_cartLK.click_title_item()
    add_to_cartLK.click_size_button()
    add_to_cartLK.click_color_button()
    add_to_cartLK.click_add_to_cart_button()
    add_to_cartLK.click_cart_icon2()
    add_to_cartLK.assert_view_and_edit_cart_blue_text()
    assert browser.should(have.url(LINK_CHECKOUT))