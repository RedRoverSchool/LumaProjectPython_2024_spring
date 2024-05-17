import pytest
import allure
from pages.men_sale_page import MenSalePage
from selene import browser
from data.page_data import MenSalePageData as data


@pytest.mark.skip
@allure.link('https://trello.com/c/j98xpncK/402-tc011012001-sale-mens-deals-verify-bread-crumbs-display')
@allure.title('Verify Bread Crumbs display')
def test_verify_bread_crumbs_display():
    page = MenSalePage(browser)
    page.open_page()
    page.are_bread_crumbs_present()
    breadcrumbs = page.get_bread_crumbs()
    assert breadcrumbs == data.breadcrumbs_path


@allure.link('https://trello.com/c/2hWLV7Cf')
@allure.title('Verify page title')
def test_verify_page_title():
    page = MenSalePage(browser)
    page.open_page()
    page.is_page_title_present()
    page.is_page_title_correct()


@pytest.mark.skip
@allure.link("https://trello.com/c/wnMvuIUl")
@allure.title("Verify total number of items on the page")
def test_verify_total_number_of_items():
    page = MenSalePage(browser)
    page.open_page()
    page.is_number_of_items_in_toolbar_corresponds_to_amount_in_list()
