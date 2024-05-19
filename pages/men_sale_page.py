from selene import Collection
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from data.links import MEN_SALE_PAGE_URL
from data.page_data import MenSalePageData as data
from pages.components.nav_wigdet import NavComponent
from pages.locators import BaseLocators as Header, MenSaleLocators as ms_locators


class MenSalePage:
    title_page = s(ms_locators.PAGE_TITLE)
    list_items = ss(ms_locators.LIST_ITEM)
    product_images = ss(ms_locators.PRODUCT_IMAGE)
    position_sort_option = s(ms_locators.POSITION_SORT_OPTION)
    product_name_sort_option = s(ms_locators.PRODUCT_NAME_SORT_OPTION)
    price_sort_option = s(ms_locators.PRICE_SORT_OPTION)
    sorter = s(ms_locators.SORTER)
    product_titles = ss(ms_locators.PRODUCT_TITLE)

    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent()
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

    def check_selected_sorting_option(self, option: str):
        if option == "Position":
            return self.position_sort_option.should(have.attribute("selected"))
        elif option == "Product Name":
            return self.product_name_sort_option.should(have.attribute("selected"))
        elif option == "Price":
            return self.price_sort_option.should(have.attribute("selected"))

    def switch_to_sorting_option(self, option: str):
        self.sorter.click()
        if option == "Position":
            self.position_sort_option.click()
        elif option == "Product Name":
            self.product_name_sort_option.click()
        elif option == "Price":
            self.price_sort_option.click()

    def check_product_arrangement_according_to_sort_option(self, option: str):
        if option == "Position":
            self.check_products_arrangement_sorted_by_position(self.product_titles)

    @staticmethod
    def check_products_arrangement_sorted_by_position(products: Collection):
        position_list = []
        for el in products:
            position_title = el.locate().text
            position_list.append(position_title.split()[-1])
        sorted_list = sorted(position_list)
        assert position_list == sorted_list

