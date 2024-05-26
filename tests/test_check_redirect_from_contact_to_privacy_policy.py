import pytest
from selene import browser, have

from data.links import *
from pages.locators import *


def test_redirect_from_contact_to_privacy_policy():
    browser.open(PRIVACY_POLICY_PAGE_LINK)
    browser.element(ContactUsLocators.CONTACT_US_LINK).click()
    browser.element(PrivacyPolicy.GO_BACK_LINK).click()
    browser.element(PrivacyPolicy.PRIVACY_POLICY_TITLE).should(have.text('Privacy Policy'))
