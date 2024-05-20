import allure
from selene import browser
import pytest
from pages.whats_new_page import WhatsNewPage
from pages import create_account, message
from pages import wish_list


@pytest.mark.skip
@allure.link('https://trello.com/c/zbRUOa7r')
@allure.suite("US_014.003 | Wish list > Removing and Edit Items")
class TestRemovingAndEditItemsInWishlist:
    def test_button_update_clickable(self, first_name, last_name, user_email, password):
        with allure.step("Precondition: login, add items to with list"):
            create_account.visit()
            create_account.create_account(first_name, last_name, last_name + user_email, password)
            message.should_be_message("Thank you for registering")
            page = WhatsNewPage(browser=browser)
            page.open_page()
            page.add_items_to_wish_list(3)
        with allure.step("Verify the trash bin icon on the product card for each item"):
            wish_list.visit()
            wish_list.verify_trash_bin_icon_present()
        with allure.step("Click on the trash icon of a specific item to delete from the wishlist"):
            size = (len(wish_list.get_products()))
            wish_list.remove_item_from_wish_list(0)
            assert len(wish_list.get_products()) + 1 == size
            last = len(wish_list.get_products()) - 1
        with allure.step("Click on the edit icon of a specific item to edit item in the wishlist"):
            wish_list.edit_item_in_wish_list(last, 3, 0, 0)
            wish_list.remove_item_from_wish_list(0)
            wish_list.remove_item_from_wish_list(0)
            wish_list.is_wish_list_empty()
