import allure
from pages import whats_new
from pages import create_account, message
from pages import wish_list


@allure.link('https://trello.com/c/zbRUOa7r')
@allure.suite("US_014.003 | Wish list > Removing and Edit Items")
class TestRemovingAndEditItemsInWishlist:
    def test_button_update_clickable(self, first_name, last_name, user_email, password):
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
        #     wish_list.edit_item_in_wish_list(last, 3, 0, 0)
        #     wish_list.remove_item_from_wish_list(0)
        #     wish_list.remove_item_from_wish_list(0)
        #     wish_list.is_wish_list_empty()
