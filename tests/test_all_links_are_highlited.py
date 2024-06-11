import allure
import pytest
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s

url_navigate = "https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode"

text = ["Luma Security", "Luma Privacy Policy", "The Information We Collect",
        "How We Use The Information We Collect", "Security",
        "Others With Whom We Share Your Information.", "Your Choices Regarding Use Of The Information We Collect",
        "Your California Privacy Rights", "Cookies, Web Beacons, and How We Use Them",
        "List of cookies we collect", "Online Account Registration", "Emails", "Acceptance", "Questions for Luma?"]


@pytest.mark.parametrize("element", text)
@allure.feature("Privacy and Cookie Policy > Main Content")
@allure.title('Verify link highlight after hovering in left-side navigation block')
@allure.link('https://trello.com/c/hMNWYKkj')
def test_check_color_of_hover_element(element):
    browser.open(url_navigate)
    for item in browser.all(by.css('ul.items > li.item> a')).by(have.text(element)):
        item.hover().should(have.css_property('background-color').value('rgba(232, 232, 232, 1)'))


@pytest.mark.parametrize("element", text)
@allure.feature('Privacy and Cookie Policy > Main Content')
@allure.title("Privacy and Cookie Policy>Main Content>Verify link highlight after hovering")
@allure.link('https://trello.com/c/hMNWYKkj')
def test_all_links_are_highlighted(element):
    browser.open(url_navigate)
    s(by.link_text(element)).should(be.visible).hover()
