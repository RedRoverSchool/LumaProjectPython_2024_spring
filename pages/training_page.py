from selene import be
from selene.support.shared.jquery_style import s
from pages.locators import TrainingPageLocators


def check_clickability_link():
    s(TrainingPageLocators.VIDEO_DOWNLOAD_LINK).should(be.clickable)


def check_visibility_link():
    s(TrainingPageLocators.VIDEO_DOWNLOAD_LINK).should(be.visible)
