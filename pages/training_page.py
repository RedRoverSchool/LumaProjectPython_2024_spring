from selene import be, have, query, browser
from selene.support.shared.jquery_style import s
from data.page_data import TrainingPageData as TPdata

url = 'https://magento.softwaretestingboard.com/training.html'

video_download_link = s('#narrow-by-list2 li a')
video_download_training_title = s('span[data-ui-id="page-title-wrapper"')
block_1 = s('.blocks-promo a:first-child')
content_block_1 = s('.blocks-promo a:first-child .title')
img_block_1 = s('a[class="block-promo training-main"] img')


def open():
    browser.open(url)


def should_be_have_text(expected_text):
    video_download_training_title.should(have.text(expected_text))


def element_should_be_visible():
    block_1.should(be.visible)


def check_clickability_link():
    return video_download_link.should(be.clickable)


def check_visibility_link():
    return video_download_link.should(be.visible)


def click_video_download_link():
    return video_download_link.click()


def block_targeting():
    return block_1.hover()


def verify_block_contains_text():
    expected_text = TPdata.block_promo_contains
    found_texts = []
    for text in expected_text:
        if content_block_1.should(have.text(text)):
            found_texts.append(text)
    return found_texts, expected_text


def verify_element_size(expected_height, expected_width):
    img_block_1.should(have.css_property('height').value(expected_height))
    img_block_1.should(have.css_property('width').value(expected_width))


def verify_element_contains_image():
    return img_block_1.get(query.attribute('src'))
