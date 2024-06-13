import allure
import pytest
from pages import search_terms_page


@allure.feature('Popular Search Terms')
@allure.title('Verify that the title is visible')
@allure.link('https://trello.com/c/tnpU7rqU')
def test_015_001_001_search_terms_title_is_visible():
    search_terms_page.visit()
    search_terms_page.title_is_correct()


@allure.feature('Popular Search Terms')
@allure.title('Verify the number of search terms is 100')
@allure.link('https://trello.com/c/9oDGaMAB')
def test_count_search_terms():
    search_terms_page.visit()
    search_terms_page.search_terms_list_have_100()


@allure.feature('Popular Search Terms')
@allure.title('Search terms in the list have sizes, ranging from 76% to 136%')
@allure.link('https://trello.com/c/VwsOnXB6')
def test_check_if_search_terms_has_size_from_76_till_136RF():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    list_font_sizes = search_terms_page.extract_font_sizes_from_search_terms(terms)
    search_terms_page.check_min_and_max_font_sizes(list_font_sizes)


@pytest.mark.skip(reason='you shall not pass')
@allure.feature('Popular Search Terms')
@allure.title('Verify the order of popular search terms')
@allure.link('https://trello.com/c/8jDgYDYW')
def test_015_002_006_order_search_terms():
    search_terms_page.visit()
    search_terms_page.order_search_terms()


@allure.feature('Popular Search Terms')
@allure.link('https://trello.com/c/XL8szgwc')
@allure.title('List of keywords is sorted alphabetically')
def test_check_if_search_terms_are_sorted():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    lst_nonsorted = search_terms_page.extract_keywords_from_search_terms_as_it_is(terms)
    lst_sorted = search_terms_page.extract_keywords_from_search_terms_sorted(terms)
    search_terms_page.compare_list_sorted_stripped_and_original(lst_nonsorted, lst_sorted)


@allure.feature('Popular Search Terms')
@allure.title('Verify the absence of duplicate keywords')
@allure.link('https://trello.com/c/RGOSzLMa')
def test_015_002_005_unique_search_terms():
    search_terms_page.visit()
    keyword_texts, keywords_set = search_terms_page.unique_search_terms()
    assert len(keyword_texts) == len(keywords_set)


@allure.feature('Popular Search Terms')
@allure.title('Verify all links are clickable')
@allure.link('https://trello.com/c/9VW3bwiJ')
def test_015_002_003_clickable_by_keywords():
    search_terms_page.visit()
    search_terms_page.clickable_by_keywords()


@allure.feature('Popular Search Terms')
@allure.title('Keywords HOODIE, jacket, pants, shirt have enlarged font size')
@allure.link("https://trello.com/c/I0RafTpi")
def test_check_if_specified_words_is_bigger_than_88():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    specific_words_and_sizes = search_terms_page.select_specific_words_and_terms(terms)
    search_terms_page.compare_selected_words_and_their_sizes(specific_words_and_sizes)


@allure.feature('Popular Search Terms')
@allure.title('At least 5 search terms in the list have font size larger than 88%')
@allure.link("https://trello.com/c/4DgqawVv")
def test_check_if_5_search_terms_is_bigger():
    search_terms_page.visit()
    terms = search_terms_page.collect_all_search_terms()
    list_font_sizes = search_terms_page.extract_font_sizes_from_search_terms(terms)
    search_terms_page.check_size_of_5_last_words_in_sorted_list(list_font_sizes)


@allure.feature('Popular Search Terms')
@allure.title('Visibility and clickability> Verify the visibility of the list')
@allure.link('https://trello.com/c/MAmB9buH')
def test_visibility_of_the_list():
    search_terms_page.visit()
    search_terms_page.visibility_of_the_list()


@allure.feature('Popular Search Terms')
@allure.title('Verify each keyword is a hyperlink')
@allure.link('https://trello.com/c/D9vY0jU3')
def test_verify_keywords_hyperlink():
    search_terms_page.visit()
    search_terms_page.verify_keywords_hyperlink()


@allure.feature('Popular Search Terms')
@allure.title('Verify the destination page for each keyword')
@allure.link('https://trello.com/c/HKRodNvW')
def test_navigated_to_after_click_keyword():
    search_terms_page.visit()
    search_terms_page.navigated_to_after_click_keyword()
