from selene import browser, be, have
from selene.support.shared.jquery_style import s
import allure
from data.links import MAIN_PAGE_LINK
from pages.locators import (CreateAccountLocators, LoginLocators)


@allure.feature('Main Page > Main Page')
@allure.title('The “Sign In” and “Create an Account” links are visible and clickable on the main page')
@allure.link('https://trello.com/c/GEQHU5fa')
def test_one(driver):
    browser.open(MAIN_PAGE_LINK)

    s(CreateAccountLocators.CREATE_AN_ACCOUNT_LINK).should(be.visible).click()

    browser.should(have.url('https://magento.softwaretestingboard.com/customer/account/create/'))

    s(CreateAccountLocators.FIRST_NAME).should(be.present)
    s(CreateAccountLocators.LAST_NAME).should(be.present)
    s(CreateAccountLocators.EMAIL_FIELD).should(be.present)
    s(CreateAccountLocators.PASSWORD).should(be.present)
    s(CreateAccountLocators.CONF_PASS).should(be.present)
    s(CreateAccountLocators.CREATE_BUTTON).should(be.present)

    browser.driver.back()

    sign_in = '(//li[@class="authorization-link"])[1]'
    s(sign_in).should(be.visible).click()

    browser.should(have.url_containing('/customer/account/login/'))

    s(LoginLocators.FIELD_NAME).should(be.present)
    s(LoginLocators.FIELD_PASSWORD).should(be.present)
    s(LoginLocators.BUTTON_SUBMIT).should(be.present)
