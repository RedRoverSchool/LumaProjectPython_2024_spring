import allure
from selene import browser
from pages.set_of_sprite_yoga_straps_page import SetYogaStraps
from pages.locators import SetYogaStrapsLocators as SYSL
from data.page_data import SetYogaStrapsData as SYSD
from data.links import SET_YOGA_STRAPS_URL
from pages import set_of_sprite_yoga_straps_page
import pytest

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


def test_009_005_004_put_sets_of_straps_in_the_cart():
    set_of_sprite_yoga_straps_page.visit()
    # add 1 set to cart
    set_of_sprite_yoga_straps_page.add_to_cart_set_8_foot(1)
    set_of_sprite_yoga_straps_page.is_visible_success_message()
    set_of_sprite_yoga_straps_page.check_nr_of_items_in_cart(1)
    # add 3 sets to cart
    set_of_sprite_yoga_straps_page.add_to_cart_set_8_foot(3)
    set_of_sprite_yoga_straps_page.is_visible_success_message()
    set_of_sprite_yoga_straps_page.check_nr_of_items_in_cart(4)

