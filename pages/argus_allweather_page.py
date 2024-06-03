from selene import browser, have, be
from selene.support.shared.jquery_style import s

argus_all_weather_tank_url = 'https://magento.softwaretestingboard.com/argus-all-weather-tank.html'

argus_all_weather_tank_product_name = 'Argus All-Weather Tank'

product_price_base = s('//*[@class="price"]')
product_image_base = s('//img[@class="fotorama__img"]')
product_title = s('span[data-ui-id="page-title-wrapper"]')


def open_page():
    browser.open(argus_all_weather_tank_url)


def check_title():
    product_title.should(have.text(argus_all_weather_tank_product_name))


def check_price():
    product_price_base.should(be.present)


def check_image():
    product_image_base.should(be.present)