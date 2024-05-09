from selene import query, have, browser
from selene.support.shared.jquery_style import ss
from pages.locators import SearchTermsLocators as ST


def order_search_terms():
    keyword_elements = ss(ST.LIST_OF_SEARCH_TERMS)
    keyword_texts = [k.get(query.attribute("text")).replace('\n', '') for k in keyword_elements]
    keyword_elements.should(have.exact_texts(sorted(keyword_texts)))
