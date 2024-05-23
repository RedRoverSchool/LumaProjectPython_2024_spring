import allure
import pages.argus_allweather_page as PA

@allure.suite('US_002.001 | Page of any product')
@allure.link('https://trello.com/c/dzrER7dp')
@allure.title('TC_002.001.012 I Argus All-Weather Tank> Check whether the product name, its price and photo are displayed')
def test_argus_allweather_tank_page_visibility_of_product_name_price_photo(login):
    PA.open_page()
    PA.check_title()
    PA.check_price()
    PA.check_image()
