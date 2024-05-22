from selene import have, browser, query
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from selenium.webdriver.support.color import Color

product_qty = s('#qty')
add_to_cart_button = s('#product-addtocart-button')
success_message = s(".success.message")
product_title = s('span[data-ui-id="page-title-wrapper"]')
product_price = s('//div[@class="product-info-price"]//span[@data-price-type="finalPrice"]')
product_img = s('//div[1]/div[3]/div[1]/img[@class="fotorama__img"]')
details = s('div.product.attribute.description div p')
more_info_tab = s('#tab-label-additional-title')
size_indicator = s('.swatch-attribute.size span.swatch-attribute-selected-option')
reviews_block = s('#customer-reviews div.block-title strong')
product_name_in_reviews = s('.legend.review-legend strong')


def open(name):
    browser.open(f'https://magento.softwaretestingboard.com/{name}.html')


def add_to_cart_with_qty(size, color, qty):
    s(f'[option-label={size}]').click()
    s(f'[option-label={color}]').click()
    product_qty.click() \
        .clear() \
        .type(qty)
    add_to_cart_button.click()
    success_message.should(have.text('You added')).should(have.text('to your shopping cart'))


def title_should_have_text(text):
    product_title.should(have.text(text))


def price_should_be_equal(price):
    product_price.should(have.attribute("data-price-amount").value(price))


def img_should_have_name(text):
    product_img.should(have.attribute('alt').value(text))


def details_should_contain_text(text):
    details.should(have.text(text))


def more_information_tab_should_contain_text(style, material, pattern, climate):
    more_info_tab.click()
    s('td[data-th="Style"]').should(have.text(style))
    s('td[data-th="Material"]').should(have.text(material))
    s('td[data-th="Pattern"]').should(have.text(pattern))
    s('td[data-th="Climate"]').should(have.text(climate))


def select_size(size):
    s(f'[option-label="{size}"]').click()
    size_indicator.should(be.visible).hover()


def size_indicator_should_have_text(text):
    size_indicator.should(have.text(text))


def size_label_should_have_frame_with_color(size, color_hex):
    size_label = s(f'[option-label={size}]')
    size_label.should(have.css_property('outline-color').value(Color.from_string(color_hex).rgba))


def size_should_be_selected(size, true_or_false):
    size_label = s(f'[option-label={size}]')
    size_label.should(have.attribute('aria-checked').value(true_or_false))


def add_to_wish_list():
    s('a.action.towishlist').click()


def click_reviews_tab():
    s('#tab-label-reviews').click()


def reviews_should_have_title(title, text):
    try:
        s('#tab-label-reviews-title span.counter')
        reviews_block.should(have.text(title))
    except:
        product_name_in_reviews.should(have.text(text))
