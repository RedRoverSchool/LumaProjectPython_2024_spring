from selene import browser, have, be
from selene.support.shared.jquery_style import s

import data.links as DL
from pages.locators import ProductLocators as PL


def open_page():
    browser.open(DL.ARGUS_ALL_WEATHER_TANK_URL)

def check_title():
    s(PL.PRODUCT_TITLE).should(have.text(PL.ARGUS_ALL_WEATHER_TANK_PRODUCT_NAME_TEXT))

def check_price():    
    s(PL.PRODUCT_PRICE_BASE).should(be.present)
    
def check_image():
    s(PL.PRODUCT_IMAGE_BASE).should(be.present)