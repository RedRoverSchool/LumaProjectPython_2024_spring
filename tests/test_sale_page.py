from selene import browser, be, have
from selene.support.shared.jquery_style import ss

from data.links import SALE_SECTION_LINK
from pages.locators import SalePageLocators, BaseLocators
import allure

from pages.sale_page import SalePage


@allure.feature("Sale")
@allure.link('https://trello.com/c/RF0vkTGW')
def test_011_001_001_sale_breadcrumbs_is_correct():
    browser.open(SalePageLocators.LINK_SALE)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale'))


@allure.feature("Sale")
@allure.link('https://trello.com/c/6x8wE9U7')
def test_availability_of_name():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.GEAR_DEALS_TITLE).should(be.visible)


@allure.feature("Sale")
@allure.link('https://trello.com/c/eVJdCZD6')
def test_availability_of_links_fitness():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).should(be.visible)


@allure.feature("Sale")
@allure.link('https://trello.com/c/eabRQXD0')
def test_availability_of_links_bags():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).should(be.visible)


@allure.feature("Sale")
@allure.link('https://trello.com/c/R37TlLm7')
def test_bags_link_clickability():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).should(be.clickable)


@allure.feature("Sale")
@allure.link('https://trello.com/c/bG0oyzyv')
def test_fitness_link_clickability():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).click()


@allure.feature("Sale")
@allure.link('https://trello.com/c/tTSnRKWm')
def test_fitness_link_correct_redirection():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).click()
    browser.should(have.url_containing("gear/fitness-equipment"))
    browser.element(BaseLocators.PAGE_NAME).should(have.text('Fitness'))


@allure.feature("Sale")
@allure.link('https://trello.com/c/QRHjcYZH')
def test_bags_link_correct_redirection():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).click()
    browser.should(have.url_containing("gear/bags"))
    browser.element(BaseLocators.PAGE_NAME).should(have.text('Bags'))


@allure.feature("Sale")
@allure.link('https://trello.com/c/pyqtpSob')
def test_011_007_002_clickability_button():
    sale_page = SalePage(browser)
    sale_page.open_page()
    sale_page.check_page_title()
    sale_page.redirect()

@allure.feature("Sale")
@allure.link('https://trello.com/c/O0iYXhy1')
def test_each_image_includes_short_description_of_the_promotion():
    browser.open(SALE_SECTION_LINK)
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_20_OFF_TITLE).should(have.text('20% OFF'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_20_OFF_INFO).should(have.text('Every $200-plus purchase!'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_FREE_SHIPPING_TITLE).should(have.text('Spend $50 or more — shipping is free!'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_FREE_SHIPPING_INFO).should(have.text('Buy more, save more'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_TITLE).should(have.text('You can\'t have too many tees'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_INFO).should(have.text('4 tees for the price of 3. Right now'))

