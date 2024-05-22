import allure
import pytest
from pages import wish_list, sale_page, sign_in
from pages import whats_new_page


@pytest.mark.skip
@allure.link("https://trello.com/c/kVWLOEl5")
def test_button_update_clickable(login):
    whats_new_page.add_item_to_wish_list()
    wish_list.visit()
    wish_list.click_update()
    wish_list.url_should_contain("wishlist_id")


@pytest.mark.skip
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


@allure.link('https://trello.com/c/WQ4d6xa4')
def test_011_006_001_message_no_items_is_displayed():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail.com", "jk$34_tor")
    wish_list.visit_sale()
    wish_list.wish_list_is_empty()


@allure.link('https://trello.com/c/ygmonlgs')
def test_011_006_003_redirection_from_wish_list():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail.com", "jk$34_tor")
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.ITEM_9_ADD_TO_WISH_LIST)
    wish_list.go_to_wish_list()
    wish_list.title_is_correct()
    wish_list.clear_wish_list()


@allure.link('https://trello.com/c/cMjsLvWj')
def test_011_006_002_check_info_in_wish_list():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail.com", "jk$34_tor")
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.ITEM_6_ADD_TO_WISH_LIST)
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.ITEM_8_ADD_TO_WISH_LIST)
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.ITEM_9_ADD_TO_WISH_LIST)
    wish_list.visit_women_jackets()
    wish_list.wish_list_is_not_empty()
    wish_list.check_qty_in_wishlist()
    wish_list.count_items_in_wishlist(3)
    wish_list.count_button_add_tocart(3)
    wish_list.count_prices_in_wishlist(3)
    wish_list.items_name_in_wishlist_is_clickable()
    wish_list.images_in_wishlist_is_clickable()
    wish_list.count_images_in_wishlist(3)
    wish_list.clear_wish_list()
