import allure
from pages import main_page
from pages import sign_in


@allure.link("https://trello.com/c/3HU9j6R7")
@allure.feature("User is not log in > click Sign in > check authorization page")
def test_check_authorization_page():
    main_page.open_page()
    main_page.sign_in_click()

    sign_in.check_page_title("Customer Login")
    sign_in.check_registered_customers_heading("Registered Customers")
    sign_in.check_new_customers_heading("New Customers")




