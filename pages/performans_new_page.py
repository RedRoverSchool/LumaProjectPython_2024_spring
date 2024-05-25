from selene import browser, be, have
from selene import command
from selene.support.shared.jquery_style import s, ss

from pages.locators import PerformanceSportswear

URL_PERFORMANCE = "https://magento.softwaretestingboard.com/collections/performance-new.html"
text_required_field = 'This is a required field.'

product_price = '.price-label'
product_name = '.product-item-link'
product_image = '.product-image-photo'


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


def compare_nr_of_items_and_nr_of_names(count):
    ss(product_name).should(have.size(count))


def compare_nr_of_items_and_nr_of_images(count):
    ss(product_image).should(have.size(count))


def compare_nr_of_items_and_nr_of_prices(count):
    ss(product_price).should(have.size(count))


def click_button_add_to_cart_with_js():
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).perform(command.js.click)


def check_no_success_message():
    s(PerformanceSportswear.SUCCESS_MESSAGE).should(have.no.text(PerformanceSportswear.TEXT_SUCCESS_MESSAGE))


def click_button_add_to_cart_with_hover():
    s(PerformanceSportswear.IMAGE_2).should(be.visible).hover()
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).should(be.clickable).click()


def go_to_product_helios_endurance_tank():
    s(PerformanceSportswear.IMAGE_2).click()


def select_size_xs():
    s('#option-label-size-143-item-166').click()


def select_color_blue():
    s('#option-label-color-93-item-50').click()


def verify_if_color_and_size_were_selected():
    selected = ss('[aria-checked="true"]')
    assert len(selected) == 2


def press_button_add_to_cart():
    s('//*[@id="product-addtocart-button"]/span').click()


def check_msg_no_required_field_color():
    choose_color = s('//*[@id="super_attribute[93]-error"]')
    choose_color.should(have.text(text_required_field))


def check_msg_no_required_field_size():
    choose_size = s('//*[@id="super_attribute[143]-error"]')
    choose_size.should(have.text(text_required_field))


def click_product_review(product_name):
    product_rating = s(f'//*[@title="{product_name}"]/../..')
    product_rating.hover()
    product_rating.s(".rating-result").should(be.visible)
    product_rating.s("a.action.view").should(be.clickable).perform(command.js.click)
