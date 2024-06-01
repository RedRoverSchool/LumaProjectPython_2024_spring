from selene import browser, be, have, command, query
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.by import By

url = "https://magento.softwaretestingboard.com/wishlist/"
product_url = "https://magento.softwaretestingboard.com/aether-gym-pant.html?qty=1#143=&93="
WOMEN_JACKET_LINK = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
add_to_wishlist = "a[class='action towishlist']"
success_msg = "div[class='message-success success message']"
item_card = "(//div[@class='product-item-info'])[1]"
REMOVE_ITEM = "//div[@class='product-item-actions']/a[@class='btn-remove action delete']"
item_title = "(//div[@class='products-grid wishlist']//a[@class='product-item-link'])[1]"
success_add_msg_text = s("div[class='message-success success message'] div")

url_login = "https://magento.softwaretestingboard.com/customer/account/login"
user_email = s("div.login-container #email")
user_password = s("div.login-container #pass")
sign_in_button = s("div.login-container #send2")

ITEM_1_ADD_TO_WISH_LIST = 'ol > li:nth-child(1) a.action.towishlist'
ITEM_6_ADD_TO_WISH_LIST = 'ol > li:nth-child(6) a.action.towishlist'
ITEM_8_ADD_TO_WISH_LIST = 'ol > li:nth-child(8) a.action.towishlist'
ITEM_9_ADD_TO_WISH_LIST = 'ol > li:nth-child(9) a.action.towishlist'
LINK_SALE = "https://magento.softwaretestingboard.com/sale.html"
delete_bucket = '.btn-remove.action.delete'

update = s(".update")
products = ss('.products-grid.wishlist .product-item')
message_wish_list_is_empty = s('div.block.block-wishlist > div.block-content > div')

empty_message = 'You have no items in your wish list.'
removed_message = 'has been removed from your Wish List.'
add_wish_list_message = "added to your Wish List"
ITEMS_IN_WISHLIST = '#wishlist-sidebar > li strong > a > span'
ITEMS_ON_WISH_PAGE = '.form-wishlist-items .product-item-info'


def visit(url=url):
    browser.open(url)


def click_update():
    update.click()


def should_be_clickable():
    update.should(be.clickable)


def url_should_contain(param):
    browser.should(have.url_containing(param))


def verify_trash_bin_icon_present():
    items = products
    size = len(items)
    count = 0
    for i in range(size):
        items[i].perform(command.js.scroll_into_view).hover()
        items[i].s(delete_bucket).should(be.visible).should(be.present)
        count += 1
    assert count == size


def has_success_message():
    assert s('div.message-success.success.message div').should(have.text(removed_message))


def remove_item_from_wish_list(index):
    product = products[index]
    product.hover().s(delete_bucket).click()
    has_success_message()


def edit_item_in_wish_list(index, qty, color, size):
    p = products[index]
    p.hover().s(".product-item-actions").click()
    ss(".input-text.qty").second.clear().send_keys(qty)
    p.s('.actions-primary').click()
    ss("div.swatch-attribute.color .swatch-option.color")[color].click()
    ss("div.swatch-attribute.size .swatch-option.text")[size].click()
    s("a.action.towishlist.updated").click()


def is_wish_list_empty():
    s('.message.info.empty span').should(have.text(empty_message))


def remove_item():
    s(REMOVE_ITEM).should(be.visible).click()
    return browser.driver.find_element(By.XPATH, item_title).text


def add_item_to_wish_list():
    visit(product_url)
    s(add_to_wishlist).should(be.clickable).click()
    s(success_msg).should(be.visible)


def hover_over_item():
    s(item_card).should(be.present).hover()


def is_item_removed(item):
    s(item_title).should(have.no.text(item))


def wish_list_is_empty():
    message_wish_list_is_empty.should(have.text(empty_message))


def wish_list_is_not_empty():
    message_wish_list_is_empty.should(have.no.text(empty_message))


def add_to_wish_list_from_catalog(item):
    s(item).perform(command.js.click)


def go_to_wish_list():
    s('.action.details').should(be.clickable).click()


def title_is_correct():
    s("h1").should(have.text("My Wish List"))


def clear_wish_list():
    if wish_list_is_not_empty():
        items_in_wish_list = ss(delete_bucket)
        for item in items_in_wish_list:
            item.should(be.clickable).click()


def success_adding_msg_should_have_text(text):
    success_add_msg_text.should(have.text(text))


def product_should_have_title(title):
    s(f'a.product-item-link[title="{title}"]').should(be.visible)

    
def visit_women_jackets():
    browser.open(WOMEN_JACKET_LINK)


def visit_login():
    browser.open(url_login)


def login(user, password):
    user_email.type(user)
    user_password.type(password)
    sign_in_button.click()


def check_qty_in_wishlist():
    s('div.block.block-wishlist > div.block-title > span').should(have.text('3 items'))


def count_items_in_wishlist(nr):
    title_items_nr = ss('[data-bind="text: product_name"]')
    assert len(title_items_nr) == nr


def count_button_add_tocart(nr):
    buttons = ss('#wishlist-sidebar button')
    assert len(buttons) == nr


def count_prices_in_wishlist(nr):
    prices = ss('.price-as-configured')
    assert len(prices) == nr


def items_name_in_wishlist_is_clickable():
    links = ss('#wishlist-sidebar strong > a')
    for ln in links:
        ln.should(be.clickable)


def images_in_wishlist_is_clickable():
    images = ss('//*[@id="wishlist-sidebar"]/li[1]/div/a/span/span/img')
    for ima in images:
        ima.should(be.clickable)


def count_images_in_wishlist(nr):
    images = ss('#wishlist-sidebar div > a > span > span > img')
    assert len(images) == nr


# def check_link_go_to_wishlist_is_clickable():
#     s('//*[@id="maincontent"]//div[3]/div[3]/div[2]/div/div/a').should(be.clickable)


def visit_sale():
    browser.open(LINK_SALE)


def collect_items_for_wishpage():
    links = ss('#wishlist-sidebar strong > a')
    wishlist_page = []
    for ln in links:
        item_text = ln.get(query.attribute("text")).strip()
        wishlist_page.append(item_text)
    return wishlist_page


def compare_side_panel_and_wishpage(wishlist):
    for item in wishlist:
        assert len(f'[alt={item}]')
