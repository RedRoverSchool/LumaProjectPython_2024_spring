from selene import be
from selene.support.shared.jquery_style import s

from pages.base_page import BasePage
from pages.locators import TrainingPageLocators


class TrainingPage(BasePage):

    @staticmethod
    def check_clickability_link():
        return s(TrainingPageLocators.VIDEO_DOWNLOAD_LINK).should(be.clickable)

    @staticmethod
    def check_visibility_link():
        return s(TrainingPageLocators.VIDEO_DOWNLOAD_LINK).should(be.visible)

    @staticmethod
    def click_video_download_link():
        return s(TrainingPageLocators.VIDEO_DOWNLOAD_LINK).click()
