from selene import browser, command
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss

erin_recommends_url = 'https://magento.softwaretestingboard.com/collections/erin-recommends.html'

PAGE_HEADER = "//span[@data-ui-id='page-title-wrapper']"
HOME_ERIN_BLOCK = "//a[@class='block-promo home-erin']"
ITEM_JADE_YOGA_JACKET = "//a[contains(text(), 'Jade Yoga Jacket')]"
ADD_TO_COMPARE = ".actions-secondary a[data-post*='1332']:nth-child(2)"
PRODUCT_LIST = "//div[@class='products wrapper list products-list']"
TEXT_COMPARE_ITEMS = "//a[@title='Compare Products']"
pagination_control = "//div[@class='pages']"
LIST_VIEW_BUTTON = "//a[@id='mode-list']"
page_dropdown = "(//select[@data-role='limiter'])[2]"

PRODUCTS = browser.all(".product-item")
page_next = s("(//a[@title='Next'])[2]")
products = ss(".product-item-info")


def open_page():
    browser.open(erin_recommends_url)


def get_current_url():
    return browser.driver.current_url


def move_to_erin_page():
    s(HOME_ERIN_BLOCK).click()


def is_header_present():
    return s(PAGE_HEADER).should(be.present)


def is_element_text_correct(element, text):
    element.should(have.text(text))


def scroll_to_footer():
    s("//footer[@class='page-footer']").perform(command.js.scroll_into_view)


def is_pagination_visible():
    s(pagination_control).should(be.visible)


def click_next():
    page_next.click()


def verify_minimum_page_numbers(minimum_count):
    browser.all(pagination_control).should(have.size_greater_than_or_equal(minimum_count))


def is_next_button_visible():
    page_next.should(be.visible)


def expand_show_per_page_dropdown():
    s(page_dropdown).click()


def select_per_page_option(selected_option):
    s(page_dropdown).element(f".//option[@value='{selected_option}']").click()


def verify_number_of_product_displayed(min_count, max_count):
    products_count = len(PRODUCTS)
    assert min_count <= products_count <= max_count, f"Number of displayed products {products_count} is not within the expected range {min_count}-{max_count}"


def switch_to_list_view():
    s(LIST_VIEW_BUTTON).click()


def is_list_view_activate():
    s(PRODUCT_LIST).should(have.css_class("products-list"))


def hover_click_item():
    s(ITEM_JADE_YOGA_JACKET).hover()
    s(ADD_TO_COMPARE).click()


def click_text_compare_products():
    s(TEXT_COMPARE_ITEMS).click()


def assert_text_of_element(locator, expected_text):
    s(locator).should(have.text(expected_text))


def assert_current_url():
    assert get_current_url() == erin_recommends_url
