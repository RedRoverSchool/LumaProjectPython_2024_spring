import allure
from selene import browser, be
from selene.support.shared.jquery_style import s, ss
from selene.support.shared import browser

from pages.set_of_sprite_yoga_straps_page import SetYogaStraps
from pages.locators import SetYogaStrapsLocators as SYSL
from data.page_data import SetYogaStrapsData as SYSD
from data.links import SET_YOGA_STRAPS_URL
from pages import product_page, fitness_equipment_page


@allure.suite("US_009.005 | Gear catalog > Fitness Equipment > Set of Sprite Yoga Straps")
class TestFitnessEquipment:
    @allure.link("https://trello.com/c/sLFXvIMH")
    @allure.title("TC_009.005.003| Gear catalog > Fitness Equipment > Set of Sprite Yoga Straps >"
                  "Adding more than the available quantity \"Sprite Yoga Strap 6 foot\" to Shopping Cart")
    def test_adding_more_than_the_available_quantity(self, browser_management):
        page = SetYogaStraps(browser)
        page.visit(SET_YOGA_STRAPS_URL)
        page.add_to_cart_more(1000)

        page.assert_text_of_element(SYSL.NOT_AVAILABLE_MESSAGE, SYSD.qty_is_not_available_message)


@allure.suite("US_009.003| Gear catalog > Fitness Equipment")
class TestFitnessEquipment0:
    @allure.link("https://trello.com/c/s9qvWzzt")
    @allure.title(
        "TC_009.003.001 | Gear catalog > Fitness Equipment > Check the user can read reviews about the product")
    def test_check_user_can_read_reviews(self, browser_management):
        fitness_equipment_page.open_page()
        product = s("a.action.view")

        product.wait_until(be.visible)
        product.click()
        product_page.open_reviews_tab()

        reviews = ss("#customer-reviews")

        for review in reviews:
            assert product_page.is_review_details_visible(review)
            assert product_page.is_rating_visible(review)
