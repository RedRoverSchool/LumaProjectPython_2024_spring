from selene import browser, by, be, have
from selene.support.shared.jquery_style import s

page_main_header_locator = "span[data-ui-id='page-title-wrapper']"
privacy_policy_page_link = 'https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode'


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