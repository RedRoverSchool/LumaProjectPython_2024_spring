import allure
from selene import browser
from pages import notes
from pages.main_page import MainPage


def test_notes_in_footer_is_visible():
    page = MainPage(browser=browser)
    page.open_page()
    page.scrol_to_footer()
    page.move_to_element()
    page.is_visible_Notes()


def test_notes_in_footer_is_clickable():
    page = MainPage(browser=browser)
    page.open_page()
    page.scrol_to_footer()
    page.move_to_element()
    page.is_clicable_Notes()


@allure.title("Verify redirect from Notes to Software Testing Board")
def test_redirect_to_contact_form_from_notes():
    page = MainPage(browser=browser)
    page.open_page()
    original_window = browser.driver.current_window_handle
    page.click_Notes()
    for window_handle in browser.driver.window_handles:
        if window_handle != original_window:
            browser.driver.switch_to.window(window_handle)
            break
    page.check_for_redirection_to_magento_store_notes()
    notes.magento_should_have_text("Magento 2 Store(Sandbox site) – Notes")
