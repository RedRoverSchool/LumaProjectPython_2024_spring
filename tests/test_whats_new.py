import allure
from selene import browser, have
from selene.support.shared.jquery_style import s

from pages import whats_new, product
from pages.locators import WhatsNewPageLocators as WNPL
from pages.main_page import MainPage


@allure.link("https://trello.com/c/VNhzWWei")
@allure.title("TC_006.006.001 | Test visibility of What's New link on the home page")
def test_whats_new_link_visibility():
    page = MainPage(browser)
    page.open_page()
    page.menu_should_be_present()
    page.whats_new_link_should_be_present()


@allure.link("https://trello.com/c/wRvM6M3F")
@allure.title("TC_006.006.002 | Check redirection to What's New page by clicking a link")
def test_redirection_to_whats_new_page():
    page = MainPage(browser=browser)
    page.open_page()
    page.whats_new.click()
    assert whats_new.is_current_link()
    header = whats_new.header_should_be_present()
    whats_new.element_should_have_correct_text(header, "What's New")


@allure.link("https://trello.com/c/bCZOe2Tp/97-tc006006003-whats-new-page-check-lumas-latest-list-visibility")
@allure.title("TC_006.006.003 | Check Luma`s latest list visibility")
def test_luma_latest_list_visibility():
    page = MainPage(browser=browser)
    page.open_page()
    page.whats_new.click()
    whats_new.luma_latest_should_be_present()
    item_number = whats_new.get_number_of_luma_latest()
    assert item_number == 4
    assert whats_new.men_and_women_items_both_should_be_present() is True


@allure.title(
    "TC_006.002.004 | What's new > Eco Collection New* > Redirection to the product page by clicking on the product "
    "name")
@allure.link('https://trello.com/c/GO8VRlcn')
def test_eco_collection_redirection_to_product_by_clicking_to_name(login):
    whats_new.open_category('Shop Eco Friendly')
    whats_new.click_to_product_name('Layla Tee')
    whats_new.url_should_contain('layla-tee')
    product.title_should_have_text('Layla Tee')


@allure.title(
    "TC_006.002.003 I What's new > Eco Collection New* > Redirection to the product page by clicking on the image")
@allure.link('https://trello.com/c/aj3EgeOa')
def test_eco_collection_redirection_to_product_by_clicking_to_img(login):
    whats_new.open_category('Shop Eco Friendly')
    whats_new.click_to_img_with_name('Layla Tee')
    whats_new.url_should_contain('layla-tee')
    product.title_should_have_text('Layla Tee')


@allure.title('TC_006.005.001 | Verify that User gets error message This this is required field in red color')
def test_user_gets_error_message():
    page = MainPage(browser=browser)
    page.open_page()
    page.whats_new.click()
    whats_new.click_bras_and_tank_link()
    whats_new.click_breathe_easy_tank_item()
    whats_new.add_to_cart_button()
    s(WNPL.ERROR_MASSAGE_UNDER_SIZE).should(have.text('This is a required field.'))
    s(WNPL.ERROR_MASSAGE_UNDER_COLOR).should(have.text('This is a required field.'))


@allure.link('https://trello.com/c/lbjGjlg5/')
@allure.title("TC_006.002.001| What's new > Eco Collection New* > Changing the color in product list")
def test_eco_collection_change_color_in_product_list(login):
    whats_new.open_category('Shop Eco Friendly')
    whats_new.change_product_color('Layla Tee', 'Blue')
    whats_new.color_label_should_be_selected('Layla Tee', 'Blue', '#ff5501')
    whats_new.product_img_should_be_color('Layla Tee', 'blue')


@allure.link('https://trello.com/c/E9ZewRUB')
@allure.title("TC_006.002.002| What's new > Eco Collection New* > Visibility of buttons on product card")
def test_eco_collections_products_buttons_visibility(login):
    whats_new.open_category('Shop Eco Friendly')
    whats_new.should_be_visible_buttons_on_product_card('Add to Cart', 'Add to Wish List', 'Add to Compare')


@allure.link('https://trello.com/c/dGGLziIU')
@allure.title("TC_006.005.002 | What's new > Eco Collection New*> Verify User gets error message")
def test_user_gets_error_massage():
    page = MainPage(browser=browser)
    page.open_page()
    page.whats_new.click()
    whats_new.click_bras_and_tank_link()
    whats_new.click_breathe_easy_tank_item()
    whats_new.add_to_wish_list_button()
    assert s(WNPL.ERROR_MASSAGE_YOU_MUST_LOGIN_OR_REGISTER).should(
        have.text('You must login or register to add items to your wishlist.'))


@allure.link('https://trello.com/c/g5xgzhu7')
@allure.title("TC_006.005.003| What's new > Eco Collection New*> Verify user gets successful message")
def test_user_gets_successful_massage(browser_management):
    page = MainPage(browser=browser)
    page.open_page()
    page.whats_new.click()
    whats_new.click_bras_and_tank_link()
    whats_new.click_breathe_easy_tank_item()
    whats_new.add_to_compare_button()
    assert s(WNPL.YOU_ADDED_PRODUCT).should(have.text('You added product Breathe-Easy Tank to the comparison list.'))
