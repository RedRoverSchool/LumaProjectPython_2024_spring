from selene import browser, by, be, have
from selene.support.shared.jquery_style import s
from pages.locators import FooterLocators
from data.links import base_url
from selene import command


class Footer:

    def __init__(self, browser):
        self.browser = browser

    def open_base_page(self):
        self.browser.open(base_url)

    def scrol_to_footer(self):
        s(FooterLocators.NOTES).perform(command.js.scroll_into_view)

    def move_to_element(self):
        s(FooterLocators.NOTES).hover()

    def is_visible_Notes(self):
        s(FooterLocators.NOTES).should(be.visible)

    def is_clicable_Notes(self):
        s(FooterLocators.NOTES).should(be.clickable)
