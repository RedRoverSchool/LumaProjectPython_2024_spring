from selene import be, have
from selene.support.shared.jquery_style import s
from pages.base_page import BasePage
from pages.locators import TrainingPageLocators as TPLoc
from data.page_data import TrainingPageData as TPdata


class TrainingPage(BasePage):

    @staticmethod
    def check_clickability_link():
        return s(TPLoc.VIDEO_DOWNLOAD_LINK).should(be.clickable)

    @staticmethod
    def check_visibility_link():
        return s(TPLoc.VIDEO_DOWNLOAD_LINK).should(be.visible)

    @staticmethod
    def click_video_download_link():
        return s(TPLoc.VIDEO_DOWNLOAD_LINK).click()

    def block_targeting(self):
        return s(TPLoc.BLOCK_1).hover()

    def verify_block_text(self):
        expected_text = TPdata.block_promo_contains
        found_texts = []
        for text in expected_text:
            if s(TPLoc.CONTENT_BLOCK_1).should(have.text(text)):
                found_texts.append(text)
        return found_texts, expected_text

    def check_size(self, expected_height, expected_width):
        s(TPLoc.IMG_BLOCK_1).should(have.css_property('height').value(expected_height))
        s(TPLoc.IMG_BLOCK_1).should(have.css_property('width').value(expected_width))
