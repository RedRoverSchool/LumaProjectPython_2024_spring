import allure
from selene import browser
from selene.support.conditions import have, be

from pages.main_page import MainPage
from data.page_data import MainPageData


@allure.feature("Main Page > New Luma Yoga Collection")
@allure.title("Verify displays of the 'New Luma Yoga Collection' block")
@allure.link("https://trello.com/c/rKXY69Mo")
def test_displays_of_new_luma_yoga_collection_block():
    main_page = MainPage(browser=browser)
    main_page.open_page()
    main_page.new_luma_yoga_collection_block.should(be.visible)
    main_page.new_luma_yoga_collection_block_info_text.should(
        have.text(MainPageData.new_luma_yoga_collection_block_info_text))
