import allure

from pages import sale


@allure.feature("Sale > MEN’s DEALS on side panel")
@allure.link('https://trello.com/c/aUn0RNxA')
@allure.title("Verify 'Hoodies and Sweatshirts' link is visible and clickable, correct redirection")
def test_verify_hoodies_clickability_visibility_redirection():
    sale.open_page()
    sale.click_men_deals()
    sale.has_header_text("Hoodies & Sweatshirts")
    sale.assert_tops_hoodies_url()
