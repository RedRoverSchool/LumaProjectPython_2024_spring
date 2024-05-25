from selene import Collection
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from data.links import MEN_SALE_PAGE_URL
from data.page_data import MenSalePageData as data
from pages.locators import BaseLocators as Header

title_page = s("[data-ui-id='page-title-wrapper']")
list_items = ss("li.product-item")
product_images = ss("img.product-image-photo")
grid_mode_option = s(".toolbar.toolbar-products:nth-child(3) > .modes > #mode-grid")
list_mode_option = s(".toolbar.toolbar-products:nth-child(3) > .modes > #mode-list")
selected_view_option = s(".toolbar.toolbar-products:nth-child(3) > .modes > strong[data-value]")
products_wrapper = s("div.products.wrapper")


def open_page():
    browser.open(MEN_SALE_PAGE_URL)


def get_bread_crumbs():
    breadcrumbs_titles = []
    for i in ss(".breadcrumbs li"):
        breadcrumbs_titles.append(i.locate().text)
    return breadcrumbs_titles


def are_bread_crumbs_present():
    s(Header.BREADCRUMBS).should(be.present)


def is_page_title_present():
    title_page.should(be.present)


def is_page_title_correct():
    title_page.should(have.text(data.page_title))


def get_number_of_items_in_te_list():
    return str(len(list_items))


def are_only_product_cards_for_men_present():
    for card in product_images:
        card.should(have.attribute("src").value_containing("/m/"))

    @staticmethod
    def is_product_list_present():
        s(ms_locators.PRODUCT_LIST).should(be.present)

    def is_number_of_items_in_toolbar_corresponds_to_amount_in_list(self):
        s(ms_locators.TOOLBAR_NUMBER).should(have.text(self.get_number_of_items_in_te_list()))

    def check_selected_view_option(self, option: str):
        return self.selected_view_option.should(have.attribute("data-value").value_containing(option))

def check_products_in_list_arrangement(option: str):
    return products_wrapper.should(have.attribute("class").value_containing(option))


def switch_to_display_option(option: str):
    return list_mode_option.click() if option == 'list' else grid_mode_option.click()

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

