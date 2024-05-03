import allure
import pytest
from selene import browser, have, be
from data.links import *
from pages import women_page
from selene.support.shared.jquery_style import s, ss
from pages.locators import WomenPageLocators as WPL
from pages.locators import SalePageLocators
from pages.locators import BaseLocators


@pytest.mark.skip("Page Women is down")
@allure.title('Women >Dropdown menu>Checking page redirection to Tops elements')
def test_checking_page_redirection_to_tops_elements():
    women_page.visit()
    women_page.move_to_woman_menu()
    women_page.click_dropdown_tops_link()
    browser.should(have.url(TOPS_WOMEN_PAGE_LINK))


@pytest.mark.skip("Page Women is down")
@allure.title('Women >Dropdown menu> Checking page redirection to Bottom elements')
def test_checking_page_redirection_to_bottom_elements():
    women_page.visit()
    women_page.move_to_woman_menu()
    women_page.click_dropdown_bottoms_link()
    browser.should(have.url(BOTTOMS_WOMEN_PAGE_LINK))


@pytest.mark.skip("Page Women is down")
@allure.title('Women >Dropdown menu>Verify visibility elements')
def test_verify_visibility_elements_dropdown_menu():
    women_page.visit()
    women_page.move_to_woman_menu()
    assert s(WPL.DROPDOWN_BLOCK).should(have.text('Tops') and have.text('Bottoms'))


@pytest.mark.xfail
@allure.link('https://trello.com/c/ZajZB0og')
def test_011_011_002_breadcrumbs_redirection_from_women_sale():
    browser.open(SalePageLocators.LINK_WOMEN_SALE)
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/sale.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))
