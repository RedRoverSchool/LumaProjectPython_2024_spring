import data.links
from selene.support.shared import browser
from pages.locators import FooterLocators
from pages.locators import NotesLocators
from selene import have, be, Element
from selene.core import command, query
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss


def hover_down_footer():
    s(FooterLocators.FOOTER_LINKS).hover()


def click_notes_link():
    s(NotesLocators.NOTES).click()


def accept_cookies():
    window_handles = browser.driver.window_handles
    browser.switch_to.window(window_handles[-1])
    browser.with_(timeout=20).element(NotesLocators.COOKIE_MSG).should(be.visible)
    s(NotesLocators.COOKIE_ACCEPT_BTN).click()


def assert_notes_page_title():
    assert s(NotesLocators.NOTES_PAGE_TITLE).should(have.text('Notes')), "wrong title"


def assert_notes_page_url():
    assert data.links.BASE_URL != data.links.NOTES_PAGE_URL, "Not redirected"