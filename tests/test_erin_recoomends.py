import allure
from selene import browser, have

from pages import erin_recommends_page
from pages.main_page import MainPage


@allure.suite("US_001.002 | Testing Erin Recommends Page")
class TestErinRecommends:
    @allure.feature("Main Page > Erin Recommendations")
    @allure.title("Check redirection to 'Shop Erin Recommends' page by clicking block")
    @allure.link('https://trello.com/c/WV6EggMW')
    def test_erin_block_link_redirection(self):
        with allure.step("Open home page"):
            page = MainPage(browser=browser)
            page.open_page()
        with allure.step("Assert Erin recommends block presence and Click"):
            page.is_erin_block_present().click()
            page = erin_recommends_page
        with allure.step("Assert current url == Erin Recommends Page url"):
            page.assert_current_url()
        with allure.step("Find header"):
            header = page.is_header_present()
        with allure.step("Assert header contains text 'Erin Recommends'"):
            page.is_element_text_correct(header, "Erin Recommends")

    @allure.feature("Main Page > Erin Recommendations")
    @allure.title("Paginated Product Catalog Display")
    @allure.link('https://trello.com/c/5IqfevjC')
    def test_pagination_controls(self):
        with allure.step("Open Erin Recommends page"):
            page = erin_recommends_page
            page.open_page()
        with allure.step("Scroll to the bottom of controls presence"):
            page.scroll_to_footer()
        with allure.step("Assert pagination control include at least two page numbers and a 'Next' button"):
            page.verify_minimum_page_numbers(2)
            page.is_next_button_visible()
        with allure.step("Assert the functionality of the pagination control"):
            page.click_next()
            browser.should(have.url_containing("p=2"))

    @allure.feature("Main Page > Erin Recommendations")
    @allure.title("Select Number of Products Displayed")
    @allure.link('https://trello.com/c/Xwdzlpus')
    def test_show_per_page(self):
        with allure.step("Open Erin Recommends page"):
            page = erin_recommends_page
            page.open_page()
        with allure.step("Scroll to and expand the 'Show Per Page' dropdown"):
            page.scroll_to_footer()
            page.expand_show_per_page_dropdown()
        with allure.step("Select a different number to display product per page"):
            page.select_per_page_option(24)
        with allure.step("Assert number of product displayed matches to selection"):
            page.verify_number_of_product_displayed(13, 24)

    @allure.feature("Main Page > Erin Recommendations")
    @allure.title("Arrangement of Products Display")
    @allure.link('https://trello.com/c/SiNG1wlV')
    def test_switch_to_list_view(self):
        with allure.step("Open Erin Recommends page"):
            page = erin_recommends_page
            page.open_page()
        with allure.step("Switch to list view"):
            page.switch_to_list_view()
        with allure.step("Assert that the layout is now in list view"):
            page.is_list_view_activate()


@allure.feature("Main Page > Erin Recommendations")
@allure.title("Adding an Item for Comparison(D_01)")
@allure.link('https://trello.com/c/TQTWkM0l')
def test_add_item_to_compare():
    with allure.step("Open Erin Recommends page"):
        erin_recommends_page.open_page()
        erin_recommends_page.hover_click_item()
        erin_recommends_page.assert_text_of_element(
            "//div[contains(text(), 'You added product Jade Yoga Jacket to the ')]",
            "You added product Jade Yoga Jacket to the ")
        erin_recommends_page.click_text_compare_products()
        erin_recommends_page.assert_text_of_element("//a[contains(text(), 'Jade Yoga Jacket')]", "Jade Yoga Jacket")
