from selene import browser, have
from selene.support.conditions import be
from selene.support.shared.jquery_style import s

create_an_account_link = s("(//a[.='Create an Account'])[1]")
base_url = 'https://magento.softwaretestingboard.com/'
gear_page_url = base_url + 'gear.html'
gear_bags_url = base_url + 'gear/bags.html'
gear_fitness_url = base_url + 'gear/fitness-equipment.html'
gear_watches_url = base_url + 'gear/watches.html'


def open_page():
    browser.open(gear_page_url)


def should_be_clickable_create_account():
    create_an_account_link.should(be.clickable)


def has_create_account_text():
    create_an_account_link.should(have.text('Create an Account'))


def open_gear_bags_page():
    browser.open(gear_bags_url)


def visit(link):
    browser.open(link)

