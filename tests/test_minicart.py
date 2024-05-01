import allure
from selene import browser, be
from selene.support.shared.jquery_style import s

from pages.main_page import MainPage
from pages.locators import ProductLocators as PL

@allure.title("Test MiniCart has link View and edit cart")
class TestMiniCart:
    def test_minicart_has_link(self, browser_management):

        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Put Radiant Tee in the cart"):
            s(PL.RADIANT_TEE_SIZE).click()
            s(PL.RADIANT_TEE_COLOR).click()
            s(PL.ADD_TO_CART_BUTTON_FROM_MAINPAGE).click()
        with allure.step("Find and click the cart icon"):
            page.is_find_cart_icon_present()
            page.find_cart_icon().click()
        with allure.step("The minicart is open"):
            page.is_minicart_present()
        with (allure.step("Minicart has link View and Edit Cart")):
            page.is_minicart_have_link()


