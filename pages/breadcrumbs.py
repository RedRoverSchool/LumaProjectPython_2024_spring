from selene import browser, be, have
from selene.support.shared.jquery_style import s

url = 'https://magento.softwaretestingboard.com'
nav_women = '#ui-id-4'
nav_tops = '#ui-id-9'
nav_jackets = '#ui-id-11'
women_crumb = '//li[@class = "item category20"]'
breadcrumbs = '//ul[@class = "items"]'

def open_page():
    browser.open(url)

def nav_women_tops_jackets():
    s(nav_women).hover()
    s(nav_tops).hover()
    s(nav_jackets).hover().click()

def click_to_women_crumb():
    s(women_crumb).click()

def is_visible():
    s(breadcrumbs).should(be.visible)
    s(women_crumb).should(have.text('Women'))
