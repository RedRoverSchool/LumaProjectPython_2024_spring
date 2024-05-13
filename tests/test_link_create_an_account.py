import allure
from selene import browser
from pages import create_account
from pages.gear_page import GearPage
from pages.main_page import MainPage
from pages.sale_page import SalePage

@allure.link("TC_004.004.006")
@allure.feature("Visibility 'Create an account' link")
def test_link_on_different_pages():
    main_page = MainPage(browser)
    main_page.open_page()
    assert main_page.is_create_account_link_visible(), "Create an account link is not visible on main page"

    gear_page = GearPage(browser)
    gear_page.open_page()
    assert gear_page.is_create_account_link_visible(), "Create an account link is not visible on gear page"

    sale_page = SalePage(browser)
    sale_page.open_page()
    assert sale_page.is_create_account_link_visible(), "Create an account link is not visible on sale page"

@allure.link("TC_004.004.006")
@allure.feature("Functionality 'Create an account' link")
def test_create_account_link_clickable():
    main_page = MainPage(browser)
    main_page.open_page()

    assert create_account.is_create_account_link_clickable(), "Create an account link is not clickable"

