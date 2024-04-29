from selene import browser, have
from data.links import *
from pages import woman_page


def test_checking_page_redirection_to_tops_elements():
    woman_page.visit()
    woman_page.move_to_woman_menu()
    woman_page.click_dropdown_tops_link()
    browser.should(have.url(TOPS_WOMAN_PAGE_LINK))


def test_checking_page_redirection_to_bottom_elements():
    woman_page.visit()
    woman_page.move_to_woman_menu()
    woman_page.click_dropdown_bottoms_link()
    browser.should(have.url(BOTTOMS_WOMAN_PAGE_LINK))

