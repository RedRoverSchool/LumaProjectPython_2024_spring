import allure
from selene import browser
from pages import create_account
from pages.gear_page import GearPage
from pages.main_page import MainPage
from pages.sale_page import SalePage


@allure.link("TC_004.004.006")
@allure.feature("Visibility 'Create an account' link")
def test_link_on_different_pages():
    pages = [MainPage(browser), GearPage(browser), SalePage(browser)]

    for page in pages:
        page.open_page()

        assert page.is_create_account_link_visible(), \
            f"Create an account link is not visible on {page.__class__.__name__.lower()}"


@allure.link("TC_004.004.006")
@allure.feature("Functionality 'Create an account' link")
def test_create_account_link_clickable():
    main_page = MainPage(browser)
    main_page.open_page()

    assert create_account.is_create_account_link_clickable(), "Create an account link is not clickable"
