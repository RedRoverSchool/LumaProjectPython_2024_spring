import pytest
import allure
from pages.men_sale_page import MenSalePage
from selene import browser
from data.page_data import MenSalePageData as data


@pytest.mark.xfail
@allure.link('https://trello.com/c/j98xpncK/402-tc011012001-sale-mens-deals-verify-bread-crumbs-display')
@allure.title('Verify Bread Crumbs display')
def test_verify_bread_crumbs_display():
    page = MenSalePage(browser)
    page.open_page()
    page.are_bread_crumbs_present()
    breadcrumbs = page.get_bread_crumbs()
    assert breadcrumbs == data.breadcrumbs_path
