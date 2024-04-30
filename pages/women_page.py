from selene import browser
from selene.support.shared.jquery_style import s
from pages.locators import WomenPageLocators as WPL
from data.links import *


def visit():
    browser.open(WOMEN_PAGE_LINK)


def move_to_woman_menu():
    s(WPL.WOMEN_MENU).hover()


def click_dropdown_tops_link():
    s(WPL.TOPS_LINK).click()


def click_dropdown_bottoms_link():
    s(WPL.BOTTOMS_LINK).click()
