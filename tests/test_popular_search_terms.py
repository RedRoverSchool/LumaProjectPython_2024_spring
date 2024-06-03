import allure

from pages import popular_search_terms


@allure.suite("US_015.003 | Popular Search Terms > Redirection")
class TestPopularSearchTerms:
    @allure.link("https://trello.com/c/YgMgvvIu")
    @allure.title("TC_015.003.002 | Popular Search Terms > Redirection > The page title contains "
                  "Search results for: and the keyword")
    def test_title_search_results_for(self):
        popular_search_terms.open_page()
        popular_search_terms.click_on_hoodie_link()
        popular_search_terms.assert_header_text('Search results for: \'HOODIE\'')

    @allure.link('https://trello.com/c/Q7ZoeJxT')
    @allure.title('TC_015.003.001 | Popular Search Terms > Search results check after clicking the'
                  '"Popular Search Terms" links')
    def test_popular_search_terms_jacket_link_results(self):
        popular_search_terms.open_page()
        popular_search_terms.jacket_link.click()
        popular_search_terms.card_titles_should_be_matching_to_link()
