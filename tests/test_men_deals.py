import allure

from pages import sale_page


class TestMenDeals:
    @allure.suite("US_011.003 | Sale > MEN’s DEALS on side panel")
    @allure.link('https://trello.com/c/aUn0RNxA')
    @allure.feature("TC_011.003.001 I Sale > MEN’s DEALS on side panel > Verify 'Hoodies and Sweatshirts' "
                    "link is visible and clickable, correct redirection")
    def test_verify_hoodies_clickability_visibility_redirection(self):
        sale_page.visit_sale()
        sale_page.click_men_deals()
        sale_page.has_header_text("Hoodies & Sweatshirts")
        sale_page.assert_tops_hoodies_url()
