from selene import Element
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss
from pages.locators import NavigatorLocators as Nav
from pages.locators import BaseLocators as Base
from data.links import MenUrls, MEN_PAGE_URL


class NavComponent:

    @staticmethod
    def is_have_text(locator, value):
        locator.should(have.text(value))

    def goto_men_page(self):
        self.find_men_link().click()

    @staticmethod
    def find_men_link():
        return s(Nav.NAV_MEN)

    @staticmethod
    def find_men_tops_link():
        return s(Nav.NAV_MEN_TOPS)

    @staticmethod
    def find_men_bottoms_link():
        return s(Nav.NAV_MEN_BOTTOMS)

    @staticmethod
    def click_to(locator):
        s("//li[contains(@class, 'nav-3')]/a[@role='menuitem']/span[text()='{}']".format(locator)).click()

    @staticmethod
    def is_clickable(locator: Element, url: str):
        locator.should(be.clickable)
        locator.should(have.attribute("href").value(url))

    @staticmethod
    def is_have_header(header):
        s(Base.PAGE_HEADER).should(have.text(header))

    @staticmethod
    def verify_sub_men_tops():
        submenus = s(Nav.NAV_MEN_SUBMENU)
        submenus.should(be.visible)
        for expected_element in list(MenUrls.men_top_urls.keys()):
            submenus.should(have.text(expected_element))

    @staticmethod
    def verify_sub_men_bottoms():
        submenus = s(Nav.NAV_MEN_BOTTOMS_SUBMENU)
        submenus.should(be.visible)
        for expected_element in list(MenUrls.men_bottoms_urls.keys()):
            submenus.should(have.text(expected_element))

    def verify_dropdown_menu(self):
        self.verify_nav_mens_tops()
        self.verify_nav_mens_bottoms()

    def verify_nav_men(self):
        self.verify_nav(s(Nav.NAV_MEN), 'Men')
        self.is_clickable(s(Nav.NAV_MEN), MEN_PAGE_URL)

    def verify_nav_mens_tops(self):
        self.verify_nav(s(Nav.NAV_MEN_TOPS), 'Tops')
        self.is_clickable(s(Nav.NAV_MEN_TOPS), MenUrls.men_sub_urls['Tops'])

    def verify_nav_mens_bottoms(self):
        self.verify_nav_mens(Nav.NAV_MEN_BOTTOMS, 'Bottoms')
        self.is_clickable(s(Nav.NAV_MEN_BOTTOMS), MenUrls.men_sub_urls['Bottoms'])

    def verify_nav_mens(self, locator, nav):
        self.verify_nav(s(locator), nav)
        self.is_clickable(s(locator), MenUrls.men_sub_urls[nav])

    def verify_nav(self, locator: Element, title: str):
        locator.should(be.present)
        locator.should(be.visible)
        self.is_have_text(locator, title)

    def verify_sub_men_tops_href_elements(self):
        for i, element in enumerate(ss(Nav.NAV_MEN_TOPS_SUBMENU_HREFS)):
            self.verify_nav(element, list(MenUrls.men_top_urls.keys())[i])
            self.is_clickable(element, list(MenUrls.men_top_urls.values())[i])

    def verify_sub_men_bottoms_href_elements(self):
        for i, element in enumerate(ss(Nav.NAV_MEN_BOTTOMS_SUBMENU_HREFS)):
            self.verify_nav(element, list(MenUrls.men_bottoms_urls.keys())[i])
            self.is_clickable(element, list(MenUrls.men_bottoms_urls.values())[i])
