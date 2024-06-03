from pages.locators import CompareProductsPage as CPP
from selene.support.shared.jquery_style import s, ss
from pages.locators import WomenPageLocators
from pages.locators import BaseLocators
from data.links import *
from selene import browser, be, have, query

LINK_WOMEN_SALE = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
WOMEN_PAGE_LINK = 'https://magento.softwaretestingboard.com/women.html'
LINK_TEES_WOMEN = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"
BREADCRUMBS_LIST = ".breadcrumbs li"
BREADCRUMBS_LINKS = '.breadcrumbs > ul  > li > a'
TANK_SIZE = '//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="M"]'
TANK_COLOR = '//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="Yellow"]'
TANK_BUTTON_ADD = '//*[@title="Breathe-Easy Tank"]/../..//*[@title="Add to Cart"]'
MESSAGE_SUCCESS_ADD = "div.messages [data-bind ^='html']"
SHOW_BASKET = ".action.showcart"
CHECKOUT_BUTTON = '#top-cart-btn-checkout'
FOOTER_LINKS = ('xpath', '//footer[@class="page-footer"]//li')
LINK_SEARCH_TERMS = 'footer > div > ul > li:nth-child(1)'
PAGE_TITLE = "h1"
BASE_URL = 'https://magento.softwaretestingboard.com'
link_top_women = BASE_URL + '/women/tops-women.html'
women_menu = s("//*[@id='ui-id-4']")
tops_link = s('a#ui-id-9')
bottoms_link = s("//*[@id='ui-id-10']")
bottoms_women_page_link = BASE_URL + '/women/bottoms-women.html'
dropdown_block = "//*[@id='ui-id-2']/li[2]/ul"
tops_page_title = '.page-title-wrapper'
bottoms_page_title = '.page-title-wrapper span'


def visit():
    browser.open(WOMEN_PAGE_LINK)


def move_to_woman_menu():
    women_menu.hover()


def click_dropdown_tops_link():
    tops_link.click()


def click_dropdown_bottoms_link():
    bottoms_link.click()


def hover_product_card():
    s(WomenPageLocators.RADIANT_TEE_HOTSELLERS_SECT).hover()


def click_add_to_compare_icon():
    s(WomenPageLocators.ADD_TO_COMPARE_ICON).click()


def click_compare_btn():
    s(WomenPageLocators.COMPARE_BTN).click()


def assert_page_title():
    assert s(BaseLocators.PAGE_TITLE).should(have.text('Compare Products')), "wrong title"


def assert_comp_list_item():
    assert s(CPP.COMP_LIST_RADIANT_TEE).should(have.text('Radiant Tee')), "wrong item"


def visit_women_tee():
    browser.open(LINK_TEES_WOMEN)


def check_if_breadcrumbs_have_all_parts():
    ss(BREADCRUMBS_LIST).should(have.texts('Home', 'Women', 'Tops', 'Tees'))


def check_nr_of_links_from_women_tee_by_breadcrumbs():
    elements = ss(BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_count():
    elements = ss(BREADCRUMBS_LINKS).by(have.attribute('href'))
    elements.should(have.size(3))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr():
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, item in enumerate(ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))):
        assert expected_links[i] == item.get(query.attribute('href'))


def visit_women_sale():
    browser.open(LINK_WOMEN_SALE)


def check_breadcrumbs_from_women_sale_have_attribute():
    elements = ss(BREADCRUMBS_LINKS).by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/sale.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_breadcrumbs_from_women_sale_have_word():
    # assert error !!! 'Sale' is missing
    ss(BREADCRUMBS_LIST).should(have.texts('Home', 'Women Sale'))


def choose_size_for_tank():
    s(TANK_SIZE).click()


def choose_color_for_tank():
    s(TANK_COLOR).click()


def button_add_to_cart_tank():
    s(TANK_BUTTON_ADD).click()


def success_msg_is_present():
    s(MESSAGE_SUCCESS_ADD).should(have.text("You added"))


def open_minicart():
    s(SHOW_BASKET).should(be.clickable).click()


def open_checkout():
    s(CHECKOUT_BUTTON).should(be.visible)
    s(CHECKOUT_BUTTON).should(be.clickable).click()


def find_link_in_footer():
    s(LINK_SEARCH_TERMS).should(be.visible)


def click_link_in_footer():
    s(LINK_SEARCH_TERMS).should(be.clickable).click()


def title_is_correct():
    s(PAGE_TITLE).should(have.text("Popular Search Terms"))


def should_be_redirect_to(link):
    browser.should(have.url(link))


def dropdown_menu_have_elements(first_elem, second_elem):
    s(dropdown_block).should(have.text(first_elem) and have.text(second_elem))


def should_have_page_title(locator, title):
    s(locator).should(have.text(title))
