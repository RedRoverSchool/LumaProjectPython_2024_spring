import allure
from selene import browser, have, be
from selene.support.shared.jquery_style import s
from pages.sale_page import SalePage
from pages.locators import SalePageLocators
from pages.locators import BaseLocators
from data.links import MEN_TOPS_HOODIES_URL
from data.page_data import MenTops


class TestMenDeals:
    @allure.suite("US_011.003 | Sale > MEN’s DEALS on side panel")
    @allure.link('https://trello.com/c/aUn0RNxA')
    @allure.feature("TC_011.003.001 I Sale > MEN’s DEALS on side panel > Verify 'Hoodies and Sweatshirts' "
                    "link is visible and clickable, correct redirection")
    def test_verify_hoodies_clickability_visibility_redirection(self, item='Hoodies and Sweatshirts'):
        sale_page = SalePage(browser=browser)
        sale_page.open_page()
        s(SalePageLocators.MENS_DEALS_BASE_LOCATOR.format(item=item)).should(be.visible).click()
        s(BaseLocators.PAGE_HEADER).should(have.text(MenTops.men_tops_titles[0]))
        assert sale_page.get_current_url() == MEN_TOPS_HOODIES_URL
