from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s
import allure
import data.links
from pages.locators import NavigatorLocators, BaseLocators
from pages.main_page import MainPage


@allure.link('https://trello.com/c/4WFy9z5C')
@allure.title('Verify redirection option "Men" menu item to the corresponding page from the "Home Page"')
def test_redirect_to_men_page():
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.handle_cookies_popup()
    s(NavigatorLocators.NAV_MEN).click()

    s(BaseLocators.PAGE_TITLE).should(have.exact_text('Men'))
    assert browser.driver.current_url == data.links.MEN_PAGE_URL, 'wrong URL'
    assert browser.driver.title == 'Men', 'Wrong title'
