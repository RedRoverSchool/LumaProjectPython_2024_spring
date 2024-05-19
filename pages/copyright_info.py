from selene.support.shared.jquery_style import s
from selene import have
from data.page_data import FooterData


def scroll_to(browser):
    browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


def is_copyright_info_visible(element):
    s(element).should(have.text(FooterData.copyright_info))
