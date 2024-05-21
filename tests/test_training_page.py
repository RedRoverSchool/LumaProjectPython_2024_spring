import allure
from pages import training_page


@allure.feature("Training page")
@allure.title('Verify clickability and visibility of the "Video Download" link')
def test_verify_clickability_visibility_video_download_link():
    training_page.open()
    training_page.check_clickability_link()
    training_page.check_visibility_link()


@allure.feature("Training page")
@allure.title("Category Video Download>Check the redirection to the Video Download page.")
def test_check_the_redirection_to_the_video_download_page():
    training_page.open()
    training_page.click_video_download_link()
    training_page.should_be_have_text('Video Download')


@allure.feature("Training page")
@allure.title('Block-promo training-main>Verify visibility "Block 1"')
def test_verify_visibility_block_1():
    training_page.open()
    training_page.element_should_be_visible()


@allure.feature("Training page")
@allure.title('Block-promo training-main>Verify Block1 consists text')
def test_verify_block1_consists_text():
    training_page.open()
    found_texts, expected_text = training_page.verify_block_contains_text()
    assert expected_text == found_texts


@allure.feature("Training page")
@allure.title('Block-promo training-main>Verify Block1 dimensions')
def test_verify_block1_consists_text():
    training_page.open()
    training_page.verify_element_size('372px', '1280px')


@allure.feature("Training page")
@allure.title('Block-promo training-main>Verify the picture format')
def test_verify_the_picture_format():
    training_page.open()
    assert '.jpg' in training_page.verify_element_contains_image()
