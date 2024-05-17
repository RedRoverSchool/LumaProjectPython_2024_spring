from selene import browser, be, have
import allure
from pages import sale_page, compare_side_panel
from selene.support.shared.jquery_style import s
from pages.sale_page import SalePage
from pages.locators import SalePageLocators, BaseLocators, NavigatorLocators
from pages.main_page import MainPage
from data.links import *
import pytest


@allure.feature("Sale")
@allure.link('https://trello.com/c/RF0vkTGW')
def test_011_001_001_sale_breadcrumbs_is_correct():
    sale_page.visit()
    sale_page.check_if_breadcrumbs_have_all_parts()


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
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_FREE_SHIPPING_TITLE).should(
        have.text('Spend $50 or more — shipping is free!'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_FREE_SHIPPING_INFO).should(have.text('Buy more, save more'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_TITLE).should(
        have.text('You can\'t have too many tees'))
    browser.element(SalePageLocators.BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_INFO).should(
        have.text('4 tees for the price of 3. Right now'))


@allure.feature("Sale")
@allure.link('https://trello.com/c/4slhRo2E')
@pytest.mark.parametrize("url", [MAIN_PAGE_LINK, LOGIN_URL, CREATE_ACCOUNT_URL, WHATS_NEW_PAGE_LINK,
                                 WOMEN_PAGE_LINK, WOMEN_TOPS_URL, WOMEN_TOPS_JACKETS_URL, WOMEN_TOPS_HOODIES_URL,
                                 WOMEN_TOPS_TEES_URL, WOMEN_TOPS_BRAS_URL, WOMEN_BOTTOMS_URL, WOMEN_BOTTOMS_PANTS_URL,
                                 WOMEN_BOTTOMS_SHORTS_URL,
                                 MEN_PAGE_URL, MEN_TOPS_URL, MEN_TOPS_JACKETS_URL, MEN_TOPS_HOODIES_URL,
                                 MEN_TOPS_TEES_URL, MEN_TOPS_TANKS_URL, MEN_BOTTOMS_URL, MEN_BOTTOMS_PANTS_URL,
                                 MEN_BOTTOMS_SHORTS_URL,
                                 GEAR_PAGE_URL, GEAR_BAGS_URL, GEAR_FITNESS_URL, GEAR_WATCHES_URL,
                                 TRAINING_URL, VIDEO_DOWNLOAD_URL, SALE_PAGE_URL, random_product_url,
                                 POPULAR_SEARCH_TERMS_URL, PRIVACY_POLICY_PAGE_LINK, ADVANCED_SEARCH_URL,
                                 ORDERS_RETURNS_URL, ERIN_RECOMMENDS_URL, YOGA_URL, PERFORMANCE_FABRICS_URL,
                                 ECO_FRIENDLY_URL, CART_URL])
@pytest.mark.skip
def test_011_001_004_user_can_see_sale_page(url):
    browser.open(url)
    MainPage.handle_cookies_popup()
    s(NavigatorLocators.NAV_SALE).should(be.visible)


# @pytest.mark.skip
@allure.link("https://trello.com/c/hSe3gPsx")
def test_11_005_003_check_items_in_list_for_compare():
    sale_page.visit_women_jackets()
    items_to_be_compared = compare_side_panel.collect_item_names_to_be_compared()
    compare_side_panel.choose_to_compare_item_nr(1)
    compare_side_panel.choose_to_compare_item_nr(2)
    compare_side_panel.choose_to_compare_item_nr(3)
    sale_page.visit_sale()
    # compare_side_panel.should_be_3_items_to_compare()
    compare_side_panel.button_compare_is_clickable()
    compare_side_panel.link_clearall_is_clickable()
    compared_items = compare_side_panel.collect_items_list_compare()
    assert items_to_be_compared == compared_items


@allure.link('https://trello.com/c/mZOkRDzP/')
@allure.title('TC_011.008.001 | Sale > Block “Men’s Deals”>Visibility of image and text')
def test_011_008_001_men_s_deals_img_and_text_visibility():
    sale_page.visit_sale()
    sale_page.is_mens_deals_img_visible()
    sale_page.is_mens_bargains_text_visible()
    sale_page.is_stretch_your_budget_text_visible()
    sale_page.is_shop_mens_deals_text_visible()
