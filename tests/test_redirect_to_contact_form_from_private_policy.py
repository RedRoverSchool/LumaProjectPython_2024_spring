import allure
from selene import browser, by, be, have, support
from selene.support.shared.jquery_style import s

base_url = "https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode"
contact_us_url = "https://magento.softwaretestingboard.com/contact/"


@allure.title("Verify redirect from Privacy Policy to Contact Us link")
def test_redirect_to_contact_form_from_private_policy():
    browser.open(base_url)
    s(by.link_text("Questions for Luma?")).click()
    s(by.link_text("Contact Us")).click()
    browser.should(have.url(contact_us_url))
    s(by.css("span[class='base']")).should(have.text("Whoops, our bad..."))

