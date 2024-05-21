import allure
from selene import browser, have
from data.links import *
from pages import women_page
from selene.support.shared.jquery_style import s
from pages.locators import WomenPageLocators


@allure.feature("Women page")
@allure.title('Women >Dropdown menu>Checking page redirection to Tops elements')
def test_checking_page_redirection_to_tops_elements():
    women_page.visit()
    women_page.move_to_woman_menu()
    women_page.click_dropdown_tops_link()
    browser.should(have.url(TOPS_WOMEN_PAGE_LINK))


@allure.feature("Women page")
@allure.title('Women >Dropdown menu> Checking page redirection to Bottom elements')
def test_checking_page_redirection_to_bottom_elements():
    women_page.visit()
    women_page.move_to_woman_menu()
    women_page.click_dropdown_bottoms_link()
    browser.should(have.url(BOTTOMS_WOMEN_PAGE_LINK))


@allure.feature("Women page")
@allure.title('Women >Dropdown menu>Verify visibility elements')
def test_verify_visibility_elements_dropdown_menu():
    women_page.visit()
    women_page.move_to_woman_menu()
    s(WomenPageLocators.DROPDOWN_BLOCK).should(have.text('Tops') and have.text('Bottoms'))


@allure.title("Compare products | From any catalog's page > Verify after clicking on the compare button user is "
              "redirected to the Compare Products page.")
@allure.link("https://trello.com/c/fvMCdJ97")
def test_checking_page_redirection_to_tops_elements():
    women_page.visit()
    women_page.hover_product_card()
    women_page.click_add_to_compare_icon()
    women_page.click_compare_btn()
    women_page.assert_page_title()
    women_page.assert_comp_list_item()
