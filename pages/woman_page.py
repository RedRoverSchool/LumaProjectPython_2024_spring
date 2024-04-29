from selene import browser
from selene.support.shared.jquery_style import s
from locators.woman_page_locators import WomanPageLocators as WPL
from data.links import *


def visit():
    browser.open(WOMAN_PAGE_LINK)


def move_to_woman_menu():
    s(WPL.WOMAN_MENU).hover()
    s(WPL.TOPS_LINK).click()
