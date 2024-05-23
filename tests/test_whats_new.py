import allure
import pytest
from selene import browser, have
from selene.support.shared.jquery_style import s

from pages import whats_new_page
from pages.locators import WhatsNewPageLocators as WNPL
from pages.main_page import MainPage


@allure.suite("US_006.006 | Testing What's New Page")
class TestWhatsNew:
    @allure.title("TC_006.006.001 | Test visibility of What's New link on the home page")
    def test_whats_new_link_visibility(self, browser_management):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Assert home page menu presence"):
            page.is_menu_present()
        with allure.step("Assert there is the What's New link in the menu"):
            page.is_whats_new_link_present()

    @allure.title("TC_006.006.002 | Check redirection to What's New page by clicking a link")
    def test_redirection_to_whats_new_page(self, browser_management):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Click on What's New link"):
            page.whats_new.click()
        with allure.step("Assert current url == What's New Page url"):
            assert whats_new_page.is_current_link()
        with allure.step("Find header"):
            header = whats_new_page.is_header_present()
        with allure.step("Assert header contains text \'What's New\'"):
            whats_new_page.is_element_text_correct(header, "What's New")

    @pytest.mark.skip
    @allure.link("https://trello.com/c/bCZOe2Tp/97-tc006006003-whats-new-page-check-lumas-latest-list-visibility")
    @allure.title("TC_006.006.003 | Check Luma`s latest list visibility")
    def test_luma_latest_list_visibility(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.whats_new.click()
        whats_new_page.is_luma_latest_present()
        item_number = whats_new_page.get_number_of_luma_latest()
        assert item_number == 4
        assert whats_new_page.are_men_and_women_items_present() is True

    @allure.title(
        "TC_006.002.004 I What's new > Eco Collection New* > Redirection to the product page by clicking on the product name")
    @allure.link('https://trello.com/c/GO8VRlcn')
    def test_eco_collection_redirection_to_pdp(self, login, browser_management):
        with allure.step('Opening Eco Collection New page'):
            whats_new_page.open_eco_collection_url()
        with allure.step('Opening Layla Tee page'):
            whats_new_page.click_layla_tee_name()
        with allure.step('Checking redirection'):
            whats_new_page.check_redirection_to_layla_tee_pdp()
        with allure.step('Checking Layla Tee title is visible'):
            whats_new_page.layla_tee_title_is_displayed()

    @allure.title(
        "TC_006.002.003 I What's new > Eco Collection New* > Redirection to the product page by clicking on the image")
    @allure.link('https://trello.com/c/aj3EgeOa')
    def test_eco_collection_redirection_to_pdp_by_clicking_on_img(self, login, browser_management):
        with allure.step('Opening Eco Collection New page'):
            whats_new_page.open_eco_collection_url()
        with allure.step('Opening Layla Tee page'):
            whats_new_page.click_layla_tee_img()
        with allure.step('Checking redirection'):
            whats_new_page.check_redirection_to_layla_tee_pdp()
        with allure.step('Checking Layla Tee title is visible'):
            whats_new_page.layla_tee_title_is_displayed()

    @allure.title('TC_006.005.001 | Verify that User gets error message This this is required field in red color')
    def test_user_gets_error_message(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.whats_new.click()
        whats_new_page.click_bras_and_tank_link()
        whats_new_page.click_breathe_easy_tank_item()
        whats_new_page.add_to_cart_button()
        s(WNPL.ERROR_MASSAGE_UNDER_SIZE).should(have.text('This is a required field.'))
        s(WNPL.ERROR_MASSAGE_UNDER_COLOR).should(have.text('This is a required field.'))

    @allure.link('https://trello.com/c/lbjGjlg5/')
    @allure.title("TC_006.002.001| What's new > Eco Collection New* > Changing the color in product list")
    def test_eco_collection_change_color_in_product_list(self, login):
        whats_new_page.open_eco_collection_url()
        whats_new_page.change_layla_tee_color('Blue')
        whats_new_page.is_color_selected('Blue', '#ff5501')
        whats_new_page.is_layla_tee_img_color_correct('blue')

    @allure.link('https://trello.com/c/E9ZewRUB')
    @allure.title("TC_006.002.002| What's new > Eco Collection New* > Visibility of buttons on product card")
    def test_eco_collections_new_products_buttons_visibility(self, login):
        whats_new_page.open_eco_collection_url()
        whats_new_page.check_buttons_visibility_on_product_card()

    @allure.link('https://trello.com/c/dGGLziIU')
    @allure.title("TC_006.005.002 | What's new > Eco Collection New*> Verify User gets error message")
    def test_user_gets_error_massage(self):
        page = MainPage(browser=browser)
        page.open_page()
        page.whats_new.click()
        whats_new_page.click_bras_and_tank_link()
        whats_new_page.click_breathe_easy_tank_item()
        whats_new_page.add_to_wish_list_button()
        assert s(WNPL.ERROR_MASSAGE_YOU_MUST_LOGIN_OR_REGISTER).should(
            have.text('You must login or register to add items to your wishlist.'))

    @allure.link('https://trello.com/c/g5xgzhu7')
    @allure.title("TC_006.005.003| What's new > Eco Collection New*> Verify user gets successful message")
    def test_user_gets_successful_massage(self, browser_management):
        page = MainPage(browser=browser)
        page.open_page()
        page.whats_new.click()
        whats_new_page.click_bras_and_tank_link()
        whats_new_page.click_breathe_easy_tank_item()
        whats_new_page.add_to_compare_button()
        assert s(WNPL.YOU_ADDED_PRODUCT).should(have.text('You added product Breathe-Easy Tank to the comparison list.'))
