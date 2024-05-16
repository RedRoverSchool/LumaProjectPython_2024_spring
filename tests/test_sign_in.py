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


# @pytest.mark.skip
@allure.link("https://trello.com/c/FxDGeQYY")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_004_005_001_login_unsuccessful():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "")
    sign_in.message_unsuccessful()


# @pytest.mark.skip
@allure.link("https://trello.com/c/otpjtX3K")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_004_005_002_login_successful():
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    sign_in.check_if_this_is_account_url()
    sign_in.check_user_name_is_present("фы ывф")
    sign_in.check_msg_signin_is_missing()


# @pytest.mark.skip
@allure.link("https://trello.com/c/rmFvh9fO")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_004_005_003_nickname_on_each_page_RF():
    # I used only 4 links, otherwise test will take too much time
    sign_in.visit()
    sign_in.login("ahahah1@gmail.com", "jk$34_tor")
    sign_in.check_all_pages_have_user_name("фы ывф")

