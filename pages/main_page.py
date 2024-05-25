from selene import have, be, Element
from selene.core import command, query
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss

from pages import cart
from pages.components import mini_card
from pages.components import nav

main_page_link = 'https://magento.softwaretestingboard.com/'
create_an_account = "(//a[.='Create an Account'])[1]"
argus_all_weather_tank_size = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="M"]'
argus_all_weather_tank_color = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="Gray"]'
argus_all_weather_tank_add_to_card = '//*[@title="Argus All-Weather Tank"]/../..//*[@title="Add to Cart"]'
MINI_BASKET_WINDOW = '[class="action showcart"]'
view_and_edit_cart_link = "//*[text()='View and Edit Cart']"


class MainPage:
    whats_new = s('#ui-id-3')
    mini_cart = s('#ui-id-1')
    cart_icon = s('a.showcart')
    message = s(".success.message")
    products = ss(".product-item-info")
    mini_cart_counter = s('.counter-label')
    products_grid = s(".products-grid.grid")
    privacy_cookie_policy_link = s("//a[contains(@href, 'privacy-policy-cookie')]")
    new_luma_yoga_collection_block = s("//a[contains(@class,'home-main')]/span")
    new_luma_yoga_collection_block_info_text = s("//a[contains(@class,'home-main')]//span[@class='info']")

    def __init__(self, browser):
        self.browser = browser
        self.nav = nav
        self.mini_card = mini_card

    def visit(self, url):
        self.browser.open(url)

    def assert_text_of_element(self, locator, expected_text):
        s(locator).should(have.text(expected_text))

    def assert_visible_of_element(self, locator):
        s(locator).should(be.visible)

    def assert_present_of_element(self, locator):
        s(locator).should(be.present)

    def get_current_url(self):
        return self.browser.driver.current_url

    def is_cart_icon_present(self):
        self.cart_icon.should(be.present)

    def is_cart_icon_clickable(self):
        return self.cart_icon.should(be.clickable)

    def is_counter_number_present(self):
        self.mini_cart_counter.should(be.present)

    def is_counter_number_visible(self):
        self.mini_cart_counter.should(be.visible)

    def add_product_to_cart(self, product: Element):
        product.hover()
        self.set_color(product)
        self.set_size(product)
        product.s("button.action.tocart.primary").should(be.visible).should(be.clickable).click()
        self.is_visible_success_message()
        self.cart_icon.should(be.clickable).hover().click()

    def goto_card_page(self):
        self.is_cart_icon_present()
        self.cart_icon.hover().click()
        self.mini_card.is_mini_cart_visible()
        self.mini_card.click_mini_cart()

    def scroll_to_hot_sellers(self):
        self.scroll_to(self.products_grid)

    def get_subtotal(self):
        self.is_cart_icon_clickable().hover().click()
        amount_price = s(".amount.price-container").s('.price-wrapper')
        price = amount_price.get(query.attribute('innerText'))
        return float(price.replace('$', ''))

    def set_size(self, product: Element):
        self.choose_first(product.ss(".swatch-attribute.size .swatch-option"))

    def set_color(self, product: Element):
        self.choose_first(product.ss(".swatch-attribute.color .swatch-option"))

    def choose_first(self, param):
        if len(param) > 0:
            param.first.click()

    def is_visible_success_message(self):
        self.message.should(be.visible)
        self.message.should(have.text('You added')).should(have.text('to your shopping cart'))

    @staticmethod
    def scroll_to(element: Element):
        element.perform(command.js.scroll_into_view)

    @staticmethod
    def get_text(selector):
        return s(selector).get(query.attribute('innerText'))

    @staticmethod
    def click_on_link(locator):
        s(locator).click()

    def open_page(self):
        self.visit(main_page_link)

    def scroll_to_privacy_cookie_policy_link(self):
        self.browser.driver.execute_script("arguments[0].scrollIntoView(true);", self.privacy_cookie_policy_link())

    def click_privacy_cookie_policy_link(self):
        self.privacy_cookie_policy_link.click()

    def is_menu_present(self):
        s('#ui-id-2').should(be.present)

    def is_whats_new_link_present(self):
        self.whats_new.should(be.present)

    def is_loaded(self):
        assert self.get_current_url() == main_page_link

    @staticmethod
    def is_erin_block_present():
        return s("//a[@class='block-promo home-erin']").should(be.present)

    @staticmethod
    def handle_cookies_popup():
        if ss('//h1[@class="fc-dialog-headline"]'):
            s('(//p[@class="fc-button-label"])[1]').click()

    @staticmethod
    def open_mini_cart():
        s('a.showcart').click()

    @staticmethod
    def check_product_qty_inside_minicart(value):
        s('input[class="item-qty cart-item-qty"]').should(have.attribute('data-item-qty').value(value))

    def add_item_to_cart(self, size, color, add_to_cart_button):
        s(size).click()
        s(color).click()
        s(add_to_cart_button).click()

    def add_to_cart_from_main_page(self):
        s(argus_all_weather_tank_size).click()
        s(argus_all_weather_tank_color).click()
        s(argus_all_weather_tank_add_to_card).click()

    def go_to_mini_cart(self):
        s(MINI_BASKET_WINDOW).should(be.clickable).click()

    def go_to_checkout_cart(self):
        s(view_and_edit_cart_link).click()
        return cart

    def click_cart_icon(self):
        self.cart_icon.click()

    def verify_counter(self, count):
        self.mini_cart_counter.should(be.visible).should(have.text(count))

    @staticmethod
    def should_be_clickable_create_account():
        s(create_an_account).should(be.clickable)

    @staticmethod
    def has_create_account_text():
        s(create_an_account).should(have.text('Create an Account'))
