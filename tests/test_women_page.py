import allure
import pytest
from pages import women_page
from pages.women_page import bottoms_page_title, tops_page_title


@allure.feature("Women page > Dropdown menu")
@allure.link('https://trello.com/c/fiaj6Wpc')
@allure.title('Verify visibility elements')
def test_verify_visibility_elements_dropdown_menu():
    women_page.visit()
    women_page.move_to_woman_menu()
    women_page.dropdown_menu_have_elements('Tops', 'Bottoms')


# @pytest.mark.skip
@allure.feature('Compare products > From any catalogs page')
@allure.title("Verify after clicking on the compare button user is redirected to the Compare Products page")
@allure.link("https://trello.com/c/fvMCdJ97")
def test_checking_page_redirection_to_tops_elements():
    women_page.visit()
    women_page.hover_product_card()
    women_page.click_add_to_compare_icon()
    women_page.click_compare_btn()
    women_page.assert_page_title()
    women_page.assert_comp_list_item()


@pytest.mark.parametrize('page_title, link_click, expected_title', [
    ("Tops", women_page.click_dropdown_tops_link, tops_page_title),
    ("Bottoms", women_page.click_dropdown_bottoms_link, bottoms_page_title)])
@allure.feature("Women page > Dropdown menu")
@allure.title('https://trello.com/c/1kNep1VB')
@allure.title('Checking page redirection to {page_title} elements')
def test_use_param(page_title, link_click, expected_title):
    women_page.visit()
    women_page.move_to_woman_menu()
    link_click()
    women_page.should_have_page_title(expected_title, page_title)
