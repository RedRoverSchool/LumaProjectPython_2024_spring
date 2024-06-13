import allure
from selene.support.shared import browser
from selene import be, have
from selene.support.shared.jquery_style import s


class PrivacyPolicyPage:
    def __init__(self):
        self.questions_section = s('#privacy-policy-title-14')
        self.contact_us_link = self.questions_section.element('//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/p[33]/a')

    def open(self):
        browser.open(
            'https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode#privacy-policy-title-2')
        return self

    def scroll_to_bottom(self):
        browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self

    def verify_questions_section(self):
        self.questions_section.should(be.visible)
        return self

    def verify_contact_us_link(self):
        self.contact_us_link.should(be.visible).should(have.text('Contact Us'))
        return self


@allure.feature('Privacy and Cookie Policy > Contact us link')
@allure.title('Verify the presence of the "Contact Us" link')
@allure.link('https://trello.com/c/0rFrHBHE')
def test_presence_of_contact_us_link():
    privacy_policy_page = PrivacyPolicyPage()
    (
        privacy_policy_page
        .open()
        .scroll_to_bottom()
        .verify_questions_section()
        .verify_contact_us_link()
    )
