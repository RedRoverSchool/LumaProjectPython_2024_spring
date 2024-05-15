from selene.support.shared import browser
from selene import be, have
from selene.support.shared.jquery_style import s, ss


def test_contact_us_link_presence():
    # Open the Privacy Policy page
    browser.open('https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode#privacy-policy-title-2')

    # Scroll to the bottom of the page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Checking the presence of the 'Questions for Luma?' section at the bottom
    questions_section = s('//*[@id="privacy-policy-title-14"]')
    questions_section.should(be.visible)

    # Verify the presence and correctness of the "Contact Us" link
    contact_us_link = questions_section.element('//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/p[33]/a')
    contact_us_link.should(be.visible).should(have.text('Contact Us'))