from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

import data.links
from data.links import MAIN_PAGE_LINK
from data.page_data import MainPageData
from pages.base_page import BasePage
from selene.support.shared import browser
from pages import cart_page
from pages.locators import BaseLocators as BL, HomeLocators, CreateAccountLocators
from pages.locators import ErinRecommendLocators as ERL
from pages.locators import NavigatorLocators as Nav, ProductLocators as PL
from pages.locators import FooterLocators as FL
from pages.locators import NotesLocators as Nl


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    whats_new = s(Nav.NAV_NEW)

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
        s(Nav.NAV_MENU).should(be.present)

    def is_whats_new_link_present(self):
        self.whats_new.should(be.present)

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
        s(HomeLocators.MINICART_PRODUCT_QTY).should(have.attribute('data-item-qty').value(value))

    def add_item_to_cart(self, size, color, add_to_cart_button):
        s(size).click()
        s(color).click()
        s(add_to_cart_button).click()

    def add_to_cart_from_main_page(self):
        s(PL.ARGUS_All_WEATHER_TANK_SIZE).click()
        s(PL.ARGUS_All_WEATHER_TANK_COLOR).click()
        s(PL.ARGUS_All_WEATHER_TANK_ADD_TO_CARD).click()

    def go_to_mini_cart(self):
        s(PL.MINI_BASKET_WINDOW).should(be.clickable).click()

    def go_to_checkout_cart(self):
        s(PL.VIEW_AND_EDIT_CART_LINK).click()
        return cart_page

    def click_cart_icon(self):
        self.cart_icon.click()

    def verify_counter(self, count):
        self.mini_cart_counter.should(be.visible).should(have.text(count))

    def should_be_clickable_create_account(self):
        s(CreateAccountLocators.CREATE_AN_ACCOUNT_LINK).should(be.clickable)

    def hover_down_footer(self):
        s(FL.FOOTER_LINKS).hover()

    def click_notes_link(self):
        s(Nl.NOTES).click()

    def accept_cookies(self):
        window_handles = browser.driver.window_handles
        browser.switch_to.window(window_handles[-1])
        browser.with_(timeout=10).element(Nl.COOKIE_MSG).should(be.visible)
        s(Nl.COOKIE_ACCEPT_BTN).click()

    def assert_notes_page_title(self):
        assert s(Nl.NOTES_PAGE_TITLE).should(have.text('Notes')), "wrong title"

    def assert_notes_page_url(self):
        assert data.links.BASE_URL != data.links.NOTES_PAGE_URL, "Not redirected"
