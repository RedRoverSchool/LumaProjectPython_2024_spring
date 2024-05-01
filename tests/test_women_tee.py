from pages.locators import SalePageLocators, BaseLocators
from selene import browser, be, have, by
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


