from selene import browser, command
from selene.support.conditions import have, be
from selene.support.conditions.have import attribute
from selene.support.shared.jquery_style import s

from pages.base_page import BasePage
from pages.locators import ErinRecommendLocators as ERL
from data.links import ERIN_RECOMMENDS_URL


class ErinRecommendsPage(BasePage):

    def open_page(self):
        self.visit(ERIN_RECOMMENDS_URL)

    def move_to_erin_page(self):
        s(ERL.HOME_ERIN_BLOCK).click()

    def is_header_present(self):
        return s(ERL.PAGE_HEADER).should(be.present)

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def scroll_to_footer(self):
        self.scroll_to(s(ERL.FOOTER))

    def is_pagination_visible(self):
        return s(ERL.PAGINATION_CONTROL).should(be.visible)

    def click_next(self):
        return s(ERL.PAGE_NEXT).click()

    def verify_minimum_page_numbers(self, minimum_count):
        return browser.all(ERL.PAGINATION_CONTROL).should(have.size_greater_than_or_equal(minimum_count))

    def is_next_button_visible(self):
        return s(ERL.PAGE_NEXT).should(be.visible)

    def expand_show_per_page_dropdown(self):
        return s(ERL.PAGE_DROPDOWN).click()

    def select_per_page_option(self, selected_option):
        return s(ERL.PAGE_DROPDOWN).element(f".//option[@value='{selected_option}']").click()

    def verify_number_of_product_displayed(self, min_count, max_count):
        products_count = len(ERL.PRODUCTS)
        assert min_count <= products_count <= max_count, f"Number of displayed products {products_count} is not within the expected range {min_count}-{max_count}"

    def switch_to_list_view(self):
        return s(ERL.LIST_VIEW_BUTTON).click()

    def is_list_view_activate(self):
        return s(ERL.PRODUCT_LIST).should(have.css_class("products-list"))

    def hover_click_item(self):
        s(ERL.ITEM_JADE_YOGA_JACKET).hover()
        s(ERL.ADD_TO_COMPARE).click()

    def click_text_compare_products(self):
        s(ERL.TEXT_COMPARE_ITEMS).click()
