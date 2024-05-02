from selene import browser
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from pages.locators import WhatsNewPageLocators as WNL
from data.links import WHATS_NEW_PAGE_LINK
from selenium.webdriver.common.action_chains import ActionChains


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
        return self.check_current_url() == WHATS_NEW_PAGE_LINK

    def click_button_more(self):
        self.find_button_more().click()

    def scroll_to(self, element):
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def move_to(self, product):
        ActionChains(self.browser.driver).move_to_element(product).perform()
