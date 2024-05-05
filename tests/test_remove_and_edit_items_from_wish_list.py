import allure
from selene import browser

from pages.whats_new_page import WhatsNewPage
from pages import create_account, message
from pages import wish_list


@allure.link('https://trello.com/c/zbRUOa7r')
@allure.suite("US_014.003 | Wish list > Removing and Edit Items")
class TestRemovingAndEditItemsInWishlist:
    def test_button_update_clickable(self, first_name, last_name, user_email, password):
        with allure.step("Precondition: login, add items to with list"):
            create_account.visit()
            create_account.new_one(first_name, last_name, last_name + user_email, password)
            message.should_be("Thank you for registering")
            page = WhatsNewPage(browser=browser)
            page.open_page()
            page.add_items_to_wish_list()
        with allure.step("Verify the trash bin icon on the product card for each item"):
            wish_list.visit()
            wish_list.verify_trash_bin_icon_present()
        with allure.step("Click on the trash icon of a specific item to delete from the wishlist"):
            # wish_list.remove_item_from_wish_list(0)
            print(len(wish_list.get_products()))