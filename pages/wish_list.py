from selene import browser, be, have, command
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/wishlist/"


def visit():
    browser.open(url)


def click_update():
    s(".update").click()


def should_be_clickable():
    s(".update").should(be.clickable)


def url_should_contain(param):
    browser.should(have.url_containing(param))


def get_products():
    return ss('.product-item-info')


def verify_trash_bin_icon_present():
    items = get_products()
    size = len(items)
    count = 0
    for i in range(size):
        items[i].perform(command.js.scroll_into_view)
        items[i].hover()
        trash_icon = items[i].s('.btn-remove.action.delete')
        trash_icon.should(be.visible)
        trash_icon.should(be.present)
        count += 1
    assert count == size


def remove_item_from_wish_list(product_index):
    product = get_products()[product_index]
    trash_bin_icon = product.s('.btn-remove.action.delete')
    trash_bin_icon.click()

