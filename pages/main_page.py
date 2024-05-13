from selene import query
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from data.links import MAIN_PAGE_LINK
from data.page_data import MainPageData
from pages.base_page import BasePage
from pages.locators import BaseLocators as BL, HomeLocators, ProductItemLocators
from pages.locators import ErinRecommendLocators as ERL
from pages.locators import NavigatorLocators as Nav


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open_page(self):
        self.visit(MAIN_PAGE_LINK)

    @property
    def privacy_cookie_policy_link(self):
        return s(BL.PRIVACY_COOKIE_POLICY_LOCATOR)

    @property
    def new_luma_yoga_collection_block(self):
        return s(BL.NEW_LUMA_YOGA_COLLECTION_BLOCK_LOCATOR)

    @property
    def new_luma_yoga_collection_block_info_text(self):
        return s(BL.NEW_LUMA_YOGA_COLLECTION_BLOCK_INFO_TEXT_LOCATOR)

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

    def is_loaded(self):
        assert self.get_current_url() == MAIN_PAGE_LINK, MainPageData.error_message

    def is_erin_block_present(self):
        return s(ERL.HOME_ERIN_BLOCK).should(be.present)

    @staticmethod
    def handle_cookies_popup():
        if ss(HomeLocators.COOKIES_MSG):
            s(HomeLocators.CONSENT_COOKIES_BTN).click()

            
    @staticmethod
    def open_mini_cart():
        s(HomeLocators.CART_ICON).click()


    @staticmethod
    def check_product_qty_inside_minicart(value):
        s(HomeLocators.MINICART_PRODUCT_QTY).should(have.attribute('data-item-qty', value))


    @staticmethod
    def clear_minicart():
        if s(HomeLocators.CART_COUNTER).get(query.text) != "0":
            s(HomeLocators.CART_ICON).click()
            s(HomeLocators.MINICART_DELETE_BUTTONS).wait_until(be.visible)
            delete_btns = ss(HomeLocators.MINICART_DELETE_BUTTONS)
            if len(delete_btns) > 1:
                for btn in delete_btns:
                    btn.click()
                    s(HomeLocators.DELETE_ITEM_CONFIRM_OK).wait_until(be.visible)
                    s(HomeLocators.DELETE_ITEM_CONFIRM_OK).click()
            elif len(delete_btns) == 1:
                s(HomeLocators.MINICART_DELETE_BUTTONS).click()
                s(HomeLocators.DELETE_ITEM_CONFIRM_OK).wait_until(be.visible)
                s(HomeLocators.DELETE_ITEM_CONFIRM_OK).click()
            s(HomeLocators.MINICART_CLOSE).click()


    @staticmethod
    def close_minicart():
        s(HomeLocators.MINICART_CLOSE).click()


    def add_item_to_cart(self, size, color, add_to_cart_button):
        s(size).click()
        s(color).click()
        s(add_to_cart_button).click()

