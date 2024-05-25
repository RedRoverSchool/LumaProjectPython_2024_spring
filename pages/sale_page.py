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
mens_deals_img = 'a.block-promo.sale-mens img'
mens_deals_img_link = 'a.block-promo.sale-mens'
mens_bargains_text = 'a.block-promo.sale-mens span strong'
stretch_your_budget_text = "//span[text()='Stretch your budget with active attire']"
shop_mens_deals = "//span[text()='Shop Men’s Deals']"

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


def is_mens_deals_img_visible():
    s(mens_deals_img).should(be.visible)


def is_mens_deals_img_clickable():
    s(mens_deals_img).should(be.clickable)


def click_mens_deals_img():
    s(mens_deals_img_link).click()


def check_redirection_mens_deals():
    assert browser.driver.current_url == promotions_men_sale_html


def is_stretch_your_budget_text_visible():
    s(stretch_your_budget_text).should(have.text('Stretch your budget with active attire'))


def is_mens_bargains_text_visible():
    s(mens_bargains_text).should(have.text('Men’s Bargains'))


def is_shop_mens_deals_text_visible():
    s(shop_mens_deals).should(have.text('Shop Men’s Deals'))


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
