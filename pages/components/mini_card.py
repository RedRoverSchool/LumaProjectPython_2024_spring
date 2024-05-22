from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color

CART_URL = 'https://magento.softwaretestingboard.com/checkout/cart/'

action = s('a.action')
quantity = s(".details-qty input")
message = s(".message-success")
mini_cart = s('#ui-id-1')
update = s('[title="Update"]')
cart_subtotal = s('.subtotal .price')
mini_cart_view = s('.action.viewcart')
see_details = s('[data-role="title"]')
view_and_edit_cart_href = s("[class='action viewcart']")
view_and_edit_cart_link = s("//*[text()='View and Edit Cart']")
size_m = s('//*[@class="product options list"]//*[text()="M"]')
color_gray = s('//*[@class="product options list"]//*[text()="Gray"]')
price_item = s('//*[@class="minicart-price"]//*[@class="price"]')
argus_all_weather = s('//*[text()="Argus All-Weather Tank"]')

def is_mini_cart_present():
    mini_cart.should(be.present)

def is_mini_cart_visible():
    mini_cart.should(be.visible)

def is_mini_cart_have_link():
    mini_cart_view.should(have.attribute('href').value(CART_URL))

def check_color_of_in_the_mini_cart(color):
    action.should(have.css_property("color").value(Color.from_string(color).rgba))

def check_edit_cart_link_in_the_mini_cart():
    view_and_edit_cart_href.should(have.attribute("href"))

def check_the_link_opens_checkout_cart_page():
    view_and_edit_cart_link.click()

def checking_the_size_color_and_product_name_are_correct():
    see_details.click()
    size_m.should(have.text("M"))
    color_gray.should(have.text("Gray"))
    argus_all_weather.should(have.text("Argus All-Weather Tank"))

def change_qty(qty):
    quantity.should(be.clickable).send_keys(Keys.BACKSPACE + qty)
    update.click()

def should_be_quantity_change(qty):
    quantity.should(have.value(qty))

def should_be_success_message():
    message.should(be.visible)

def should_be_change_subtotal(price, total):
    price_item.should(have.text(price))
    cart_subtotal.should(have.text(total))

def click_mini_cart():
    mini_cart.should(be.clickable).click()
