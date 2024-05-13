import allure
from selene import browser
import pytest
from pages import wish_list
from pages.whats_new_page import WhatsNewPage

@pytest.mark.skip
@allure.link("https://trello.com/c/kVWLOEl5")
def test_button_update_clickable(login):
    WhatsNewPage(browser=browser).add_item_to_wish_list()
    wish_list.visit()
    wish_list.click_update()
    wish_list.url_should_contain("wishlist_id")

@allure.link("https://trello.com/c/xP2eIJZq")
@allure.feature("Wish list > Removing and Edit Items")
@allure.title("TC_014.003.002 | Wish list > Removing items")
def test_remove_item_from_wishlist(login):
    wish_list.add_item_to_wish_list()
    with allure.step("Hover cursor on the item"):
        wish_list.hover_over_item()
    with allure.step("Click on ‘trash bin’ icon of item"):
        item_title = wish_list.remove_item()
    with allure.step("Verify that the item with saved name doesnt appear in wish list"):
        wish_list.is_item_removed(item_title)
