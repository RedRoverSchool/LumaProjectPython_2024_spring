from selene import browser, be, have, command
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.by import By

url = "https://magento.softwaretestingboard.com/wishlist/"
product_url = "https://magento.softwaretestingboard.com/aether-gym-pant.html?qty=1#143=&93="

ADD_TO_WISHLIST = "a[class='action towishlist']"
SUCCESS_MSG = "div[class='message-success success message']"
ITEM_CARD = "(//div[@class='product-item-info'])[1]"
REMOVE_ITEM = "//div[@class='product-item-actions']/a[@class='btn-remove action delete']"
ITEM_TITLE = "(//div[@class='products-grid wishlist']//a[@class='product-item-link'])[1]"


def visit(url=url):
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


def remove_item():
    item_title = browser.driver.find_element(By.XPATH, ITEM_TITLE).text
    s(REMOVE_ITEM).should(be.visible).click()
    return item_title


def add_item_to_wish_list():
    visit(product_url)
    s(ADD_TO_WISHLIST).should(be.clickable).click()
    s(SUCCESS_MSG).should(be.visible)


def hover_over_item():
    s(ITEM_CARD).should(be.present).hover()


def is_item_removed(item):
    s(ITEM_TITLE).should(have.no.text(item))
