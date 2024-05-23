from selene.support.shared import browser
import allure
from pages.main_page import MainPage


@allure.title("Verify the click on the Notes link redirects to the Magento Store Notes page")
@allure.link("https://trello.com/c/oJB7xCdy")
def test_notes_link_redirection():
    main_page = MainPage(browser=browser)

    main_page.open_page()
    main_page.hover_down_footer()
    main_page.click_notes_link()
    main_page.accept_cookies()
    main_page.assert_notes_page_title()
    main_page.assert_notes_page_url()
