from selene import query, have
from selene.support.conditions import be
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support.color import Color

from pages.base_page import BasePage
from pages.locators import ProductLocators as PL, HomeLocators as HL, WishListLocators as WLL


class ProductPage(BasePage):

    def open_radiant_tee_page(self):
        self.visit(PL.RADIANT_TEE_URL)

    def is_radiant_tee_title_visible(self):
        self.assert_visible_of_element(PL.RADIANT_TEE_TITLE)

    def is_radiant_tee_img_visible(self):
        self.assert_visible_of_element(PL.RADIANT_TEE_IMG)

    def is_radiant_tee_price_is_visible(self):
        self.assert_visible_of_element(PL.RADIANT_TEE_PRICE)

    def is_radiant_tee_name_visible_in_minicart(self):
        self.assert_visible_of_element(HL.MINICART_RADIANT_TEE_NAME)

    def is_product_details_visible(self):
        assert s(PL.PRODUCT_DETAILS_TEXT).get(query.text) != 0

    def click_more_information_tab(self):
        s(PL.MORE_INFO_TAB).should(be.clickable).click()

    def is_more_information_visible(self):
        text = []
        for n in range(1, 5):
            text.append(s(f'//tbody/tr[{n}]/td').get(query.text))
        assert text != []

    def click_reviews_tab(self):
        self.click_on_link(PL.REVIEWS_TAB)

    def is_reviews_content_visible(self):
        s(PL.REVIEWS_CONTENT).should(be.visible)

    @staticmethod
    def add_product_to_wishlist():
        s(PL.ADD_TO_WISHLIST_LINK).click()

    @staticmethod
    def is_success_message_adding_to_wishlist_visible():
        s(WLL.SUCCESS_MESSAGE).should(have.text('has been added to your Wish List.'))

    @staticmethod
    def is_product_title_visible_in_wishlist(title):
        s(f'a.product-item-link[title="{title}"]').should(be.visible)
        
    @staticmethod
    def select_size(size):
        s(f'[option-label="{size}"]').click()
        s(PL.SIZE_INDICATOR).should(be.visible).hover()

    @staticmethod
    def is_size_selected(size, color_hex):
        size_selector = s(f'[option-label={size}]')
        size_selector.should(have.css_property('outline-color').value(Color.from_string(color_hex).rgba))
        size_selector.should(have.attribute('aria-checked').value('true'))

    @staticmethod
    def is_size_indicator_correct(size):
        s(PL.SIZE_INDICATOR).should(have.text(size))
