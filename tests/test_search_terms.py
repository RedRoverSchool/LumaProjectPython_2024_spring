import allure
import pytest
from pages.locators import SearchTermsLocators as ST
from pages.locators import BaseLocators as Base
from selene import browser, be, have, query
from selene.support.shared.jquery_style import s, ss
from pages import search_terms_page


@allure.link('https://trello.com/c/tnpU7rqU')
def test_015_001_001_search_terms_title_is_visible():
    browser.open(ST.LINK_SEARCH_TERMS)
    s(Base.PAGE_TITLE).should(have.text("Popular Search Terms"))


@allure.link('https://trello.com/c/9oDGaMAB')
def test_015_001_002_count_search_terms():
    browser.open(ST.LINK_SEARCH_TERMS)
    ss(ST.TERMS_FOR_SEARCH_LIST_QTY).should(have.size(100))


@allure.link('https://trello.com/c/VwsOnXB6')
def test_015_001_003_check_if_search_terms_has_size_from_76_till_136():
    # assert from selenium - how to check sizes
    browser.open(ST.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get(query.attribute("style")).split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    assert min(list_font_sizes) <= 76 and max(list_font_sizes) >= 136, "Font sizes not between 76 and 136"


@pytest.mark.skip('Test have a bug')
@allure.link('https://trello.com/c/8jDgYDYW')
def test_015_002_006_order_search_terms():
    browser.open(ST.LINK_SEARCH_TERMS)
    search_terms_page.order_search_terms()


@allure.link('https://trello.com/c/XL8szgwc')
def test_015_001_006_check_if_search_terms_are_sorted():
    # список ключевых,вытаскиваемых с помощью selene, выглядит не так, как при selenium.
    # Теперь есть лишние пробелы, перевод строки, слова с малой буквы неправильно сортируются.
    # С selenium тест = ОК
    browser.open(ST.LINK_SEARCH_TERMS)
    list_of_goods = []  # good : strip, lower, no spaces
    list_of_goods_from_terms = []  # words from terms applied lower()
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for keyword in terms:
        keyword = keyword.get(query.attribute("text")).strip().replace(" ", "").lower()
        list_of_goods_from_terms.append(keyword.lower())
        list_of_goods.append(keyword)
    list_of_goods_sorted = sorted(list_of_goods)
    assert list_of_goods_from_terms == list_of_goods_sorted


@allure.link('https://trello.com/c/RGOSzLMa')
def test_015_002_005_unique_search_terms():
    browser.open(ST.LINK_SEARCH_TERMS)
    keyword_elements = ss(ST.LIST_OF_SEARCH_TERMS)
    keyword_texts = [k.get(query.attribute("text")).strip() for k in keyword_elements]
    keywords_set = set(keyword_texts)
    assert len(keyword_texts) == len(keywords_set)


@allure.link('https://trello.com/c/9VW3bwiJ')
def test_015_002_003_keywords_clickable():
    browser.open(ST.LINK_SEARCH_TERMS)
    keyword_elements = ss(ST.LIST_OF_SEARCH_TERMS)
    [k.should(be.visible).should(be.clickable) for k in keyword_elements]


@allure.link("https://trello.com/c/I0RafTpi")
def test_015_001_005_check_if_specified_words_is_bigger_than_88():
    words = ["hoodie", "jacket", "pants", "shirt"]
    browser.open(ST.LINK_SEARCH_TERMS)
    list_of_goods = []
    list_font_sizes = []
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for keyword in terms:
        word = keyword.get(query.attribute("text")).strip().replace(" ", "").lower()
        if word in words:
            list_of_goods.append(word)
            g_font, g_size = keyword.get(query.attribute("style")).split(": ")
            g_size = float(g_size.replace("%;", ""))
            list_font_sizes.append(g_size)
    assert set(list_of_goods) == set(words) and all(
        [size > 88 for size in list_font_sizes]), "Selected words have font size bigger than 88%"


@allure.link("https://trello.com/c/4DgqawVv")
def test_015_001_004_check_if_5_search_terms_is_bigger():
    browser.open(ST.LINK_SEARCH_TERMS)
    list_font_sizes = []
    terms = ss(ST.LIST_OF_SEARCH_TERMS)
    for g in terms:
        g_font, g_size = g.get(query.attribute("style")).split(": ")
        g_size = float(g_size.replace("%;", ""))
        list_font_sizes.append(g_size)
    sizes_sorted = sorted(list_font_sizes, reverse=True)
    for size in range(0, 5):
        if sizes_sorted[size] < 88:
            assert False, "List of search terms has not 5 elements which size is bigger than 88%"
