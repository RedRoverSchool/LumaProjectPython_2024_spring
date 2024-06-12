import allure
from pages import sign_in


@allure.feature('Sign in > Forgot Your Password?')
@allure.title('The ‘Forgot Your Password?’ link is highlighted while hovering over')
@allure.link('https://trello.com/c/rGtdeLFr')
def test_forgot_password_link_is_highlighted_while_hovering_over():
    sign_in.visit()
    sign_in.verify_forgot_password_link_is_underlined()
