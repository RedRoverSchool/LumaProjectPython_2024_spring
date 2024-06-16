from selene.support.shared.jquery_style import s, ss
from pages.locators import BaseLocators
from selene import browser, be, have, query

link_women_sale = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
women_page_link = 'https://magento.softwaretestingboard.com/women.html'
link_tees_women = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"
base_url = 'https://magento.softwaretestingboard.com'
link_top_women = base_url + '/women/tops-women.html'
bottoms_women_page_link = base_url + '/women/bottoms-women.html'
tops_women_page_link = base_url + '/women/tops-women.html'

add_to_compare_icon = s("(//a[@title='Add to Compare'])[1]")
bottoms_link = s("//*[@id='ui-id-10']")
bottoms_page_title = '.page-title-wrapper span'
breadcrumbs_links = ss('.breadcrumbs > ul  > li > a')
breadcrumbs_list = ss(".breadcrumbs li")
checkout_button = s('#top-cart-btn-checkout')
comp_list_radiant_tee = s("//a[contains(text(), 'Radiant Tee')]")
compare_btn = s("//span[text()='Compare']")
dropdown_block = s("//*[@id='ui-id-2']/li[2]/ul")
footer_links = ('xpath', '//footer[@class="page-footer"]//li')
link_search_terms = s('footer > div > ul > li:nth-child(1)')
message_success_add = s("div.messages [data-bind ^='html']")
page_title = s("h1")
radiant_tee_hotsellers_sect = s("//a[contains(text(), 'Radiant Tee')]")
show_basket = s(".action.showcart")
tank_button_add = s('//*[@title="Breathe-Easy Tank"]/../..//*[@title="Add to Cart"]')
tank_color = s('//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="Yellow"]')
tank_size = s('//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="M"]')
tops_link = s('a#ui-id-9')
tops_page_title = '.page-title-wrapper'
women_menu = s("//*[@id='ui-id-4']")


def visit():
    browser.open(women_page_link)


def move_to_woman_menu():
    women_menu.hover()


def click_dropdown_tops_link():
    tops_link.click()


def click_dropdown_bottoms_link():
    bottoms_link.click()


def hover_product_card():
    radiant_tee_hotsellers_sect.hover()


def click_add_to_compare_icon():
    add_to_compare_icon.click()


def click_compare_btn():
    compare_btn.click()


def assert_page_title():
    assert page_title.should(have.text('Compare Products')), "wrong title"


def assert_comp_list_item():
    assert comp_list_radiant_tee.should(have.text('Radiant Tee')), "wrong item"


def visit_women_tee():
    browser.open(link_tees_women)


def check_if_breadcrumbs_have_all_parts():
    breadcrumbs_list.should(have.texts('Home', 'Women', 'Tops', 'Tees'))


def check_nr_of_links_from_women_tee_by_breadcrumbs():
    elements = breadcrumbs_links.by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_count():
    elements = breadcrumbs_links.by(have.attribute('href'))
    elements.should(have.size(3))


def check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr():
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/women.html',
                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    for i, item in enumerate(ss(BaseLocators.BREADCRUMBS_LINKS).by(have.attribute('href'))):
        assert expected_links[i] == item.get(query.attribute('href'))


def visit_women_sale():
    browser.open(link_women_sale)


def check_breadcrumbs_from_women_sale_have_attribute():
    elements = breadcrumbs_links.by(have.attribute('href'))
    expected_links = ['https://magento.softwaretestingboard.com/',
                      'https://magento.softwaretestingboard.com/sale.html']
    for i, element in enumerate(elements):
        element.should(have.attribute('href').value(expected_links[i]))


def check_breadcrumbs_from_women_sale_have_word():
    # assert error !!! 'Sale' is missing
    breadcrumbs_list.should(have.texts('Home', 'Women Sale'))


def choose_size_for_tank():
    tank_size.click()


def choose_color_for_tank():
    tank_color.click()


def button_add_to_cart_tank():
    tank_button_add.click()


def success_msg_is_present():
    message_success_add.should(have.text("You added"))


def open_minicart():
    show_basket.should(be.clickable).click()


def open_checkout():
    checkout_button.should(be.visible)
    checkout_button.should(be.clickable).click()


def find_link_in_footer():
    link_search_terms.should(be.visible)


def click_link_in_footer():
    link_search_terms.should(be.clickable).click()


def title_is_correct():
    page_title.should(have.text("Popular Search Terms"))


def should_be_redirect_to(link):
    browser.should(have.url(link))


def dropdown_menu_have_elements(first_elem, second_elem):
    dropdown_block.should(have.text(first_elem) and have.text(second_elem))


def should_have_page_title(locator, title):
    s(locator).should(have.text(title))


def visit_tops_women():
    browser.open(link_top_women)


def visit_bottoms_women():
    browser.open(bottoms_women_page_link)