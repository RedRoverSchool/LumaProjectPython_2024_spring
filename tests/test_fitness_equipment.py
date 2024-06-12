import allure
from selene import be
from selene.support.shared.jquery_style import ss, s
from pages import set_of_sprite_yoga_straps_page, women_page, fitness_equipment_page


@allure.feature("Gear catalog > Fitness Equipment")
@allure.title("Adding more than the available quantity \"Sprite Yoga Strap 6 foot\" to Shopping Cart")
@allure.link("https://trello.com/c/sLFXvIMH")
def test_adding_more_than_the_available_quantity():
    page = set_of_sprite_yoga_straps_page
    page.visit()
    page.add_to_cart_more(1000)
    page.assert_text_of_element('//div[contains(text(),"The requested qty is not available")]',
                                'The requested qty is not available')


@allure.feature("Gear catalog > Fitness Equipment")
@allure.title("Check the user can read reviews about the product")
@allure.link("https://trello.com/c/s9qvWzzt")
def test_check_the_user_can_read_reviews_about_the_product():
    fitness_equipment_page.open_page()
    link_to_reviews = 'a.action.view'
    s(link_to_reviews).click()
    reviews = ss("#customer-reviews")
    for review in reviews:
        assert review.should(be.visible)


@allure.feature("Gear catalog > Fitness Equipment")
@allure.title("Put set or a few sets of “Sprite Yoga Strap 8 foot” in the cart")
@allure.link("https://trello.com/c/PJ8YNNCm")
def test_put_sets_of_straps_in_the_cart():
    set_of_sprite_yoga_straps_page.visit()
    # add 1 set to cart
    set_of_sprite_yoga_straps_page.add_to_cart_set_8_foot(1)
    set_of_sprite_yoga_straps_page.is_visible_success_message()
    set_of_sprite_yoga_straps_page.check_nr_of_items_in_cart(1)
    # add 3 sets to cart
    set_of_sprite_yoga_straps_page.add_to_cart_set_8_foot(3)
    set_of_sprite_yoga_straps_page.is_visible_success_message()
    set_of_sprite_yoga_straps_page.check_nr_of_items_in_cart(4)


@allure.feature("Gear catalog > Fitness Equipment")
@allure.title("Block “More information” contains description of material for this item")
@allure.link("https://trello.com/c/V6O1wFcf")
def test_check_additional_info():
    set_of_sprite_yoga_straps_page.visit()
    set_of_sprite_yoga_straps_page.open_window_more_info()
    set_of_sprite_yoga_straps_page.check_details_about_material("Canvas, Plastic")


@allure.feature("Gear catalog > Fitness Equipment")
@allure.title("Check the application of discount for amount of more than 200 $")
@allure.link("https://trello.com/c/icLePPJ7")
def test_application_of_discount_amount_more_200():
    set_of_sprite_yoga_straps_page.visit()
    set_of_sprite_yoga_straps_page.add_to_cart_set_6_foot(6)
    set_of_sprite_yoga_straps_page.add_to_cart_set_8_foot(6)
    set_of_sprite_yoga_straps_page.add_to_cart_set_10_foot(6)
    set_of_sprite_yoga_straps_page.check_nr_of_items_in_cart(18)
    women_page.open_minicart()
    set_of_sprite_yoga_straps_page.open_link_view_and_edit_cart()
    set_of_sprite_yoga_straps_page.check_discount_amount_more_200()
