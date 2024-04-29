from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import SalePageLocators, BaseLocators
import allure


@allure.link('https://trello.com/c/RF0vkTGW')
def test_011_001_001_sale_breadcrumbs_is_correct():
    browser.open(SalePageLocators.LINK_SALE)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale'))


@allure.link('https://trello.com/c/6x8wE9U7')
def test_availability_of_name():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.GEAR_DEALS_TITLE).should(be.visible)


@allure.link('https://trello.com/c/eVJdCZD6')
def test_availability_of_links_fitness():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).should(be.visible)


@allure.link('https://trello.com/c/eabRQXD0')
def test_availability_of_links_bags():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).should(be.visible)


@allure.link('https://trello.com/c/R37TlLm7')
def test_bags_link_clickability():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.BAGS_LINK).should(be.clickable)


@allure.link('https://trello.com/c/bG0oyzyv')
def test_fitness_link_clickability():
    browser.open('https://magento.softwaretestingboard.com/sale.html')
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).click()