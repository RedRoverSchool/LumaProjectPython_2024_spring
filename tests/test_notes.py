import allure
from selene import browser
from pages.main_page import main_page_link, notes_link
from pages import notes

practice_api_link = 'https://softwaretestingboard.com/practice-api-testing-using-magento-2/'


@allure.feature('Footer > Notes')
@allure.link('https://trello.com/c/DIZ062AG')
@allure.title('Verify the click on the "PRACTICE API TESTING USING MAGENTO 2" link redirects to the corresponding page')
def test_clickability_and_redirection_practice_api_link():
    notes.visit(main_page_link)
    notes_link.click()
    browser.switch_to_next_tab()
    notes.practice_api_link_click()
    notes.is_current_url_practice_api(practice_api_link)
    notes.verify_header_text('Practice API Testing using Magento 2')
