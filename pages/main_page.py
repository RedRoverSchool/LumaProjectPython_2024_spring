from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s
from data.links import MAIN_PAGE_LINK
from pages.locators import BaseLocators as BL
from pages.locators import NavigatorLocators as Nav
from pages.locators import HomeLocators as HL


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(MAIN_PAGE_LINK)

    @property
    def privacy_cookie_policy_link(self):
        return s(BL.PRIVACY_COOKIE_POLICY_LOCATOR)

    def scroll_to_privacy_cookie_policy_link(self):
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", self.privacy_cookie_policy_link())

    def is_menu_present(self):
        return s(Nav.NAV_MENU).should(be.present)

    def is_whats_new_link_present(self):
        return s(Nav.NAV_NEW).should(be.present)

    def find_whats_new_link(self):
        return s(Nav.NAV_NEW)


    def find_men_link(self):
        return s(Nav.NAV_MEN)

    def is_men_present(self):
        return self.find_men_link().should(be.present)

    def is_men_visible(self):
        return self.find_men_link().should(be.visible)    
    
    def is_men_link_present(self):
        return self.find_men_link().should(be.present)

    def is_men_have_text(self):
        return self.find_men_link().should(have.text('Men'))


    def find_men_tops_link(self):
        return s(Nav.NAV_MEN_TOPS)

    def is_men_tops_present(self):
        return self.find_men_tops_link().should(be.present)

    def is_men_tops_visible(self):
        return self.find_men_tops_link().should(be.visible)    
    
    def is_men_tops_link_present(self):
        return self.find_men_tops_link().should(be.present)

    def is_men_tops_have_text(self):
        return self.find_men_tops_link().should(have.text('Tops'))


    def find_men_bottoms_link(self):
        return s(Nav.NAV_MEN_BOTTOMS)

    def is_men_bottoms_present(self):
        return self.find_men_bottoms_link().should(be.present)

    def is_men_bottoms_visible(self):
        return self.find_men_bottoms_link().should(be.visible)    
    
    def is_men_bottoms_link_present(self):
        return self.find_men_bottoms_link().should(be.present)

    def is_men_bottoms_have_text(self):
        return self.find_men_bottoms_link().should(have.text('Bottoms'))

    def find_cart_icon(self):
        return s(HL.CART_ICON)

    def find_minicart(self):
        return s(HL.MINICART)
    def is_minicart_present(self):
        return self.find_minicart().should(be.present)

    def is_minicart_visible(self):
        return self.find_minicart().should(be.visible)

    def find_minicart_view(self):
        return s(HL.MINICART_VIEW)

    def is_minicart_have_text(self):
        return self.find_minicart_view().should(have.text('View and Edit Cart'))