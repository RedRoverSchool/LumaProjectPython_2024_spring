import allure
import pytest
from selene import browser
from pages.men_page import MenPage
from pages.main_page import MainPage
from data.links import MenUrls


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
            page.nav.verify_dropdown_menu()
            page.nav.goto_men_page()

    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_redirection_in_the_men_page(self):
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

    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_redirection_in_the_tops_page(self):
        men = self.hover_men_nav()
        with allure.step("Assert there is the Men Tops link in the menu"):
            men.nav.verify_nav_mens_tops()
            men.nav.find_men_tops_link().hover()
        with allure.step("Verify the presence of a submenu under the Tops link"):
            men.nav.verify_sub_men_tops()
            men.nav.verify_sub_men_tops_href_elements()

    @pytest.mark.parametrize("name", MenUrls.men_top_urls.keys())
    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_redirection_in_the_men_page_tops(self, name):
        men = self.hover_men_nav()
        with allure.step("Click on each submenu item(Jackets, Hoodies & Sweatshirts, Tees, Tanks)"):
            men.nav.find_men_tops_link().hover()
            men.nav.click_to(name)
            men.nav.is_have_header(name)
            assert men.get_current_url() == MenUrls.men_top_urls[name]

    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_redirection_in_the_bottoms_page(self):
        men = self.hover_men_nav()
        men.nav.verify_nav_mens_bottoms()
        men.nav.find_men_bottoms_link().hover()
        with allure.step("Verify the presence of a submenu under the Tops link"):
            men.nav.verify_sub_men_bottoms()
            men.nav.verify_sub_men_bottoms_href_elements()

    @pytest.mark.parametrize("name", MenUrls.men_bottoms_urls.keys())
    @allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
    def test_verifying_men_link_is_displayed_clickable_in_the_men_page_bottoms(self, name):
        with allure.step("Click on each submenu item(Pants and Shorts)"):
            men = self.hover_men_nav()
            men.nav.find_men_bottoms_link().hover()
            men.nav.click_to(name)
            men.nav.is_have_header(name)
            assert men.get_current_url() == MenUrls.men_bottoms_urls[name]

    @staticmethod
    def hover_men_nav():
        men = MenPage(browser=browser)
        men.open_page()
        men.nav.find_men_link().hover()
        return men
