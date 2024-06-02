import allure
from pages import sign_in


allure.title('TC_004.003.002 | Sign in > Forgot Your Password? > The ‘Forgot Your Password?’ link is highlighted while hovering over')
allure.link('https://trello.com/c/rGtdeLFr')
def test_forgot_password_link_is_highlighted_while_hovering_over():
    sign_in.visit()
    sign_in.verify_forgot_password_link_is_underlined()

