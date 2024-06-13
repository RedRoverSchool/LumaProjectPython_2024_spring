import allure
from pages import argus_allweather_page


@allure.feature('Argus All-Weather Tank')
@allure.link('https://trello.com/c/dzrER7dp')
@allure.title('Check whether the product name, its price and photo are displayed')
def test_argus_all_weather_tank_page_visibility_of_product_name_price_photo(login):
    argus_allweather_page.open_page()
    argus_allweather_page.check_title()
    argus_allweather_page.check_price()
    argus_allweather_page.check_image()
