import allure
from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s

from data.links import POPULAR_SEARCH_TERMS
from data.links import POPULAR_SEARCH_TERMS_URL
from data.page_data import PopularSearchTermsData as PSTD
from pages.locators import PopularSearchTermsLocators as PSTL
from pages.locators import SearchTermsLocators
from pages.popular_search_terms_page import PopularSearchTerms


@allure.suite("US_015.003 | Popular Search Terms > Redirection")
class TestPopularSearchTerms:
    @allure.link("https://trello.com/c/YgMgvvIu")
    @allure.title("TC_015.003.002 | Popular Search Terms > Redirection > The page title contains "
                  "Search results for: and the keyword")
    def test_title_search_results_for(self):
        page = PopularSearchTerms(browser)
        page.visit(POPULAR_SEARCH_TERMS)
        page.click_on_link(PSTL.HOODIE_LINK)

        page.assert_text_of_element(PSTL.SEARCH_RESULTS_HEADER, PSTD.result_page_header)


    @allure.link('https://trello.com/c/Q7ZoeJxT/286-tc015003001-popular-search-terms-search-results-check-after-clicking-the-popular-search-terms-links')
    @allure.title('TC_015.003.001 | Popular Search Terms > Search results check after clicking the "Popular Search Terms" links')
    def test_popular_search_terms_links_results(self):
        browser.open(POPULAR_SEARCH_TERMS_URL)
        s('//*[@id="maincontent"]/div[3]/div/ul/li[32]/a').click()

        assert browser.element(SearchTermsLocators.PRODUCT_ITEM_NAMES).matching(have.text('Jacket'))
