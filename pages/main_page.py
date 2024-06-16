from selene import have, be, Element, browser
from selene.core import command, query
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from data.links import SOFTWARE_TESTING_BOARD
from pages import cart
from pages.components import mini_card
from pages.components import nav
from pages.locators import FooterLocators
from pages import privacy_policy_page

main_page_link = 'https://magento.softwaretestingboard.com/'
create_an_account = "(//a[.='Create an Account'])[1]"
argus_all_weather_tank_size = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="M"]'
argus_all_weather_tank_color = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="Gray"]'
argus_all_weather_tank_add_to_card = '//*[@title="Argus All-Weather Tank"]/../..//*[@title="Add to Cart"]'
mini_basket_window = '[class="action showcart"]'
view_and_edit_cart_link = "//*[text()='View and Edit Cart']"
notes_link = s('//footer//a[contains(text(), "Notes")]')
item_size = s('[option-label="XS"]')
color_item = s('[option-label="Orange"]')
btn_add_to_cart = s('form[data-product-sku="WS12"] button')
privacy_cookie_policy_link = s("//a[contains(@href, 'privacy-policy-cookie')]")
sign_in_link = s('(//li[@class="authorization-link"])[1]')
page_title = s("h1")
footer_links = ss('//footer[@class="page-footer"]//li')


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

    @staticmethod
    def menu_should_be_present():
        s('#ui-id-2').should(be.present)

    def whats_new_link_should_be_present(self):
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

    def add_to_cart_from_main_page(self):
        s(argus_all_weather_tank_size).click()
        s(argus_all_weather_tank_color).click()
        s(argus_all_weather_tank_add_to_card).click()

    def go_to_mini_cart(self):
        s(mini_basket_window).should(be.clickable).click()

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

    def scrol_to_footer(self):
        s(FooterLocators.NOTES).perform(command.js.scroll_into_view)

    def move_to_element(self):
        s(FooterLocators.NOTES).hover()

    def is_visible_notes(self):
        s(FooterLocators.NOTES).should(be.visible)

    def is_clicable_notes(self):
        s(FooterLocators.NOTES).should(be.clickable)

    def click_notes(self):
        s(FooterLocators.NOTES).click()

    def magento_text_check(self, text):
        s(FooterLocators.MAGENTO).should(have.text(text))

    def check_for_redirection_to_magento_store_notes(self):
        assert self.get_current_url() == SOFTWARE_TESTING_BOARD


def open_page():
    browser.open(main_page_link)


def add_item_to_cart():
    item_size.click()
    color_item.click()
    btn_add_to_cart.click()


def scroll_to_privacy_cookie_policy_link():
    privacy_cookie_policy_link.perform(command.js.scroll_into_view)


def link_name_is_visible(text):
    privacy_cookie_policy_link.should(be.visible)
    privacy_cookie_policy_link.should(have.text(text))


def click_privacy_cookie_policy_link():
    privacy_cookie_policy_link.click()


def should_be_redirected_to(text):
    privacy_policy_page.is_current_url()
    privacy_policy_page.is_header_has_text(text)


def click_on_create_account_link():
    s(create_an_account).should(be.visible).click()


def click_on_sign_in_link():
    sign_in_link.should(be.visible).click()


def check_header(header):
    return page_title.should(have.text(header))
