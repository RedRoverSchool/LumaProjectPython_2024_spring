from selene import browser
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from pages.locators import ErinRecommendLocators as ERL
from data.links import *


class ErinRecommendsPage:
    def __init__(self, browser):
        self.browser = browser

    def visit(self):
        browser.open(ERIN_RECOMMENDS_URL)

    def move_to_erin_page(self):
        s(ERL.HOME_ERIN_BLOCK).click()

    def check_current_url(self):
        return browser.driver.current_url

    def is_header_present(self):
        return s(ERL.PAGE_HEADER).should(be.present)

    def is_element_text_correct(self, element, text):
        return element.should(have.text(text))