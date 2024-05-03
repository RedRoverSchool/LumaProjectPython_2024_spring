from selene import browser

from pages import wish_list
from pages.whats_new_page import WhatsNewPage


def test_button_update_clickable(login):
    WhatsNewPage(browser=browser).add_item_to_wish_list()
    wish_list.visit()
    wish_list.click_update()
    wish_list.url_should_contain("wishlist_id")


