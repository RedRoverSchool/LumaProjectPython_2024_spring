import allure
import pytest

from pages import create_account, message
from pages.create_account import redirect


@pytest.mark.skip
def test_create_account(first_name, last_name, user_email, password):
    print("user: ", user_email, password)
    create_account.visit()
    create_account.new_one(first_name, last_name, user_email, password)
    message.should_be("Thank you for registering")


@pytest.mark.skip
def test_create_account_with_empty_first_name(last_name, user_email, password):
    create_account.visit()
    create_account.new_one("", last_name, user_email, password)
    create_account.first_name_error("This is a required field.")


@allure.link("https://trello.com/c/MI25boC8")
@allure.feature("Sign in & Registration, Account >Create an account")
def test_004_006_05_verify_the_redirection_after_creating_account():
    create_account.visit()
    create_account.click_the_create_account_link()
    create_account.page_title()
    redirect()

