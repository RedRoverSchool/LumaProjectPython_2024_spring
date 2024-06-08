import allure
from pages import breadcrumbs


@allure.link('https://trello.com/c/s9FJicG5')
@allure.feature('Breadcrumbs')
@allure.title('Verify that the breadcrumbs displayed and clickable')
def test_breadcrumbs():
    breadcrumbs.open_page()
    breadcrumbs.nav_women_tops_jackets()
    breadcrumbs.click_to_women_crumb()
    breadcrumbs.is_visible()
