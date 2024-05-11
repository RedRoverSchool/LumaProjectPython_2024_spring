from pages.components.nav_wigdet import NavComponent
from data.links import MEN_SALE_PAGE_URL
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import BaseLocators as Header, MenSaleLocators as ms_locators
from data.page_data import MenSalePageData as data


class MenSalePage:
    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent()

    def open_page(self):
        self.browser.open(MEN_SALE_PAGE_URL)

    @staticmethod
    def get_bread_crumbs():
        elements = ss(Header.BREADCRUMBS_LIST)
        breadcrumbs_titles = []
        for i in elements:
            breadcrumbs_titles.append(i.locate().text)
        return breadcrumbs_titles

    @staticmethod
    def are_bread_crumbs_present():
        return s(Header.BREADCRUMBS).should(be.present)

    @staticmethod
    def is_page_title_present():
        return s(ms_locators.PAGE_TITLE).should(be.present)

    @staticmethod
    def is_page_title_correct():
        return s(ms_locators.PAGE_TITLE).should(have.text(data.page_title))
