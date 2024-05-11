import allure
from selene import browser
from data.links import *
from pages.locators import TrainingPageLocators as TPL
from pages.training_page import TrainingPage


class TestTrainingPage:
    @allure.feature("Training page")
    @allure.link("https://trello.com/c/sQZTeeBf")
    @allure.title('Verify clickability and visibility of the "Video Download" link')
    def test_verify_clickability_visibility_video_download_link(self):
        page = TrainingPage(browser=browser)
        page.visit(TRAINING_PAGE_URL)
        page.check_clickability_link()
        page.check_visibility_link()

    @allure.feature("Training page")
    @allure.title("Category Video Download>Check the redirection to the Video Download page.")
    def test_check_the_redirection_to_the_video_download_page(self):
        page = TrainingPage(browser=browser)
        page.visit(TRAINING_PAGE_URL)
        page.click_video_download_link()
        page.assert_text_of_element(TPL.VIDEO_DOWNLOAD_TRAINING_TITLE, 'Video Download')

    @allure.feature("Training page")
    @allure.title('Block-promo training-main>Verify visibility "Block 1"')
    def test_verify_visibility_block_1(self):
        page = TrainingPage(browser=browser)
        page.visit(TRAINING_PAGE_URL)
        page.assert_visible_of_element(TPL.BLOCK_1)

    @allure.feature("Training page")
    @allure.title('Block-promo training-main>Verify Block1 consists text')
    def test_verify_block1_consists_text(self):
        page = TrainingPage(browser=browser)
        page.visit(TRAINING_PAGE_URL)
        found_texts, expected_text = page.verify_block_text()
        assert expected_text == found_texts

    @allure.feature("Training page")
    @allure.title('Block-promo training-main>Verify Block1 dimensions')
    def test_verify_block1_consists_text(self):
        page = TrainingPage(browser=browser)
        page.visit(TRAINING_PAGE_URL)
        Height, Width = page.check_size()
        assert Height, Width
