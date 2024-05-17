from selene.support.shared.jquery_style import s, ss
from pages.locators import WomenLocators, WomenPageLocators, FooterLocators
from pages.locators import BaseLocators, SalePageLocators
from data.links import *
from selene import browser, be, have, query


def visit():
    browser.open(WOMEN_PAGE_LINK)


def move_to_woman_menu():
    s(WomenPageLocators.WOMEN_MENU).hover()


def click_dropdown_tops_link():
    s(WomenPageLocators.TOPS_LINK).click()


def click_dropdown_bottoms_link():
    s(WomenPageLocators.BOTTOMS_LINK).click()


def visit_women_tee():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)


def check_if_breadcrumbs_have_all_parts():
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Women', 'Tops', 'Tees'))


def check_nr_of_links_from_women_tee_by_breadcrumbs():
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_count():
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    elements.should(have.size(3))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr():
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, item in enumerate(ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))):
        assert expected_links[i] == item.get(query.attribute('href'))


def visit_women_sale():
    browser.open(SalePageLocators.LINK_WOMEN_SALE)


def check_breadcrumbs_from_women_sale_have_attribute():
    elements = ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/sale.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_breadcrumbs_from_women_sale_have_word():
    # assert error !!! 'Sale' is missing
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Sale', 'Women Sale'))


def choose_size_for_tank():
    s(WomenLocators.TANK_SIZE).click()


def choose_color_for_tank():
    s(WomenLocators.TANK_COLOR).click()


def button_add_to_cart_tank():
    s(WomenLocators.TANK_BUTTON_ADD).click()


def success_msg_is_present():
    s(WomenLocators.MESSAGE_SUCCESS_ADD).should(have.text("You added"))


def open_minicart():
    s(WomenLocators.SHOW_BASKET).should(be.clickable).click()


def open_checkout():
    s(WomenLocators.CHECKOUT_BUTTON).should(be.visible)
    s(WomenLocators.CHECKOUT_BUTTON).should(be.clickable).click()


def find_link_in_footer():
    s(FooterLocators.LINK_SEARCH_TERMS).should(be.visible)


def click_link_in_footer():
    s(FooterLocators.LINK_SEARCH_TERMS).should(be.clickable).click()


def title_is_correct():
    s(BaseLocators.PAGE_TITLE).should(have.text("Popular Search Terms"))
