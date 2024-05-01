import allure
from selene import browser
from pages.main_page import MainPage


@allure.link('https://trello.com/c/i4IEFhzW')
@allure.suite("US_008.001.013 | Verifying Men > Displayed, Clickable, Redirection")
class TestVerifyingMenLink:
    @allure.feature("Verifying Men > Displayed, Clickable, Redirection from Main page")
    def test_verifying_men_link_is_displayed_clickable_redirection(self):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Assert men page menu presence"):
            page.is_men_present()
        with allure.step("Assert there is the Men link in the menu"):
            page.is_men_link_present()
            page.is_men_present()
            page.is_men_visible()
            page.is_men_have_text()
            page.find_men_link().hover()
        with allure.step("Assert there is the Men Tops link in the menu"):
            page.is_men_tops_link_present()
            page.is_men_tops_present()
            page.is_men_tops_visible()
            page.is_men_tops_have_text()
        with allure.step("Assert there is the Men Bottoms link in the menu"):
            page.is_men_bottoms_link_present()
            page.is_men_bottoms_present()
            page.is_men_bottoms_visible()
            page.is_men_bottoms_have_text()
            page.find_men_tops_link().click()
