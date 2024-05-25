
import allure

from pages import set_of_sprite_yoga_straps_page, women_page


@allure.suite("US_009.005 | Gear catalog > Fitness Equipment > Set of Sprite Yoga Straps")
class TestFitnessEquipment:
    @allure.link("https://trello.com/c/sLFXvIMH")
    @allure.title("TC_009.005.003| Gear catalog > Fitness Equipment > Set of Sprite Yoga Straps >" 
                    "Adding more than the available quantity \"Sprite Yoga Strap 6 foot\" to Shopping Cart")
    def test_adding_more_than_the_available_quantity(self):
        page = set_of_sprite_yoga_straps_page
        page.visit()
        page.add_to_cart_more(1000)
        page.assert_text_of_element('//div[contains(text(),"The requested qty is not available")]', 'The requested qty is not available')


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


def test_009_005_005_check_additional_info():
    set_of_sprite_yoga_straps_page.visit()
    set_of_sprite_yoga_straps_page.open_window_more_info()
    set_of_sprite_yoga_straps_page.check_details_about_material("Canvas, Plastic")


def test_009_005_006_application_of_discount_amount_more_200():
    set_of_sprite_yoga_straps_page.visit()
    set_of_sprite_yoga_straps_page.add_to_cart_set_6_foot(6)
    set_of_sprite_yoga_straps_page.add_to_cart_set_8_foot(6)
    set_of_sprite_yoga_straps_page.add_to_cart_set_10_foot(6)
    set_of_sprite_yoga_straps_page.check_nr_of_items_in_cart(18)
    women_page.open_minicart()
    set_of_sprite_yoga_straps_page.open_link_view_and_edit_cart()
    set_of_sprite_yoga_straps_page.check_discount_amount_more_200()


