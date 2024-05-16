from selene.support.shared.jquery_style import s, ss
from pages.locators import WomenPageLocators as WPL, ProductLocators as PL, SalePageLocators as SPL, BaseLocators as BL
from data.links import *
from selene import browser, be, have, query


def visit():
    browser.open(WOMEN_PAGE_LINK)


def move_to_woman_menu():
    s(WPL.WOMEN_MENU).hover()


def click_dropdown_tops_link():
    s(WPL.TOPS_LINK).click()


def move_to_tops_menu():
    s(WPL.TOPS_LINK).hover()


def click_dropdown_bottoms_link():
    s(WPL.BOTTOMS_LINK).click()


def click_dropdown_tees():
    s(WPL.TEES_LINK).wait_until(be.clickable)
    s(WPL.TEES_LINK).click()


def click_radiant_tee():
    s(PL.RADIANT_TEE_LINK).wait_until(be.visible)
    s(PL.RADIANT_TEE_LINK).click()


def check_radiant_tee_title_is_visible():
    browser.element(PL.RADIANT_TEE_TITLE).should(be.visible)


def check_radiant_tee_img_are_visible():
    browser.element(PL.RADIANT_TEE_IMG).should(be.visible)


def check_radiant_tee_price_is_visible():
    browser.element(PL.RADIANT_TEE_PRICE).should(be.visible)


def visit_women_tee():
    browser.open(SPL.LINK_TEES_WOMEN)


def check_if_breadcrumbs_have_all_parts():
    ss(BL.BREADCRUMBS_LIST).should(have.texts('Home', 'Women', 'Tops', 'Tees'))


def check_nr_of_links_from_women_tee_by_breadcrumbs():
    elements = ss(BL.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_count():
    elements = ss(BL.BREADCRUMBS_LINKS).by(have.attribute('href'))
    elements.should(have.size(3))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr():
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, item in enumerate(ss(BL.BREADCRUMBS_LINKS).by(have.attribute('href'))):
        assert expected_links[i] == item.get(query.attribute('href'))


def visit_women_sale():
    browser.open(SPL.LINK_WOMEN_SALE)


def check_breadcrumbs_from_women_sale_have_attribute():
    elements = ss(BL.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/sale.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_breadcrumbs_from_women_sale_have_word():
    # assert error !!! 'Sale' is missing
    ss(BL.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale', 'Women Sale'))
