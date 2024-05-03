from selene import browser
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from pages.locators import WhatsNewPageLocators as WNL
from pages.locators import HomeLocators as Url



class WhatsNewPage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(Url.WHAT_NEW_URL)

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))

    def is_header_present(self):
        return s(WNL.HEADER).should(be.present)

    def is_lumas_latest_present(self):
        return s(WNL.LUMAS_LATEST_LIST).should(be.present)

    def get_lumas_latest_items(self):
        return s(WNL.LUMAS_LATEST_ITEMS)

    def check_current_url(self):
        return browser.driver.current_url

    @staticmethod
    def find_button_more():
        return s(WNL.BUTTON_MORE)

    def is_button_present(self):
        return self.find_button_more().should(be.present)

    def is_button_visible(self):
        return self.find_button_more().should(be.visible)

    def is_current_link(self):
        return self.check_current_url() == Url.WHAT_NEW_URL

    def click_button_more(self):
        self.find_button_more().click()

    def scroll_to(self, element):
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @staticmethod
    def click_bras_and_tank_link():
        return s(WNL.BRAS_TANKS).click()

    def click_breathe_easy_tank_item(self):
        return s(WNL.BREATHE_EASY_TANK).click()


    def add_to_cart_button(self):
        return s(WNL.ADD_TO_CART_BUTTON).click()
