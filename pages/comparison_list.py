from selene import browser, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.by import By
from pages.locators import WhatsNewPageLocators as LumaListLocators
from pages.locators import ComparisonListLocators as CompListLocators
from data.page_data import ComparisonListData


WHATS_NEW_PAGE_URL = "https://magento.softwaretestingboard.com/what-is-new.html"

def visit(url=WHATS_NEW_PAGE_URL):
    browser.open(url)

def get_products():
    return ss(CompListLocators.ITEM_CARDS)

def has_success_message():
    assert s(CompListLocators.COMPARISON_LIST_SUCCESS_MSG).should(have.text(ComparisonListData.success_message))

def is_comparison_list_empty():
    s(CompListLocators.EMPTY_MESSAGE).should(have.text(ComparisonListData.empty_message2))


