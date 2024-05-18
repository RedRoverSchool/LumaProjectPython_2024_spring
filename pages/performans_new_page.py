from selene import browser, be, have, command, query
from selene import browser, be, have, Element
from selene.support.shared.jquery_style import s, ss
from pages.locators import BaseLocators, PerformanceSportswear, ProductLocators

URL_PERFORMANCE = "https://magento.softwaretestingboard.com/collections/performance-new.html"

def visit():
    browser.open(URL_PERFORMANCE)


def items_count():
    return len(ss('.product-item-info'))


def check_buttons():
    for product_card in ss('.product-item'):
        product_card.hover()
        product_card.s(".actions-primary").should(be.visible)
        product_card.s(".actions-secondary").should(be.visible)
        product_card.s(".action.tocompare").should(be.visible)


def compare_nr_of_items_and_nr_of_names(items_count):
    ss(BaseLocators.PRODUCT_NAME).should(have.size(items_count))


def compare_nr_of_items_and_nr_of_images(items_count):
    ss(BaseLocators.PRODUCT_IMAGE).should(have.size(items_count))


def compare_nr_of_items_and_nr_of_prices(items_count):
    ss(BaseLocators.PRODUCT_PRICE).should(have.size(items_count))


def click_button_add_to_cart_with_js():
    # кликнуть невидимую кнопку - она за пределами экрана и/или не отрисована
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).perform(command.js.click)


def check_no_success_message():
    s(PerformanceSportswear.SUCCESS_MESSAGE).should(have.no.text(PerformanceSportswear.TEXT_SUCCESS_MESSAGE))


def click_button_add_to_cart_with_hover():
    s(PerformanceSportswear.IMAGE_2).should(be.visible).hover()
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).should(be.clickable).click()


def go_to_product_helios_endurance_tank():
    s(PerformanceSportswear.IMAGE_2).click()


def select_size_XS():
    s(ProductLocators.SIZE_XS).click()

def select_color_blue():
    s(ProductLocators.COLOR_BLUE).click()


def verify_if_color_and_size_were_selected():
    selected = ss('[aria-checked="true"]')
    assert len(selected) == 2


def press_button_add_to_cart():
    s(ProductLocators.ADD_TO_CART_BUTTON).click()


def check_msg_no_required_field_color():
    choose_color = s(ProductLocators.SHOULD_CHOOSE_COLOR)
    choose_color.should(have.text(ProductLocators.TEXT_REQUIRED_FIELD))


def check_msg_no_required_field_size():
    choose_size = s(ProductLocators.SHOULD_CHOOSE_SIZE)
    choose_size.should(have.text(ProductLocators.TEXT_REQUIRED_FIELD))

