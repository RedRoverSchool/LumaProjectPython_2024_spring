import allure
import pytest
from pages import search_terms_page


@allure.link('https://trello.com/c/tnpU7rqU')
def test_015_001_001_search_terms_title_is_visible():
    search_terms_page.visit()
    search_terms_page.title_is_correct()


@allure.link('https://trello.com/c/9oDGaMAB')
def test_015_001_002_count_search_terms():
    search_terms_page.visit()
    search_terms_page.search_terms_list_have_100()


@allure.link('https://trello.com/c/VwsOnXB6')
def test_015_001_003_check_if_search_terms_has_size_from_76_till_136RF():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    list_font_sizes = search_terms_page.extract_font_sizes_from_search_terms(terms)
    search_terms_page.check_min_and_max_font_sizes(list_font_sizes)


@pytest.mark.skip(reason='you shall not')
@allure.link('https://trello.com/c/8jDgYDYW')
def test_015_002_006_order_search_terms():
    search_terms_page.visit()
    search_terms_page.order_search_terms()


@allure.link('https://trello.com/c/XL8szgwc')
def test_015_001_006_check_if_search_terms_are_sorted():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    lst_nonsorted = search_terms_page.extract_keywords_from_search_terms_as_it_is(terms)
    lst_sorted = search_terms_page.extract_keywords_from_search_terms_sorted(terms)
    search_terms_page.compare_list_sorted_stripped_and_original(lst_nonsorted, lst_sorted)


@allure.feature('Popular Search Terms')
@allure.link('https://trello.com/c/RGOSzLMa')
def test_015_002_005_unique_search_terms():
    search_terms_page.visit()
    keyword_texts, keywords_set = search_terms_page.unique_search_terms()
    assert len(keyword_texts) == len(keywords_set)


@allure.feature('Popular Search Terms')
@allure.link('https://trello.com/c/9VW3bwiJ')
def test_015_002_003_clickable_by_keywords():
    search_terms_page.visit()
    search_terms_page.clickable_by_keywords()


@allure.link("https://trello.com/c/I0RafTpi")
def test_015_001_005_check_if_specified_words_is_bigger_than_88():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    specific_words_and_sizes = search_terms_page.select_specific_words_and_terms(terms)
    search_terms_page.compare_selected_words_and_their_sizes(specific_words_and_sizes)


@allure.link("https://trello.com/c/4DgqawVv")
def test_015_001_004_check_if_5_search_terms_is_bigger():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    list_font_sizes = search_terms_page.extract_font_sizes_from_search_terms(terms)
    search_terms_page.check_size_of_5_last_words_in_sorted_list(list_font_sizes)


@allure.title('TC_015.002.007 Popular Search Terms > Visibility and clickability> Verify the visibility of the list')
@allure.feature('Popular Search Terms')
@allure.link('https://trello.com/c/MAmB9buH')
def test_015_002_007_visibility_of_the_list():
    search_terms_page.visit()
    search_terms_page.visibility_of_the_list()


@allure.feature('Popular Search Terms')
@allure.link('https://trello.com/c/D9vY0jU3')
def test_015_002_002_verify_keywords_hyperlink():
    search_terms_page.visit()
    search_terms_page.verify_keywords_hyperlink()

