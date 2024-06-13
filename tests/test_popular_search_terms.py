import allure

from pages import popular_search_terms


@allure.feature("Popular Search Terms > Redirection")
@allure.link("https://trello.com/c/YgMgvvIu")
@allure.title("The page title contains Search results for: and the keyword")
def test_title_search_results_for():
    popular_search_terms.open_page()
    popular_search_terms.click_on_hoodie_link()
    popular_search_terms.assert_header_text('Search results for: \'HOODIE\'')


@allure.feature('Popular Search Terms')
@allure.link('https://trello.com/c/Q7ZoeJxT')
@allure.title('Search results check after clicking the"Popular Search Terms" links')
def test_popular_search_terms_jacket_link_results():
    popular_search_terms.open_page()
    popular_search_terms.jacket_link.click()
    popular_search_terms.card_titles_should_be_matching_to_link()
