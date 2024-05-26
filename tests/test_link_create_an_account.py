import allure
from selene import browser
from pages import gear_page
from pages import sale_page
from pages.main_page import MainPage


@allure.link("TC_004.004.006")
@allure.feature("Visibility 'Create an account' link")
def test_link_on_different_pages():
    pages = [MainPage(browser), gear_page, sale_page]

    for page in pages:
        page.open_page()
        page.should_be_clickable_create_account()
        page.has_create_account_text()


@allure.link("TC_004.004.006")
@allure.feature("Functionality 'Create an account' link")
def test_create_account_link_clickable():
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.should_be_clickable_create_account()
    main_page.has_create_account_text()
