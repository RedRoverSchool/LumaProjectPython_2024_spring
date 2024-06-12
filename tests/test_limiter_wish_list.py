import allure
from pages import limiter_item


@allure.feature('Limiter "Show on Page"')
@allure.title('Verify filter “Show on page')
@allure.link('https://trello.com/c/zKMpEsGc')
def test_limiter_options():
    limiter_item.preconditions()
    limiter_item.change_limit_to_20()
    limiter_item.items_number()
