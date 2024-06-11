import allure
import pytest

from selene import browser, be, have
from pages import sale, tees_page
from selene.support.shared.jquery_style import s
from pages.locators import SalePageLocators, BaseLocators, NavigatorLocators
from pages.main_page import MainPage
from data.links import *


@allure.feature("Sale")
@allure.title('TC_011.001.001 !Card not found!')
@allure.link('https://trello.com/c/RF0vkTGW')
def test_sale_breadcrumbs_is_correct():
    sale.open_page_women_sale()
    sale.check_if_breadcrumbs_have_all_parts()


@allure.feature("Sale > Gear deals on side panel")
@allure.title('Visibility of name GEAR DEALS')
@allure.link('https://trello.com/c/6x8wE9U7')
def test_availability_of_name():
    sale.open_page()
    browser.element(SalePageLocators.GEAR_DEALS_TITLE).should(be.visible)


@allure.feature("Sale > Gear deals on side panel")
@allure.title('Visibility of link Fitness Equipment')
@allure.link('https://trello.com/c/eVJdCZD6')
def test_availability_of_links_fitness():
    sale.open_page()
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).should(be.visible)


@allure.feature("Sale > Gear deals on side panel")
@allure.title('Visibility of link Bags')
@allure.link('https://trello.com/c/eabRQXD0')
def test_availability_of_links_bags():
    sale.open_page()
    browser.element(SalePageLocators.BAGS_LINK).should(be.visible)


@allure.feature("Sale > Gear deals on side panel")
@allure.title('Check Bags link clickability')
@allure.link('https://trello.com/c/R37TlLm7')
def test_bags_link_clickability():
    sale.open_page()
    browser.element(SalePageLocators.BAGS_LINK).should(be.clickable)


@allure.feature("Sale > Gear deals on side panel")
@allure.title('Check Fitness Equipment link clickability')
@allure.link('https://trello.com/c/bG0oyzyv')
def test_fitness_link_clickability():
    sale.open_page()
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).click()


@allure.feature("Sale > Gear deals on side panel")
@allure.title('Check Fitness Equipment link correct redirection')
@allure.link('https://trello.com/c/tTSnRKWm')
def test_fitness_link_correct_redirection():
    sale.open_page()
    browser.element(SalePageLocators.FITNESS_EQUIPMENT_LINK).click()
    browser.should(have.url_containing("gear/fitness-equipment"))
    browser.element(BaseLocators.PAGE_NAME).should(have.text('Fitness'))


@allure.feature("Sale > Gear deals on side panel")
@allure.title("Check Bags link correct redirection")
@allure.link('https://trello.com/c/QRHjcYZH')
def test_bags_link_correct_redirection():
    sale.open_page()
    browser.element(SalePageLocators.BAGS_LINK).click()
    browser.should(have.url_containing("gear/bags"))
    browser.element(BaseLocators.PAGE_NAME).should(have.text('Bags'))


@allure.feature("Sale")
@allure.title('Verify clickability of a button "Shop Womens Deals"')
@allure.link('https://trello.com/c/pyqtpSob')
def test_011_007_002_clickability_button():
    sale.open_page()
    sale.check_page_title()
    sale.assert_redirect_url()


@allure.feature("Sale")
@allure.title('Verify each image includes a short description of the promotion and its benefits')
@allure.link('https://trello.com/c/O0iYXhy1')
def test_each_image_includes_short_description_of_the_promotion():
    sale.open_page()
    s(SalePageLocators.BLOCK_PROMO_SALE_20_OFF_TITLE).should(have.text('20% OFF'))
    s(SalePageLocators.BLOCK_PROMO_SALE_20_OFF_INFO).should(have.text('Every $200-plus purchase!'))
    s(SalePageLocators.BLOCK_PROMO_SALE_FREE_SHIPPING_TITLE).should(have.text('Spend $50 or more — shipping is free!'))
    s(SalePageLocators.BLOCK_PROMO_SALE_FREE_SHIPPING_INFO).should(have.text('Buy more, save more'))
    s(SalePageLocators.BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_TITLE).should(have.text('You can\'t have too many tees'))
    s(SalePageLocators.BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_INFO).should(have.text('4 tees for the price of 3. Right now'))


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
@allure.feature("Sale")
@allure.title('Verify redirection to the sale page from any page')
@allure.link('https://trello.com/c/4slhRo2E')
def test_011_001_004_user_can_see_sale_page(url):
    browser.open(url)
    MainPage.handle_cookies_popup()
    s(NavigatorLocators.NAV_SALE).should(be.visible)


@allure.feature('Sale > Block “Men’s Deals”')
@allure.title('Visibility of image and text')
@allure.link('https://trello.com/c/mZOkRDzP/')
def test_men_s_deals_img_and_text_visibility():
    sale.open_page()
    sale.should_be_visible_image("Shop Men’s Deals")
    sale.should_be_visible_texts_on_image("Men’s Bargains", "Stretch your budget with active attire",
                                          "Shop Men’s Deals", "Shop Men’s Deals")


@allure.feature("Sale > Block 'Men’s Deals'")
@allure.title("Verify clicking to 'Men's Bargains' image redirect to the 'Men Sale' page")
@allure.link('https://trello.com/c/kH80u6ta')
def test_mens_deals_img_clickability_and_redirection():
    sale.open_page()
    sale.should_be_clickable_image("Shop Men’s Deals")
    sale.click_image_with_name("Shop Men’s Deals")
    sale.should_be_redirected_to_url_containing('men-sale')


@pytest.mark.skip
@allure.feature('Sale > Tees-women')
@allure.title("Check four different model of Tees for three discount is applied")
@allure.link('https://trello.com/c/Njj1Vlhj')
def test_discount_four_tees_for_different_model_is_applies():
    tees_page.open_login_page()
    tees_page.login_in()
    tees_page.click_on_four_tees_discount_banner()
    tees_page.check_the_shopping_cart_is_empty()
    tees_page.add_one_tees_black_color_size_l()
    tees_page.click_on_add_to_cart_btn()
    tees_page.add_one_tees_green_color_size_s()
    tees_page.click_on_add_to_cart_btn()
    tees_page.add_one_tees_orange_color_size_xs()
    tees_page.click_on_add_to_cart_btn()
    tees_page.add_one_tees_yellow_color_size_m()
    tees_page.click_on_add_to_cart_btn()
    tees_page.click_on_the_shopping_cart_icon()
    tees_page.check_quantity_items_in_the_shopping_list()
    tees_page.check_discount_is_applied_for_four_different_tees()
    tees_page.clear_the_cart_with_all_items()
    tees_page.check_shopping_cart_is_empty_after_deleting_all_items()


# @pytest.mark.skip
@allure.feature('Sale > Tees-women')
@allure.title("Check four tees for three with similar tess is applied")
@allure.link('https://trello.com/c/Njj1Vlhj')
def test_four_tees_discount_is_apply_for_similar_tees():
    tees_page.open_login_page()
    tees_page.click_on_four_tees_discount_banner()
    tees_page.add_four_same_model_tees()
    tees_page.click_on_add_to_cart_btn()
    tees_page.click_on_the_shopping_cart_icon()
    tees_page.check_discount_is_applied_for_four_similar_tees()
    tees_page.clear_cart_after_test()
