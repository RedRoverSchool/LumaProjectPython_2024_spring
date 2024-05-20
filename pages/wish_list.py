from selene import browser, be, have, command
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.by import By
from pages.locators import WishListLocators as WishList, BaseLocators
from data.page_data import WishListData as Data

url = "https://magento.softwaretestingboard.com/wishlist/"
product_url = "https://magento.softwaretestingboard.com/aether-gym-pant.html?qty=1#143=&93="

ADD_TO_WISHLIST = "a[class='action towishlist']"
SUCCESS_MSG = "div[class='message-success success message']"
ITEM_CARD = "(//div[@class='product-item-info'])[1]"
REMOVE_ITEM = "//div[@class='product-item-actions']/a[@class='btn-remove action delete']"
ITEM_TITLE = "(//div[@class='products-grid wishlist']//a[@class='product-item-link'])[1]"

ITEM_6_ADD_TO_WISH_LIST = 'ol > li:nth-child(6) a.action.towishlist'
ITEM_8_ADD_TO_WISH_LIST = 'ol > li:nth-child(8) a.action.towishlist'
ITEM_9_ADD_TO_WISH_LIST = 'ol > li:nth-child(9) a.action.towishlist'


def visit(url=url):
    browser.open(url)


def click_update():
    s(".update").click()


def should_be_clickable():
    s(".update").should(be.clickable)


def url_should_contain(param):
    browser.should(have.url_containing(param))


def get_products():
    return ss(WishList.PRODUCT_ITEM)


def verify_trash_bin_icon_present():
    items = get_products()
    size = len(items)
    count = 0
    for i in range(size):
        items[i].perform(command.js.scroll_into_view).hover()
        items[i].s(WishList.DELETE_BUCKET).should(be.visible).should(be.present)
        count += 1
    assert count == size


def has_success_message():
    assert s(BaseLocators.SUCCESS_MESSAGE).should(have.text(Data.removed_message))


def remove_item_from_wish_list(index):
    product = get_products()[index]
    product.hover().s(WishList.DELETE_BUCKET).click()
    has_success_message()


def edit_item_in_wish_list(index, qty, color, size):
    get_products()[index].hover().s(WishList.ITEM_ACTIONS).click()
    s(WishList.QUALITY).clear().send_keys(qty)
    ss(WishList.COLORS)[color].click()
    ss(WishList.SIZES)[size].click()
    s(WishList.UPDATED).click()


def is_wish_list_empty():
    s(WishList.EMPTY_MESSAGE).should(have.text(Data.empty_message))


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


def wish_list_is_empty():
    s(WishList.MESSAGE_WISH_LIST_IS_EMPTY).should(have.text(Data.empty_message))


def wish_list_is_not_empty():
    s(WishList.MESSAGE_WISH_LIST_IS_EMPTY).should(have.no.text(Data.empty_message))


def add_to_wish_list_from_catalog(item_nr):
    s(item_nr).perform(command.js.click)


def go_to_wish_list():
    s('.action.details').should(be.clickable).click()


def title_is_correct():
    s(BaseLocators.PAGE_TITLE).should(have.text("My Wish List"))


def clear_wish_list():
    if wish_list_is_not_empty():
        items_in_wish_list = ss('.btn-remove.action.delete')
        for item in items_in_wish_list:
            item.should(be.clickable).click()

