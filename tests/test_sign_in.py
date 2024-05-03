import allure
import pytest

from pages import sign_in, my_account, message
from pages.locators import LoginLocators, BaseLocators
from selene import browser, be, have
from selene.support.shared.jquery_style import s


@allure.link("https://trello.com/c/V3vp6nIt")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_sign_in_with_good_credentials():
    sign_in.visit()
    sign_in.login("pamela341714226113@example.com", "@8j%Yltt(E")
    my_account.page_title("My Account")


@pytest.mark.skip
@allure.link("https://trello.com/c/L5xi1X8i")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_sign_in_with_bad_credentials():
    sign_in.visit()
    sign_in.login("jasonbrown1714146903@example.net", "wrong_password")
    message.should_be("account sign-in was incorrect")


@pytest.mark.skip
@allure.link("https://trello.com/c/FxDGeQYY")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_004_005_001_login_unsuccessful():
    browser.open(LoginLocators.LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("")
    s(LoginLocators.BUTTON_SUBMIT).click()
    s(LoginLocators.MESSAGE_UNSUCCESSFUL).should(have.text("This is a required field."))


@pytest.mark.skip
@allure.link("https://trello.com/c/otpjtX3K")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_004_005_002_login_successful():
    browser.open(LoginLocators.LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.should(have.url(LoginLocators.LINK_ACCOUNT))
    s(LoginLocators.USER_NAME_IN_WELCOME).should(have.text("фы ывф"))
    s(LoginLocators.AUTHORIZATION_LINK).should(have.no.text("Sign In"))


@allure.link("https://trello.com/c/rmFvh9fO")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_004_005_003_nickname_on_each_page():
    # I used only 4 links, otherwise test will take too much time
    browser.open(LoginLocators.LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    for lnk in BaseLocators.ALL_URL:
        browser.open(lnk)
        s(LoginLocators.USER_NAME_IN_WELCOME).should(have.text("фы ывф"))

