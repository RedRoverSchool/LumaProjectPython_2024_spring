from selene import query
from selene.support.conditions import be
from selene.support.shared.jquery_style import s, ss
from pages.base_page import BasePage
from pages.locators import ProductLocators as PL, HomeLocators as HL


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