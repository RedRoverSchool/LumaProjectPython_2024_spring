import allure

from pages import forgot_password, message


@allure.feature('Sign in > Registration, Account')
@allure.title('Check reset user password')
@allure.link('https://trello.com/c/uVaFutGs')
def test_reset_user_password(user_email):
    forgot_password.visit()
    forgot_password.reset(user_email)
    message.should_be_message("you will receive an email")
