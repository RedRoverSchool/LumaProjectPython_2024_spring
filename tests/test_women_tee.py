import pytest

from pages.locators import SalePageLocators, BaseLocators, ProductLocators as PL
from pages import sign_in, women_page
from selene import browser, be, have, by, query
from selene.support.shared.jquery_style import s, ss
import allure
from data.links import *


@allure.link('https://trello.com/c/fhLdyS1l')
def test_011_016_001_women_tees_breadcrumbs_is_correct():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Women', 'Tops', 'Tees'))


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_redirection_from_women_tees():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_nr_of_links_from_women_tees():
    # test another method
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    elements.should(have.size(3))


def test_011_016_002_breadcrumbs_redirection_from_women_tees_var2():
    # сравнить ссылки ожидаемые и фактические перебором по очереди
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    for i, item in enumerate(ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))):
        assert expected_links[i] == item.get(query.attribute('href'))


@pytest.mark.skip
@allure.link('https://trello.com/c/SKLAh5ku/')
def test_002_001_001_product_name_price_img_visibility():
    sign_in.visit()
    sign_in.login('test12345678@example.com', 'Test12345678')
    women_page.move_to_woman_menu()
    women_page.move_to_tops_menu()
    women_page.click_dropdown_tees()
    women_page.click_radiant_tee()
    browser.element(PL.RADIANT_TEE_TITLE).should(be.visible)
    browser.element(PL.RADIANT_TEE_IMG).should(be.visible)
    browser.element(PL.RADIANT_TEE_PRICE).should(be.visible)

