import allure
import pytest
from selene import browser
from pages import men_page
from pages.components.nav import men_bottoms_urls, men_top_urls
from pages.main_page import MainPage
from pages.components import nav


@allure.link('https://trello.com/c/i4IEFhzW')
@allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
def test_verifying_men_link_is_displayed_clickable_redirection_in_the_main_page():
    with allure.step("Open home page and check if load successfully"):
        page = MainPage(browser=browser)
        page.open_page()
        page.is_loaded()
    with allure.step("Assert there is the Men link in the menu on the Home Page"):
        nav.verify_nav_men()
        nav.men_link.hover()
        nav.verify_dropdown_menu()
        nav.goto_men_page()


@allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
def test_verifying_men_link_is_displayed_clickable_redirection_in_the_men_page():
    men = men_page
    men.open_page()
    with allure.step("Assert there is the Men page is load successfully"):
        men.check_current_page()
        men.is_active()
    with allure.step("Assert there is the Men nav links in the menu on the Men Page"):
        nav.verify_nav_men()
        nav.men_link.hover()
    with allure.step("Assert there is the Men Tops and Bottoms navs is present"):
        nav.verify_dropdown_menu()


@allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
def test_verifying_men_link_is_displayed_clickable_redirection_in_the_tops_page():
    men_page.open_page()
    nav.men_link.hover()
    with allure.step("Assert there is the Men Tops link in the menu"):
        nav.verify_nav_mens_tops()
        nav.men_tops.hover()
    with allure.step("Verify the presence of a submenu under the Tops link"):
        nav.verify_sub_men_tops()
        nav.verify_sub_men_tops_href_elements()


@pytest.mark.parametrize("name", men_top_urls.keys())
@allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
def test_verifying_men_link_is_displayed_clickable_redirection_in_the_men_page_tops(name):
    men_page.open_page()
    nav.men_link.hover()
    with allure.step("Click on each submenu item(Jackets, Hoodies & Sweatshirts, Tees, Tanks)"):
        nav.men_tops.hover()
        nav.click_to(name)
        nav.is_have_header(name)
        men_page.verify_top_urls(name)


@allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
def test_verifying_men_link_is_displayed_clickable_redirection_in_the_bottoms_page():
    men_page.open_page()
    nav.men_link.hover()
    nav.verify_nav_mens_bottoms()
    nav.men_bottoms.hover()
    with allure.step("Verify the presence of a submenu under the Tops link"):
        nav.verify_sub_men_bottoms()
        nav.verify_sub_men_bottoms_href_elements()


@pytest.mark.parametrize("name", men_bottoms_urls.keys())
@allure.feature("Verifying Men > Displayed, Clickable, Redirection for Men navigator")
def test_verifying_men_link_is_displayed_clickable_in_the_men_page_bottoms(name):
    with allure.step("Click on each submenu item(Pants and Shorts)"):
        men_page.open_page()
        nav.men_link.hover()
        nav.men_bottoms.hover()
        nav.click_to(name)
        nav.is_have_header(name)
        men_page.verify_bottoms_urls(name)
