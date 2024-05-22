from selene.support.shared import browser
from selene import have
from selene.support.shared.jquery_style import s


def test_contact_us_link_redirects_to_contact_us_page():
    browser.open('https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode')

    contact_us_link = s('#maincontent > div.columns > div > div.privacy-policy.cms-content > div.privacy-policy-content > p:nth-child(51) > a')
    contact_us_link.click()

    browser.wait_until(have.url_containing('contact-us'))

    header = s('h1')
    header.should(have.text('Whoops, our bad...'))
