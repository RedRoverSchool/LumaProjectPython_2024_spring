from selene import browser, by, be, have
from selene.support.shared.jquery_style import s
import allure
from data.links import MAIN_PAGE_LINK
from pages.locators import (CreateAccountLocators, LoginLocators)

@allure.title('TC_001.001.003 | The “Sign In” and “Create an Account” links are visible and clickable on the main page')
def test_one(driver):
    with allure.step("Open home page"):
        browser.open(MAIN_PAGE_LINK)
    with allure.step("Click on 'Create an Account'"):
        s(CreateAccountLocators.CREATE_AN_ACCOUNT_LINK).should(be.visible).click()
    with allure.step("Assert url containing str'....customer/account/create/'"):
        browser.should(have.url('https://magento.softwaretestingboard.com/customer/account/create/'))
    with allure.step("Assert registation form is present"):
        s(CreateAccountLocators.FIRST_NAME).should(be.present)
        s(CreateAccountLocators.LAST_NAME).should(be.present)
        s(CreateAccountLocators.EMAIL_FIELD).should(be.present)
        s(CreateAccountLocators.PASSWORD).should(be.present)
        s(CreateAccountLocators.CONF_PASS).should(be.present)
        s(CreateAccountLocators.CREATE_BUTTON).should(be.present)
    with allure.step("Return to the main page"):
        browser.driver.back()
    with allure.step("Click on 'Sign in'"):
        sign_in = '(//li[@class="authorization-link"])[1]'
        s(sign_in).should(be.visible).click()
    with allure.step("Assert url containing str'.../customer/account/login/'"):
        browser.should(have.url_containing('/customer/account/login/'))
    with allure.step("Assert that fields 'name', 'password' and 'button submit' is present"):
        s(LoginLocators.FIELD_NAME).should(be.present)
        s(LoginLocators.FIELD_PASSWORD).should(be.present)
        s(LoginLocators.BUTTON_SUBMIT).should(be.present)


