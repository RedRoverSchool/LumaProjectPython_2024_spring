from selene import browser, have
from data.links import *
from pages import woman_page


def test_checking_page_redirection_to_tops_elements():
    woman_page.visit()
    woman_page.move_to_woman_menu()
    browser.should(have.url(TOPS_WOMAN_PAGE_LINK))
