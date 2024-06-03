import allure

from pages import sale


class TestMenDeals:
    @allure.suite("US_011.003 | Sale > MEN’s DEALS on side panel")
    @allure.link('https://trello.com/c/aUn0RNxA')
    @allure.feature("TC_011.003.001 I Sale > MEN’s DEALS on side panel > Verify 'Hoodies and Sweatshirts' "
                    "link is visible and clickable, correct redirection")
    def test_verify_hoodies_clickability_visibility_redirection(self):
        sale.open_page()
        sale.click_men_deals()
        sale.has_header_text("Hoodies & Sweatshirts")
        sale.assert_tops_hoodies_url()
