import pytest
import allure
from pages import women_page


@pytest.mark.xfail(reason="assert error !!! 'Sale' is missing")
@allure.feature('Sale > Women Sale')
@allure.link('https://trello.com/c/Ae5Bscv3')
@allure.title('Breadcrumbs are visible and correct')
def test_women_sale_breadcrumbs_is_correct():
    women_page.visit_women_sale()
    women_page.check_breadcrumbs_from_women_sale_have_word()


@pytest.mark.xfail
@allure.feature('Sale > Women Sale')
@allure.link('https://trello.com/c/ZajZB0og')
@allure.title('Breadcrumbs redirects to the correct page')
def test_readcrumbs_have_attribute():
    women_page.visit_women_sale()
    women_page.check_breadcrumbs_from_women_sale_have_attribute()


@allure.feature('Footer > "Search terms" link')
@allure.link("https://trello.com/c/vmAubLQw")
@allure.title('Correct redirection for unauthorized user')
def test_redirection_to_search_page():
    women_page.visit()
    women_page.find_link_in_footer()
    women_page.click_link_in_footer()
    women_page.title_is_correct()
