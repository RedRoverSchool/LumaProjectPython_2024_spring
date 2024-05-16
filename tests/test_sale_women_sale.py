import pytest
import allure
from pages import women_page


@pytest.mark.xfail
@allure.link('https://trello.com/c/Ae5Bscv3')
def test_011_011_001_women_sale_breadcrumbs_is_correct():
    # assert error !!! 'Sale' is missing
    women_page.visit_women_sale()
    women_page.check_breadcrumbs_from_women_sale_have_word()


@pytest.mark.xfail
@allure.link('https://trello.com/c/ZajZB0og')
def test_011_011_002_breadcrumbs_have_attribute():
    women_page.visit_women_sale()
    women_page.check_breadcrumbs_from_women_sale_have_attribute()
