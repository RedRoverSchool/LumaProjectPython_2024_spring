import allure
from pages import training_page
from data.links import *


@allure.feature("Training page")
@allure.link("https://trello.com/c/sQZTeeBf")
@allure.title('Verify clickability and visibility of the "Video Download" link')
def test_verify_clickability_visibility_video_download_link(visit_page):
    visit_page(TRAINING_PAGE_URL)
    training_page.check_clickability_link()
    training_page.check_visibility_link()
