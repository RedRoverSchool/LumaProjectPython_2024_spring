from selene import browser, have
from selene.support.conditions import be
from selene.support.shared.jquery_style import s

create_an_account_link = s("(//a[.='Create an Account'])[1]")
gear_page_url = 'https://magento.softwaretestingboard.com/gear.html'


def open_page():
    browser.open(gear_page_url)


def should_be_clickable_create_account():
    create_an_account_link.should(be.clickable)


def has_create_account_text():
    create_an_account_link.should(have.text('Create an Account'))
