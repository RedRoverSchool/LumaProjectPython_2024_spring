import pytest
from pages.locators import SalePageLocators, BaseLocators, ProductLocators as PL
from pages import women_page, main_page, product_page
from selene import browser, be, have, by, query
from selene.support.shared.jquery_style import s, ss
import allure


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


@allure.suite('US_002.001 | Page of any product')
@allure.title('TC_002.001.001 | Radiant Tee product page > Visibility of product name, price and photo')
@allure.link('https://trello.com/c/SKLAh5ku/')
def test_002_001_001_product_name_price_img_visibility(login):
    women_page.move_to_woman_menu()
    women_page.move_to_tops_menu()
    women_page.click_dropdown_tees()
    women_page.click_radiant_tee()
    women_page.check_radiant_tee_title_is_visible()
    women_page.check_radiant_tee_img_are_visible()
    women_page.check_radiant_tee_price_is_visible()


@pytest.mark.skip
@allure.suite('US_002.001 | Page of any product')
@allure.title('TC_002.001.002 | Radiant Tee product page > Add to cart > Adding the product to cart')
@allure.link('https://trello.com/c/xGtHnQaq/')
def test_002_001_002_adding_product_to_cart(login):
    with allure.step('Opening Radiant Tee product page'):
        browser.open(PL.RADIANT_TEE_URL)
    with allure.step('Checking whether the cart is empty, if not - clearing the cart'):
        main_page.MainPage.clear_minicart()
    with allure.step('Selecting product size'):
        product_page.select_product_size("M")
    with allure.step('Selecting product color'):
        product_page.select_product_color("Blue")
    with allure.step('Entering product quantity'):
        product_page.select_product_quantity('2')
    with allure.step('Adding the product to cart'):
        product_page.add_product_to_cart()
    with allure.step('Opening mini-cart'):
        main_page.MainPage.open_mini_cart()
    with allure.step('Checking whether Radiant Tee name is visible in mini-cart'):
        product_page.check_radiant_tee_name_in_minicart_is_visible()
    with allure.step('Checking whether the product qty in mini-cart is correct'):
        main_page.MainPage.check_product_qty_inside_minicart("2")
    with allure.step('Checking whether mini-cart Subtotal is correct'):
        product_page.check_minicart_subtotal("2")
    with allure.step('Closing mini-cart'):
        main_page.MainPage.close_minicart()
    with allure.step('Clearing mini-cart'):
        main_page.MainPage.clear_minicart()
