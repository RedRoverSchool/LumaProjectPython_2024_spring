from selene import browser
from selene.support.shared.jquery_style import s
from pages.locators import WomenPageLocators as WPL, ProductLocators as PL
from data.links import *


def visit():
    browser.open(WOMEN_PAGE_LINK)


def move_to_woman_menu():
    s(WPL.WOMEN_MENU).hover()


def click_dropdown_tops_link():
    s(WPL.TOPS_LINK).click()


def move_to_tops_menu():
    s(WPL.TOPS_LINK).hover()


def click_dropdown_bottoms_link():
    s(WPL.BOTTOMS_LINK).click()


def click_dropdown_tees():
    s(WPL.TEES_LINK).click()


def click_radiant_tee():
    s(PL.RADIANT_TEE_LINK).click()

