from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss
from pages.locators import NavigatorLocators as Nav
from data.links import MEN_PAGE_URL
from data.links import MEN_TOPS_PAGE_URL
from data.links import MEN_BOTTOMS_PAGE_URL


class NavComponent:

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def is_have_text(locator, text):
        s(locator).should(have.text(text))

    @staticmethod
    def goto_men_page():
        s(Nav.NAV_MEN).click()

    @staticmethod
    def find_men_link():
        return s(Nav.NAV_MEN)

    @staticmethod
    def find_men_tops_link():
        return s(Nav.NAV_MEN_TOPS)

    @staticmethod
    def is_clickable(locator, url):
        s(locator).should(be.clickable)
        s(locator).should(have.attribute("href", url))

    @staticmethod
    def verify_sub_men_tops():
        submenu = s(Nav.NAV_MEN_TOPS_SUBMENU)
        submenu.should(be.visible)
        submenus = ss(Nav.NAV_MEN_TOPS_SUBMENU)
        expected_elements = ["Jackets", "Hoodies & Sweatshirts", "Tees", "Tanks"]
        for expected_element in expected_elements:
            submenu_found = False
            for submenu in submenus:
                if submenu.should(have.text(expected_element)):
                    submenu_found = True
                    break
            assert submenu_found, f"Expected submenu '{expected_element}' not found"

    def verify_nav_men(self):
        self.verify_nav(Nav.NAV_MEN, 'Men')
        self.is_clickable(Nav.NAV_MEN, MEN_PAGE_URL)

    def verify_dropdown_menu(self):
        self.verify_nav_men_tops()
        self.verify_nav_men_bottoms()

    def verify_nav_men_tops(self):
        self.verify_nav(Nav.NAV_MEN_TOPS, 'Tops')
        self.is_clickable(Nav.NAV_MEN_TOPS, MEN_TOPS_PAGE_URL)

    def verify_nav_men_bottoms(self):
        self.verify_nav(Nav.NAV_MEN_BOTTOMS, 'Bottoms')
        self.is_clickable(Nav.NAV_MEN_BOTTOMS, MEN_BOTTOMS_PAGE_URL)

    def verify_nav(self, locator, text):
        s(locator).should(be.present)
        s(locator).should(be.visible)
        self.is_have_text(locator, text)
