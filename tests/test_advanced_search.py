import allure
from pages import advanced_search


@allure.link('https://trello.com/c/kn91s1De')
@allure.feature("Advanced Search")
def test_input_fields_are_empty():
    advanced_search.open()
    advanced_search.click_button()
    advanced_search.message_text()


@allure.link('https://trello.com/c/X8H9lLun/')
@allure.feature('Advanced Search')
@allure.title('Entering an incorrect price range')
def test_incorrect_price_range():
    advanced_search.open()
    advanced_search.fill_wrong_price_range()
    advanced_search.click_button()
    advanced_search.price_range_error_message()
