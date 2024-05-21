from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from data.links import MEN_SALE_PAGE_URL
from data.page_data import MenSalePageData as data
from pages.components import nav
from pages.locators import BaseLocators as Header, MenSaleLocators as ms_locators


class MenSalePage:

    title_page = s(ms_locators.PAGE_TITLE)
    list_items = ss(ms_locators.LIST_ITEM)
    product_images = ss(ms_locators.PRODUCT_IMAGE)
    grid_mode_option = s(ms_locators.GRID_MODE_OPTION)
    list_mode_option = s(ms_locators.LIST_MODE_OPTION)
    selected_view_option = s(ms_locators.SELECTED_MODE_OPTION)
    products_wrapper = s(ms_locators.PRODUCTS_WRAPPER)

    def __init__(self, browser):
        self.browser = browser
        self.nav = nav
        self.browser.open(MEN_SALE_PAGE_URL)

    @staticmethod
    def get_bread_crumbs():
        breadcrumbs_titles = []
        for i in ss(Header.BREADCRUMBS_LIST):
            breadcrumbs_titles.append(i.locate().text)
        return breadcrumbs_titles

    @staticmethod
    def are_bread_crumbs_present():
        s(Header.BREADCRUMBS).should(be.present)

    def is_page_title_present(self):
        self.title_page.should(be.present)

    def is_page_title_correct(self):
        self.title_page.should(have.text(data.page_title))

    def get_number_of_items_in_te_list(self):
        return str(len(self.list_items))

    def are_only_product_cards_for_men_present(self):
        for card in self.product_images:
            card.should(have.attribute("src").value_containing("/m/"))

    @staticmethod
    def is_product_list_present():
        s(ms_locators.PRODUCT_LIST).should(be.present)

    def is_number_of_items_in_toolbar_corresponds_to_amount_in_list(self):
        s(ms_locators.TOOLBAR_NUMBER).should(have.text(self.get_number_of_items_in_te_list()))

    def check_selected_view_option(self, option: str):
        return self.selected_view_option.should(have.attribute("data-value").value_containing(option))

    def check_products_in_list_arrangement(self, option: str):
        return self.products_wrapper.should(have.attribute("class").value_containing(option))

    def switch_to_display_option(self, option: str):
        return self.list_mode_option.click() if option == 'list' else self.grid_mode_option.click()
