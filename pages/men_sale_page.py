from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from data.links import MEN_SALE_PAGE_URL
from data.page_data import MenSalePageData as data
from pages.components.nav_wigdet import NavComponent
from pages.locators import BaseLocators as Header, MenSaleLocators as ms_locators


class MenSalePage:

    title_page = s(ms_locators.PAGE_TITLE)

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

    @staticmethod
    def is_number_of_items_in_toolbar_corresponds_to_amount_in_list():
        number = str(len(ss(ms_locators.LIST_ITEM)))
        s(ms_locators.TOOLBAR_NUMBER).should(have.text(number))
