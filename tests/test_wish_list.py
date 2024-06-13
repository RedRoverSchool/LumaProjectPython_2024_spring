import allure
import pytest
from pages import whats_new
from pages import create_account, message
from pages import wish_list


@pytest.mark.skip
@allure.feature('Wish list > Visibility, Clickability')
@allure.title('Check button "Update Wish List" is clickable')
@allure.link("https://trello.com/c/kVWLOEl5")
def test_button_update_clickable(login):
    whats_new.add_item_to_wish_list()
    wish_list.visit()
    wish_list.click_update()
    wish_list.url_should_contain("wishlist_id")


@pytest.mark.skip(reason="you shall not pass")
@allure.link("https://trello.com/c/xP2eIJZq")
@allure.feature("Wish list > Removing and Edit Items")
@allure.title("Removing items")
def test_remove_item_from_wishlist(login):
    wish_list.add_item_to_wish_list()
    with allure.step("Hover cursor on the item"):
        wish_list.hover_over_item()
    with allure.step("Click on ‘trash bin’ icon of item"):
        item_title = wish_list.remove_item()
    with allure.step("Verify that the item with saved name doesnt appear in wish list"):
        wish_list.is_item_removed(item_title)


@pytest.mark.skip
@allure.feature('Sale > My Wish List on side panel')
@allure.title('Verify the message “You have no items in your wish list is displayed')
@allure.link('https://trello.com/c/WQ4d6xa4')
def test_message_no_items_is_displayed():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail.com", "jk$34_tor")
    wish_list.visit_sale()
    wish_list.wish_list_is_empty()


@allure.feature("Sale > My Wish List on side panel")
@allure.title('Redirection to the product page by clicking on product name')
@allure.link('https://trello.com/c/ygmonlgs')
def test_redirection_from_wish_list():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail1.com", "jk$34_tor1")
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_9_add_to_wish_list)
    wish_list.go_to_wish_list()
    wish_list.title_is_correct()
    wish_list.clear_wish_list()


@allure.feature("Sale > My Wish List on side panel")
@allure.title('Information about items is visible and correct')
@allure.link('https://trello.com/c/cMjsLvWj')
def test_check_info_in_wish_list():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail1.com", "jk$34_tor1")
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_6_add_to_wish_list)
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_8_add_to_wish_list)
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_9_add_to_wish_list)
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


@allure.feature("Wish list")
@allure.title('Removing and Edit Items')
@allure.link('https://trello.com/c/zbRUOa7r')
def test_check_items_on_page_wishlist():
    wish_list.visit_login()
    wish_list.login("ahahah1@gmail2.com", "jk$34_tor2")
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_6_add_to_wish_list)
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_8_add_to_wish_list)
    wish_list.visit_women_jackets()
    wish_list.add_to_wish_list_from_catalog(wish_list.item_9_add_to_wish_list)
    wish_list.go_to_wish_list()
    items_in_wishlist = wish_list.collect_items_for_wishpage()
    wish_list.compare_side_panel_and_wishpage(items_in_wishlist)
    wish_list.clear_wish_list()


@allure.feature("Wish list")
@allure.title('Removing and Edit Items')
@allure.link('https://trello.com/c/zbRUOa7r')
def test_button_update_clickable(first_name, last_name, user_email, password):
    with allure.step("Precondition: login, add items to with list"):
        create_account.visit()
        create_account.create_account(first_name, last_name, last_name + user_email, password)
        message.should_be_message("Thank you for registering")
        whats_new.open_page()
        whats_new.add_items_to_wish_list(3)
    with allure.step("Verify the trash bin icon on the product card for each item"):
        wish_list.visit()
        wish_list.verify_trash_bin_icon_present()
    with allure.step("Click on the trash icon of a specific item to delete from the wishlist"):
        size = (len(wish_list.products))
        wish_list.remove_item_from_wish_list(0)
        assert len(wish_list.products) + 1 == size
