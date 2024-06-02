from selene import browser, have
from selene.support.conditions import be
from selene.support.shared.jquery_style import s, ss

link_sale = "https://magento.softwaretestingboard.com/sale.html"
sale_page_url = 'https://magento.softwaretestingboard.com/sale.html'
link_women_sale = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
promotions_men_sale_html = 'https://magento.softwaretestingboard.com/promotions/men-sale.html'
women_jacket_link = "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html"
men_tops_hoodies_url = 'https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html'
create_an_account_link = "(//a[.='Create an Account'])[1]"

breadcrumbs_list = ss(".breadcrumbs li")


def open_page_women_sale():
    browser.open(link_women_sale)


def open_page_men_sale():
    browser.open(promotions_men_sale_html)


def visit_women_jackets():
    browser.open(women_jacket_link)


def open_page():
    browser.open(sale_page_url)


def check_if_breadcrumbs_have_all_parts():
    breadcrumbs_list.should(have.texts('Home', 'Sale'))


def should_be_visible_image(name):
    s(f'//span[contains(text(), "{name}")]/../../img').should(be.visible)


def should_be_clickable_image(name):
    s(f'//span[contains(text(), "{name}")]/../../img').should(be.clickable)


def click_image_with_name(name):
    s(f'//span[contains(text(), "{name}")]/../..').click()


def should_be_redirected_to_url_containing(text):
    browser.should(have.url_containing(text))


def should_be_visible_texts_on_image(text1, text2, text3, image):
    text_elements = ss(f"//span[contains(text(), '{image}')]/../*")
    text_elements[0].should(have.text(text1))
    text_elements[1].should(have.text(text2))
    text_elements[2].should(have.text(text3))


def check_page_title():
    s("h1.page-title").should(have.text('Sale'))


def assert_redirect_url():
    browser.should(have.url(sale_page_url))


def should_be_clickable_create_account():
    s(create_an_account_link).should(be.clickable)


def has_create_account_text():
    s(create_an_account_link).should(have.text('Create an Account'))


def assert_tops_hoodies_url():
    assert browser.driver.current_url == men_tops_hoodies_url


def click_men_deals():
    mens_deals_base_locator = "//ul[@class='items']//a[contains(@href, 'hoodies-and-sweatshirts-men')]"
    s(mens_deals_base_locator).should(be.visible).click()


def has_header_text(header):
    s("#page-title-heading").should(have.text(header))
