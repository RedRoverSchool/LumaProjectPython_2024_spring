from pages.locators import *
from data.links import *
from pages.footer import Footer
import allure
from selene import browser, by, be, have, support
from selene.support.shared.jquery_style import s


def test_notes_in_footer_is_visible():
    footer = Footer(browser=browser)
    footer.open_base_page()
    footer.scrol_to_footer()
    footer.move_to_element()
    footer.is_visible_Notes()


def test_notes_in_footer_is_clickable():
    footer = Footer(browser=browser)
    footer.open_base_page()
    footer.scrol_to_footer()
    footer.move_to_element()
    footer.is_clicable_Notes()


@allure.title("Verify redirect from Notes to Software Testing Board")
def test_redirect_to_contact_form_from_notes():
    browser.open(BASE_URL)
    original_window = browser.driver.current_window_handle
    s(FooterLocators.NOTES).click()
    for window_handle in browser.driver.window_handles:
        if window_handle != original_window:
            browser.driver.switch_to.window(window_handle)
            break
    browser.should(have.url(SOFTWARE_TESTING_BOARD))
    s("h1.alignwide").should(have.text("Magento 2 Store(Sandbox site) – Notes"))
