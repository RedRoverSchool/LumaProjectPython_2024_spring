import allure
from selene import browser
from pages.main_page import MainPage
from pages import sign_in


class TestAuthorizationPage:

    @allure.link("https://trello.com/c/3HU9j6R7")
    @allure.feature("User is not log in > click Sign in > check authorization page")
    def test_check_authorization_page(self):
        main_page = MainPage(browser=browser)

        main_page.open_page()
        main_page.sign_in_click()

        sign_in.page_title("Customer Login")
        sign_in.registered_customers_blog("Registered Customers")
        sign_in.new_customers_blog("New Customers")




