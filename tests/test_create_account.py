import allure

from pages import create_account, message


@allure.feature('Sign in & Registration, Account > Create an account')
@allure.title('Verifying that the account was successfully created')
def test_create_account(first_name, last_name, user_email, password):
    create_account.visit()
    create_account.create_account(first_name, last_name, user_email, password)
    message.should_be_message("Thank you for registering")


@allure.feature('Sign in & Registration, Account > Create an account')
@allure.title('Create account with empty first name')
def test_create_account_with_empty_first_name(last_name, user_email, password):
    create_account.visit()
    create_account.create_account("", last_name, user_email, password)
    create_account.should_be_first_name_error("This is a required field.")


@allure.feature("Sign in & Registration, Account > Create an account")
@allure.title('Verify the redirection of the link')
@allure.link("https://trello.com/c/MI25boC8")
def test_004_006_05_verify_the_redirection_after_creating_account():
    create_account.visit()
    create_account.click_the_create_account_link()
    create_account.should_have_page_title('Create New Customer Account')
    create_account.should_be_create_account_url()
