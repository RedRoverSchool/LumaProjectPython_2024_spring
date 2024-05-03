from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s
from data.links import MAIN_PAGE_LINK
from pages.locators import BaseLocators as BL
from pages.locators import NavigatorLocators as Nav
from pages.locators import HomeLocators as HL
from pages.components.nav_wigdet import NavComponent


class MainPage:

    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent(browser)

    def open_page(self):
        self.browser.open(MAIN_PAGE_LINK)

    @property
    def privacy_cookie_policy_link(self):
        return s(BL.PRIVACY_COOKIE_POLICY_LOCATOR)

    def scroll_to_privacy_cookie_policy_link(self):
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", self.privacy_cookie_policy_link())

    def click_privacy_cookie_policy_link(self):
        self.privacy_cookie_policy_link.click()

    def is_menu_present(self):
        return s(Nav.NAV_MENU).should(be.present)

    def is_whats_new_link_present(self):
        return s(Nav.NAV_NEW).should(be.present)

    def find_whats_new_link(self):
        return s(Nav.NAV_NEW)

    def get_current_url(self):
        return self.browser.driver.current_url

    def is_loaded(self):
        assert self.get_current_url() == MAIN_PAGE_LINK, "Home page did not load successfully"

    def find_cart_icon(self):
        return s(HL.CART_ICON)

    def is_find_cart_icon_present(self):
        return self.find_cart_icon().should(be.present)

    def find_minicart(self):
        return s(HL.MINICART)

    def is_minicart_present(self):
        return self.find_minicart().should(be.present)

    def is_minicart_visible(self):
        return self.find_minicart().should(be.visible)

    def find_minicart_view(self):
        return s(HL.MINICART_VIEW)

    def is_minicart_view_present(self):
        return self.find_minicart_view().should(be.present)

    def is_minicart_view_visible(self):
        return self.find_minicart_view().should(be.visible)

    def is_minicart_have_link(self):
        return self.find_minicart_view().should(have.attribute('href').value('https://magento.softwaretestingboard.com/checkout/cart/'))
