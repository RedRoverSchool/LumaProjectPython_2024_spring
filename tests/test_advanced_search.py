import allure
from pages import advanced_search


@allure.link('https://trello.com/c/kn91s1De')
@allure.feature("Advanced Search")
def test_input_fields_are_empty():
    advanced_search.open()
    advanced_search.click_button()
    advanced_search.message_text()