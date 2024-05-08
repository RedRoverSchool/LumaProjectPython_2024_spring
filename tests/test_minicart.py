import allure
from selene import browser
from selene.support.shared.jquery_style import s

from pages.main_page import MainPage
from pages.locators import ProductLocators as PL

@allure.title("Test MiniCart has link View and edit cart")
class TestMiniCart:
    def test_minicart_has_link(self):

        page = MainPage(browser=browser)
        page.open_page()
        s(PL.RADIANT_TEE_SIZE).click()
        s(PL.RADIANT_TEE_COLOR).click()
        s(PL.ADD_TO_CART_BUTTON_FROM_MAINPAGE).click()
        page.is_cart_icon_present()
        page.find_cart_icon().click()
        page.is_minicart_present()
        page.is_minicart_have_link()


