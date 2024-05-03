import allure
from selene import browser
from pages.men_page import MenPage
from pages.main_page import MainPage


@allure.link('https://trello.com/c/i4IEFhzW')
@allure.suite("US_008.001 | Verifying Men > Displayed, Clickable, Redirection")
class TestVerifyingMenLink:
    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_redirection_in_the_main_page(self):
        with allure.step("Open home page and check if load successfully"):
            page = MainPage(browser=browser)
            page.open_page()
            page.is_loaded()
        with allure.step("Assert there is the Men link in the menu on the Home Page"):
            page.nav.verify_nav_men()
            page.nav.find_men_link().hover()
            page.nav.verify_nav_men_tops()
            page.nav.verify_nav_men_bottoms()
            page.nav.goto_men_page()

    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_redirection_in_the_men_page(self):
        with allure.step("Open men page"):
            men = MenPage(browser=browser)
            men.open_page()
        with allure.step("Assert there is the Men page is load successfully"):
            men.is_loaded()
            men.is_active()
        with allure.step("Assert there is the Men nav links in the menu on the Men Page"):
            men.nav.verify_nav_men()
            men.nav.find_men_link().hover()
        with allure.step("Assert there is the Men Tops and Bottoms navs is present"):
            men.nav.verify_dropdown_menu()
        with allure.step("Assert there is the Men Tops link in the menu"):
            men.nav.verify_nav_men_tops()
            men.nav.find_men_tops_link().hover()
        with allure.step("6. Verify the presence of a submenu under the Tops link"):
            men.nav.verify_sub_men_tops()
