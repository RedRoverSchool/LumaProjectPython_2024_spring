import allure
from selene import browser, be
from selene.support.shared.jquery_style import s

from pages.main_page import MainPage

@allure.title("Test MiniCart has link View and edit cart")
class TestMiniCart:
    def test_minicart_has_link(self, browser_management):

        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Put one item in the cart"):
            s('#option-label-size-143-item-166').click()
            s('#option-label-color-93-item-50').click()
            s('/html/body/div[2]/main/div[3]/div/div[3]/div[3]/div/div/ol/li[1]/div/div/div[4]/div/div[1]/form/button').click()
        with allure.step("Find and click the cart icon"):
            page.find_cart_icon().click()
        with allure.step("The minicart is open"):
            page.is_minicart_present()
        with (allure.step("Minicart has link View and Edit Cart")):
            page.is_minicart_have_text()

