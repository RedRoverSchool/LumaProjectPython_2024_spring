import allure

from pages import whats_new_page
from pages import yoga_page


@allure.suite("US_006.007 | What`s new page > New Luma Yoga Collection")
class TestYoga:
    @allure.link("https://trello.com/c/G7Iz9eaQ")
    @allure.title("TC_006.007.001 | The New Luma Yoga Collection link and Shop New Yoga button links"
                  " are displayed on the What's New page")
    def test_new_luma_yoga_collection_link_visibility(self, browser_management):
        whats_new_page.open_page()
        whats_new_page.is_yoga_link_visible()
        whats_new_page.is_button_visible()

    @allure.link("https://trello.com/c/jqrXmRkR")
    @allure.title("TC_006.007.002| What`s new page > New Luma Yoga Collection > "
                  "The \"New Luma Yoga Collection\" link redirects to New Luma Yoga Collection page")
    def test_yoga_link_redirection(self):
        whats_new_page.open_page()
        whats_new_page.new_yoga_link_click()
        assert whats_new_page.is_current_url_yoga()
        whats_new_page.verify_header_text('New Luma Yoga Collection')

    @allure.link("https://trello.com/c/oTH09O30")
    @allure.title("TC_006.007.003| What`s new page > New Luma Yoga Collection "
                  "> The \"Shop New Yoga\" button link redirects to New Luma Yoga Collection page")
    def test_yoga_button_redirection(self):
        whats_new_page.open_page()
        whats_new_page.click_button_shop_new_yoga()
        assert whats_new_page.is_current_url_yoga()
        whats_new_page.verify_header_text('New Luma Yoga Collection')


    @allure.link("https://trello.com/c/jRy1WrCH")
    @allure.title("TC_006.007.004| What`s new page > New Luma Yoga Collection > "
                  "The \"List\" button is displayed and changes a page view type")
    def test_yoga_list_button_visibility_and_redirection(self):
        yoga_page.open_page()
        yoga_page.is_list_button_visible()
        yoga_page.list_button_click()
        assert yoga_page.is_current_url_list
        yoga_page.is_wrapper_list_view_visible()

    @allure.link("https://trello.com/c/k2lE2NmK")
    @allure.title("TC_006.007.005| What`s new page > New Luma Yoga Collection "
                  "> The \"Grid\" button is displayed and changes a page view type")
    def test_yoga_grid_button_visibility_and_redirection(self):
        yoga_page.open_list_view_page()
        yoga_page.is_grid_button_visible()
        yoga_page.grid_button_click()
        assert yoga_page.is_current_url_yoga()
        yoga_page.is_wrapper_grid_view_visible()
