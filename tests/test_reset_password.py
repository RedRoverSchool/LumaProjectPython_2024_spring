from pages import forgot_password, message


def test_reset_user_password(user_email):
    forgot_password.visit()
    forgot_password.reset(user_email)
    message.should_be_message("you will receive an email")
