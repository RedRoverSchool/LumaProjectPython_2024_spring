from selene import browser, command, Element
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss

from data.links import WHATS_NEW_PAGE_LINK
from data.page_data import WishListData as Data
from pages.locators import ProductItemLocators as Product
from pages.locators import WishListLocators as WishList
from pages.locators import WhatsNewPageLocators as WNL


class WhatsNewPage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(WHATS_NEW_PAGE_LINK)

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def is_header_present(self):
        return s(WNL.HEADER).should(be.present)

    def is_lumas_latest_present(self):
        return s(WNL.LUMAS_LATEST_LIST).should(be.present)

    def get_lumas_latest_items(self):
        return ss(WNL.LUMAS_LATEST_ITEMS)

    def check_current_url(self):
        return browser.driver.current_url

    @staticmethod
    def find_button_new_yoga():
        return s(WNL.BUTTON_MORE)

    def is_button_present(self):
        return self.find_button_new_yoga().should(be.present)

    def is_button_visible(self):
        return self.find_button_new_yoga().should(be.visible)

    def is_current_link(self):
        return self.check_current_url() == WHATS_NEW_PAGE_LINK

    def click_button_shop_new_yoga(self):
        self.find_button_new_yoga().click()

    @staticmethod
    def scroll_to(element: Element):
        element.perform(command.js.scroll_into_view)

    def add_items_to_wish_list(self, size):
        self.click_button_shop_new_yoga()
        products = ss(Product.ITEM_INFO)
        for i in range(size):
            self.scroll_to(products[i])
            products[i].hover()
            products[i].s(Product.WISH_LIST).click()
            s(WishList.SUCCESS_MESSAGE).should(have.text(Data.add_wish_list_message))
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
