from selene.support.shared.jquery_style import s
from selene import be, have, browser
import time

url = 'https://magento.softwaretestingboard.com/gear/bags.html'

product_image = s('img[alt="Push It Messenger Bag"]')
add_to_cart_button = s('(//button[@class="action tocart primary"]/span)[1]')
cart_counter = s('.counter-number')


def open():
    browser.open(url)


def cart_button():
    return s('a[class="action showcart active"]')


def view_and_edit_card_button():
    return s('//a[@class="action viewcart"]')


def add_item_to_cart():
    product_image.hover()
    # timesleep is needed for awaiting of the form_key value changing. Test sometime fails without it.
    time.sleep(1)
    add_to_cart_button.wait_until(be.visible)
    add_to_cart_button.click()
    cart_counter.wait_until(have.text('1'))
