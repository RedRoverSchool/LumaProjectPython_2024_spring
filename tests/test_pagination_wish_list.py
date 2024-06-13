from pages import limiter_item
import allure


@allure.link('https://trello.com/c/4pi1wsxr')
@allure.feature('Pagination')
@allure.title('Verify the function of pagination')
def test_pagination_wish_list():
    limiter_item.preconditions()
    limiter_item.change_limit_to_10()
    limiter_item.item_page_item_next()
    limiter_item.items_amount()
