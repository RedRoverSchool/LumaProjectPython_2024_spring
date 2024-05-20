import allure
import pytest
from selene import browser

from pages import women_page
from pages.product_page import ProductPage


@allure.link('https://trello.com/c/fhLdyS1l')
def test_011_016_001_women_tees_breadcrumbs_is_correct():
    women_page.visit_women_tee()
    women_page.check_if_breadcrumbs_have_all_parts()


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_nr_of_links_from_women_tees():
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs()


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_nr_of_links_from_women_tees_var2():
    # test another method
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs_by_count()


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_redirection_from_women_tees_var3():
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr()


@allure.suite('US_002.001 | Page of any product')
class TestRadiantTeePage:
    @allure.title('TC_002.001.002 | Radiant Tee product page > Add to cart > Adding the product to cart')
    @allure.link('https://trello.com/c/xGtHnQaq/')
    def test_002_001_002_adding_product_to_cart(self, login):
        page = ProductPage(browser=browser)
        page.clear_cart()
        page.open_radiant_tee_page()
        page.add_product_to_cart_with_qty("M", "Blue", "2")
        page.goto_card_page()
        page.is_radiant_tee_name_visible_in_minicart()
        page.is_minicart_quantity_correct("2")
        page.is_minicart_subtotal_correct("2")
        page.delete_product_from_cart()

    @allure.title('TC_002.001.001 | Radiant Tee product page > Visibility of product name, price and photo')
    @allure.link('https://trello.com/c/SKLAh5ku/')
    def test_002_001_001_product_name_price_img_visibility(self, login):
        page = ProductPage(browser=browser)
        page.open_radiant_tee_page()
        page.is_radiant_tee_title_visible()
        page.is_radiant_tee_img_visible()
        page.is_radiant_tee_price_is_visible()


    @allure.link('https://trello.com/c/mtsK5CPx')
    @allure.title('TC_002.001.003 | Radiant Tee product page > Quantity of items> Quantity of items added to cart')
    def test_002_001_003_radiant_tee_quantity_added_to_cart(self, login):
        page = ProductPage(browser=browser)
        page.clear_cart()
        page.open_radiant_tee_page()
        page.add_product_to_cart_with_qty("M", "Blue", "2")
        page.goto_card_page()
        page.is_cart_counter_shows_correct_number("2")
        page.is_minicart_quantity_correct("2")
        page.is_minicart_subtotal_correct("2")
        page.delete_product_from_cart()
        
    @allure.link('https://trello.com/c/EXhjde1P')
    @allure.title('TC_002.001.004 | Radiant Tee product page > Visibility of the product description and detailed information')
    def test_radiant_tee_visibility_of_description(self, login):
        page = ProductPage(browser=browser)
        page.open_radiant_tee_page()
        page.is_product_details_visible()
        page.click_more_information_tab()
        page.is_more_information_visible()

    @allure.link('https://trello.com/c/PChP2lY4')
    @allure.title('TC_002.001.005 | Radiant Tee product page > Reviews > Reviews visibility')
    def test_radiant_tee_reviews_visibility(self, login):
        page = ProductPage(browser=browser)
        page.open_radiant_tee_page()
        page.click_reviews_tab()
        page.is_reviews_content_visible()
