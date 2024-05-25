from selene import browser, have
from selene.support.shared.jquery_style import s

url = 'https://magento.softwaretestingboard.com/search/term/popular/'

product_item = s('[class=product-item-link]')
hoodie_link = s('//a[contains(text(),"HOODIE")]')
jacket_link = s('//*[@id="maincontent"]/div[3]/div/ul/li[32]/a')
search_results_header = s('//h1/span[@data-ui-id="page-title-wrapper"]')


def open_page():
    browser.open(url)


def card_titles_should_be_matching_to_link():
    product_item.should(have.text('Jacket'))


def click_on_hoodie_link():
    hoodie_link.click()


def assert_header_text(expected_text):
    search_results_header.should(have.text(expected_text))
