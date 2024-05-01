import allure
from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.action_chains import ActionChains
from pages.whats_new_page import WhatsNewPage
from pages.locators import ProductItem as Product
from pages.locators import LoginPage as Login


@allure.link('https://trello.com/c/jgLmzBZX')
@allure.feature("TC_006.004.005 | What's new > Eco Collection New")
def test_add_product_to_wishlist_as_non_logged_in_user():
    message = "You must login or register to add items to your wishlist"
    page = WhatsNewPage(browser=browser)
    with allure.step("Assert current url == What's New Page url"):
        page.open_page()
        page.is_current_link()
    with allure.step("Click button more"):
        page.is_button_visible()
        page.click_button_more()
    with allure.step("Go to product item"):
        product = ss(Product.ITEM_INFO).first()
        page.scroll_to(product)
        ActionChains(browser.driver).move_to_element(product).perform()
    with allure.step("Add to Wish List"):
        s(Product.WISH_LIST).click()
    with allure.step("Redirect to Customer Login and verify message"):
        s(Login.PAGE_TITLE_WRAPPER).should(have.text("Customer Login"))
        s(Login.MESSAGE_TEXT).should(have.text(message))
