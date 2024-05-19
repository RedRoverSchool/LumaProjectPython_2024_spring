from selene import browser, have
from selene.support.shared.jquery_style import s
from pages.locators import WomenPageLocators as WPL
from data.links import *
from pages.locators import BaseLocators as BL
from pages.locators import CompareProductsPage as CPP


def visit():
    browser.open(WOMEN_PAGE_LINK)


def move_to_woman_menu():
    s(WPL.WOMEN_MENU).hover()


def click_dropdown_tops_link():
    s(WPL.TOPS_LINK).click()


def click_dropdown_bottoms_link():
    s(WPL.BOTTOMS_LINK).click()


def hover_product_card():
    s(WPL.RADIANT_TEE_HOTSELLERS_SECT).hover()


def click_add_to_compare_icon():
    s(WPL.ADD_TO_COMPARE_ICON).click()


def click_compare_btn():
    s(WPL.COMPARE_BTN).click()


def assert_page_title():
    assert s(BL.PAGE_TITLE).should(have.text('Compare Products')), "wrong title"


def assert_comp_list_item():
    assert s(CPP.COMP_LIST_RADIANT_TEE).should(have.text('Radiant Tee')), "wrong item"
