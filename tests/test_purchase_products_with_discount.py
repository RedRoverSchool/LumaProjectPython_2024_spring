import allure
from selene import browser
from selene.support.conditions import have

from pages.main_page import MainPage


@allure.link('https://trello.com/c/9c2BadPx')
@allure.suite("US_011.013 | Sale > 20% OFF: Purchase of goods with a 20% discount")
class TestPurchaseOfGoodsWithDiscount:
    @allure.feature(" Sale > 20% OFF: Purchase of goods with a 20% discount")
    def test_sale_off_purchase_of_goods_with_discount(self):
        with allure.step("Open main page and check if load successfully"):
            page = MainPage(browser=browser)
            page.open_page()
            page.is_loaded()
        with (allure.step("Add to products item to card until sub total > 200")):
            products = page.find_products()
            page.scroll_to_hot_sellers()
            size = len(products)
            count = 0
            for i in range(0, size):
                page.add_product_to_cart(products[i])
                count += 1
                page.find_counter_number().should(have.text(str(count)))
            page.find_counter_number().should(have.text(str(count)))
        with (allure.step("Go to checkout card with products item")):
            card = page.goto_card_page()
            print(card.get_cart_totals())
