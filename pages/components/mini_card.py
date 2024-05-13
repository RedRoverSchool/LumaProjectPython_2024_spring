from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from pages.locators import HomeLocators as Home


class MiniCard:

    def find_minicart(self):
        return s(Home.MINICART)

    def is_minicart_present(self):
        return self.find_minicart().should(be.present)

    def is_minicart_visible(self):
        return self.find_minicart().should(be.visible)

    @staticmethod
    def find_minicart_view():
        return s(Home.MINICART_VIEW)

    @property
    def is_minicart_view_present(self):
        return self.find_minicart_view().should(be.present)

    def is_minicart_view_enable(self):
        return self.find_minicart_view().should(be.enabled)

    def is_minicart_view_visible(self):
        return self.find_minicart_view().should(be.visible)

    def is_minicart_have_link(self):
        return self.find_minicart_view().should(
            have.attribute('href').value('https://magento.softwaretestingboard.com/checkout/cart/'))