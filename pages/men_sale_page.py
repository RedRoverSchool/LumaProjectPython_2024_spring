from pages.components.nav_wigdet import NavComponent
from data.links import MEN_SALE_PAGE_URL
from selene.support.conditions import be
from selene.support.shared.jquery_style import s, ss
from pages.locators import BaseLocators as Header


class MenSalePage:
    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent(browser)

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
