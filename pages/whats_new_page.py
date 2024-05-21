from selene import browser, command, Element, query
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support.color import Color

from data.links import WHATS_NEW_PAGE_LINK, LAYLA_TEE_URL
from data.page_data import WishListData as Data
from pages.base_page import BasePage
from pages.locators import ProductItemLocators as Product, BaseLocators
from pages.locators import WhatsNewPageLocators as WNL


class WhatsNewPage(BasePage):

    def open_page(self):
        self.visit(WHATS_NEW_PAGE_LINK)

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def is_header_present(self):
        return s(WNL.HEADER).should(be.present)

    def is_lumas_latest_present(self):
        return s(WNL.LUMAS_LATEST_LIST).should(be.present)

    def get_lumas_latest_items(self):
        return ss(WNL.LUMAS_LATEST_ITEMS)

    @staticmethod
    def find_button_new_yoga():
        return s(WNL.BUTTON_MORE)

    def is_button_present(self):
        return self.find_button_new_yoga().should(be.present)

    def is_button_visible(self):
        return self.find_button_new_yoga().should(be.visible)

    def is_current_link(self):
        return self.get_current_url() == WHATS_NEW_PAGE_LINK

    def click_button_shop_new_yoga(self):
        self.find_button_new_yoga().click()

    def add_items_to_wish_list(self, size):
        self.click_button_shop_new_yoga()
        products = ss(Product.ITEM_INFO)
        for i in range(size):
            self.scroll_to(products[i])
            products[i].hover()
            products[i].s(Product.WISH_LIST).click()
            s(BaseLocators.SUCCESS_MESSAGE).should(have.text(Data.add_wish_list_message))
            self.browser.driver.back()

    def add_item_to_wish_list(self):
        self.open_page()
        self.click_button_shop_new_yoga()
        product = s(Product.ITEM_INFO)
        self.scroll_to(product)
        product.hover()
        s(Product.WISH_LIST).click()

    def get_number_of_lumas_latest(self):
        collection = self.get_lumas_latest_items()
        return len(collection)

    @staticmethod
    def get_collection_lumas_latest_items():
        return ss(WNL.LUMAS_LATEST_IMAGES)

    def are_men_and_women_items_present(self):
        collection = self.get_collection_lumas_latest_items()
        m = 0
        w = 0
        for item in collection:
            if item.matching(have.attribute("src").value_containing('/m/')):
                m += 1
            elif item.matching(have.attribute("src").value_containing('/w/')):
                w += 1
        return True if (m > 0 and w > 0) and m + w == 4 else False

    def is_yoga_link_visible(self):
        return s(WNL.NEW_YOGA_LINK).should(be.visible)

    def new_yoga_link_click(self):
        return s(WNL.NEW_YOGA_LINK).click()

    def open_eco_collection_url(self):
        self.open_page()
        s(BaseLocators.ECO_COLLECTION_NAME).click()

    def click_layla_tee_name(self):
        s(Product.LAYLA_TEE_PRODUCT_NAME).click()

    def check_redirection_to_layla_tee_pdp(self):
        return self.get_current_url() == LAYLA_TEE_URL

    def layla_tee_title_is_displayed(self):
        return s(Product.LAYLA_TEE_TITLE).should(be.visible)

    def click_layla_tee_img(self):
        s(Product.LAYLA_TEE_IMG).click()

    @staticmethod
    def click_bras_and_tank_link():
        return s(WNL.BRAS_TANKS).click()

    def click_breathe_easy_tank_item(self):
        return s(WNL.BREATHE_EASY_TANK).click()

    def add_to_cart_button(self):
        return s(WNL.ADD_TO_CART_BUTTON).click()

    def add_to_compare_button(self):
        return s(WNL.ADD_TO_COMPARE).click()

    def add_to_wish_list_button(self):
        return s(WNL.ADD_TO_WISH_LIST_BUTTON).click()

    def change_layla_tee_color(self, color):
        layla_tee = s(WNL.LAYLA_TEE_NAME)
        layla_tee.hover()
        s(f"//li[2]//div[@option-label='{color}']").click()
        layla_tee.hover()

    def is_color_selected(self, color_name, color_hex):
        color_selector = f"//li[2]//div[@option-label='{color_name}']"
        s(color_selector).should(have.css_property('outline-color').value(Color.from_string(color_hex).rgba))

    def is_layla_tee_img_color_correct(self, color):
        img_url = f"https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/s/ws04-{color}_main_1.jpg"
        s(WNL.LAYLA_TEE_IMG).wait_until(have.attribute('src').value(img_url))
        color_img_name = f'ws04-{color}_main_1.jpg'
        img_src_name = s(WNL.LAYLA_TEE_IMG).get(query.attribute('src'))
        assert color_img_name in img_src_name

    def check_buttons_visibility_on_product_card(self):
        for i in range(1, 6):
            s(f"//li[{i}]/div/div").hover()
            s(f'//li[{i}]//button[@class="action tocart primary"]').should(be.visible)
            s(f'//li[{i}]//a[@class="action towishlist"]').should(be.visible)
            s(f'//li[{i}]//a[@class="action tocompare"]').should(be.visible)
