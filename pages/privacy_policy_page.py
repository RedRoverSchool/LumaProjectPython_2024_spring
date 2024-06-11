from selene import browser, by, be, have
from selene.support.shared.jquery_style import s

base_url = 'https://magento.softwaretestingboard.com'
privacy_policy_page_link = base_url + '/privacy-policy-cookie-restriction-mode'

page_main_header_locator = "span[data-ui-id='page-title-wrapper']"
contact_us_link = s("a[href$='/contact/']")
title_page = s('.base')


def open_page():
    browser.open(privacy_policy_page_link)


def open_page_with_navigate_block(url):
    browser.open(url)


def move_to_elements(text_data):
    elements = []
    for i in text_data:
        element = s(by.link_text(i))
        element.hover()
        element.should(be.existing)
        elements.append(element)
    return elements


def get_privacy_policy_url():
    return browser.driver.current_url


def is_header_has_text(title):
    s(page_main_header_locator).should(have.text(title))


def is_current_url():
    return get_privacy_policy_url() == privacy_policy_page_link


def click_to_contact_us_link():
    contact_us_link.click()


def check_redirect_to_contact_us_page(text):
    browser.wait_until(have.url_containing('contact-us'))
    title_page.should(have.text(text))
