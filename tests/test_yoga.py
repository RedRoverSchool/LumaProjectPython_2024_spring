import allure
from pages import whats_new
from pages import yoga_page


@allure.feature("What`s new page > New Luma Yoga Collection")
@allure.link("https://trello.com/c/G7Iz9eaQ")
@allure.title("The New Luma Yoga Collection link and Shop New Yoga button links are displayed on the What's New page")
def test_new_luma_yoga_collection_link_visibility():
    whats_new.open_page()
    whats_new.is_yoga_link_visible()
    whats_new.is_button_visible()


@allure.feature("What`s new page > New Luma Yoga Collection")
@allure.link("https://trello.com/c/jqrXmRkR")
@allure.title("The \"New Luma Yoga Collection\" link redirects to New Luma Yoga Collection page")
def test_yoga_link_redirection():
    whats_new.open_page()
    whats_new.new_yoga_link_click()
    assert whats_new.is_current_url_yoga()
    whats_new.verify_header_text('New Luma Yoga Collection')


@allure.feature("What`s new page > New Luma Yoga Collection")
@allure.link("https://trello.com/c/oTH09O30")
@allure.title("The \"Shop New Yoga\" button link redirects to New Luma Yoga Collection page")
def test_yoga_button_redirection():
    whats_new.open_page()
    whats_new.click_button_shop_new_yoga()
    assert whats_new.is_current_url_yoga()
    whats_new.verify_header_text('New Luma Yoga Collection')


@allure.feature("What`s new page > New Luma Yoga Collection")
@allure.link("https://trello.com/c/jRy1WrCH")
@allure.title("The \"List\" button is displayed and changes a page view type")
def test_yoga_list_button_visibility_and_redirection():
    yoga_page.open_page()
    yoga_page.is_list_button_visible()
    yoga_page.list_button_click()
    assert yoga_page.is_current_url_list
    yoga_page.is_wrapper_list_view_visible()


@allure.feature("What`s new page > New Luma Yoga Collection")
@allure.link("https://trello.com/c/k2lE2NmK")
@allure.title("The \"Grid\" button is displayed and changes a page view type")
def test_yoga_grid_button_visibility_and_redirection():
    yoga_page.open_list_view_page()
    yoga_page.is_grid_button_visible()
    yoga_page.grid_button_click()
    assert yoga_page.is_current_url_yoga()
    yoga_page.is_wrapper_grid_view_visible()
