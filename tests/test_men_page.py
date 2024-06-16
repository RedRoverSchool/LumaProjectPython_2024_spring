import allure
import data.links
from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s
from pages.locators import NavigatorLocators, BaseLocators
from pages.main_page import MainPage


@allure.feature('Men > Displayed, Clickability, Redirection')
@allure.title('Verify redirection option "Men" menu item to the corresponding page from the "Home Page"')
@allure.link('https://trello.com/c/4WFy9z5C')
def test_redirect_to_men_page():
    main_page = MainPage(browser)
    main_page.open_page()
    main_page.handle_cookies_popup()
    s(NavigatorLocators.NAV_MEN).click()
    s(BaseLocators.page_title).should(have.exact_text('Men'))
    assert browser.driver.current_url == data.links.men_page_url, 'wrong URL'
    assert browser.driver.title == 'Men', 'Wrong title'
