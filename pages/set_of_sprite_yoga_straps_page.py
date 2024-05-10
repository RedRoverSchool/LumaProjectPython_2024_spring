from pages.base_page import BasePage
from selene.support.shared.jquery_style import s
from pages.locators import SetYogaStrapsLocators as SYSL, ProductLocators

class SetYogaStraps(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def add_to_cart_more(self, count):
        s(SYSL.SPRITE_YOGA_STRAP_10_FOOT).click().send_keys(count)
        s(ProductLocators.ADD_TO_CART_BUTTON).click()



