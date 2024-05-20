from selene import be, have, query, browser
from selene.support.shared.jquery_style import s
from pages.locators import TrainingPageLocators as TPLoc
from data.page_data import TrainingPageData as TPdata

url = 'https://magento.softwaretestingboard.com/training.html'


def open():
    browser.open(url)


def should_be_have_text(expected_text):
    s(TPLoc.VIDEO_DOWNLOAD_TRAINING_TITLE).should(have.text(expected_text))


def element_should_be_visible():
    s(TPLoc.BLOCK_1).should(be.visible)


def check_clickability_link():
    return s(TPLoc.VIDEO_DOWNLOAD_LINK).should(be.clickable)


def check_visibility_link():
    return s(TPLoc.VIDEO_DOWNLOAD_LINK).should(be.visible)


def click_video_download_link():
    return s(TPLoc.VIDEO_DOWNLOAD_LINK).click()


def block_targeting():
    return s(TPLoc.BLOCK_1).hover()


def verify_block_contains_text():
    expected_text = TPdata.block_promo_contains
    found_texts = []
    for text in expected_text:
        if s(TPLoc.CONTENT_BLOCK_1).should(have.text(text)):
            found_texts.append(text)
    return found_texts, expected_text


def verify_element_size(expected_height, expected_width):
    s(TPLoc.IMG_BLOCK_1).should(have.css_property('height').value(expected_height))
    s(TPLoc.IMG_BLOCK_1).should(have.css_property('width').value(expected_width))


def verify_element_contains_image():
    return s(TPLoc.IMG_BLOCK_1).get(query.attribute('src'))
