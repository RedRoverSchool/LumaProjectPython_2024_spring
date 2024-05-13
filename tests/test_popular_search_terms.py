import allure
from selene import browser
from pages.popular_search_terms_page import PopularSearchTerms
from data.links import POPULAR_SEARCH_TERMS
from pages.locators import PopularSearchTermsLocators as PSTL
from data.page_data import PopularSearchTermsData as PSTD



@allure.suite("US_015.003 | Popular Search Terms > Redirection")
class TestPopularSearchTerms:
    @allure.link("https://trello.com/c/YgMgvvIu")
    @allure.title("TC_015.003.002 | Popular Search Terms > Redirection > The page title contains "
                  "Search results for: and the keyword")
    def test_title_search_results_for(self, browser_management):
        page = PopularSearchTerms(browser)
        page.visit(POPULAR_SEARCH_TERMS)
        page.click_on_link(PSTL.HOODIE_LINK)

        page.assert_text_of_element(PSTL.SEARCH_RESULTS_HEADER, PSTD.result_page_header)
