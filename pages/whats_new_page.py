from selene import browser, command, Element, query
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support.color import Color

product = s(".product-item-info")
products = ss(".product-item-info")
button_new_yoga = s('span.more.button')
layla_tee = s("//a[@title='Layla Tee']")
luma_latest_items = ss('.products-grid>ol>li')
collection_luma_latest_items = ss('.product-image-photo')
new_yoga_link = s("//*[text()='New Luma Yoga Collection']")

add_wish_list = "[aria-label='Add to Wish List']"

whats_new_page_link = 'https://magento.softwaretestingboard.com/what-is-new.html'
yoga_url = 'https://magento.softwaretestingboard.com/collections/yoga-new.html'
layla_tee_url = 'https://magento.softwaretestingboard.com/layla-tee.html'

message = "You must login or register to add items to your wishlist"
add_wish_list_message = "added to your Wish List"


def open_page():
    browser.open(whats_new_page_link)


def get_current_url():
    return browser.driver.current_url


def is_current_url_yoga():
    return browser.driver.current_url == yoga_url


def element_should_have_correct_text(element, text):
    element.should(have.text(text))


def header_should_be_present():
    return s('h1>span').should(be.present)


def luma_latest_should_be_present():
    s('.products-grid>ol').should(be.present)


def is_button_present():
    return button_new_yoga.should(be.present)


def is_button_visible():
    button_new_yoga.should(be.visible)


def is_current_link():
    return get_current_url() == whats_new_page_link


def click_button_shop_new_yoga():
    button_new_yoga.click()


def scroll_to(element: Element):
    element.perform(command.js.scroll_into_view)


def add_items_to_wish_list(size):
    click_button_shop_new_yoga()
    for i in range(size):
        scroll_to(products[i])
        products[i].hover()
        products[i].s(add_wish_list).click()
        s('.message-success.success.message').should(have.text(add_wish_list_message))
        browser.driver.back()


def click_on_wish_list():
    s(add_wish_list).click()


def add_item_to_wish_list():
    open_page()
    click_button_shop_new_yoga()
    scroll_to(product)
    product.hover()
    click_on_wish_list()


def men_and_women_items_both_should_be_present():
    m = 0
    w = 0
    for item in collection_luma_latest_items:
        if item.matching(have.attribute("src").value_containing('/m/')):
            m += 1
        elif item.matching(have.attribute("src").value_containing('/w/')):
            w += 1
    return True if (m > 0 and w > 0) and m + w == 4 else False


def is_yoga_link_visible():
    new_yoga_link.should(be.visible)


def new_yoga_link_click():
    new_yoga_link.click()


def open_eco_collection_url():
    open_page()
    s("//span[contains (text(), 'Shop Eco Friendly')]").click()


def click_layla_tee_name():
    s("a[title='Layla Tee']").click()


def check_redirection_to_layla_tee_pdp():
    return get_current_url() == layla_tee_url


def layla_tee_title_is_displayed():
    s("h1.page-title span").should(be.visible)


def click_layla_tee_img():
    s("img[alt='Layla Tee']").click()


def click_bras_and_tank_link():
    s('.categories-menu ul:nth-child(2) li:nth-child(4) a').click()


def click_breathe_easy_tank_item():
    s("a.product-item-link[href*='breathe-easy-tank']").click()


def add_to_cart_button():
    s('//*[@id="product-addtocart-button"]/span').click()


def add_to_compare_button():
    s('.product-social-links a:last-child').click()


def add_to_wish_list_button():
    s('.product-social-links a:first-child').click()


def change_layla_tee_color(color):
    layla_tee.hover()
    s(f"//li[2]//div[@option-label='{color}']").click()
    layla_tee.hover()


def is_color_selected(color_name, color_hex):
    color_selector = f"//li[2]//div[@option-label='{color_name}']"
    s(color_selector).should(have.css_property('outline-color').value(Color.from_string(color_hex).rgba))


def is_layla_tee_img_color_correct(color):
    img_url = f"https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/s/ws04-{color}_main_1.jpg"
    s('//li[2]//img[@class="product-image-photo"]').wait_until(have.attribute('src').value(img_url))
    color_img_name = f'ws04-{color}_main_1.jpg'
    assert color_img_name in s('//li[2]//img[@class="product-image-photo"]').get(query.attribute('src'))


def check_buttons_visibility_on_product_card():
    for i in range(1, 6):
        s(f"//li[{i}]/div/div").hover()
        s(f'//li[{i}]//button[@class="action tocart primary"]').should(be.visible)
        s(f'//li[{i}]//a[@class="action towishlist"]').should(be.visible)
        s(f'//li[{i}]//a[@class="action tocompare"]').should(be.visible)


def verify_header_text(text):
    s('#page-title-heading > span').should(have.text(text))


def hover_on_product():
    scroll_to(product)
    product.hover()


def check_redirection_to_login():
    s("span.base[data-ui-id='page-title-wrapper']").should(have.text("Customer Login"))
    s("div[data-bind='html: $parent.prepareMessageForHtml(message.text)']").should(have.text(message))


def get_number_of_luma_latest():
    return len(luma_latest_items)