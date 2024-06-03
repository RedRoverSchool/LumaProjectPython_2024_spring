from selene import Element
from selene.support.conditions import have, be
from selene.support.shared.jquery_style import s, ss


men_page_url = 'https://magento.softwaretestingboard.com/men.html'
men_sub_urls = {
    'Tops': 'https://magento.softwaretestingboard.com/men/tops-men.html',
    'Bottoms': 'https://magento.softwaretestingboard.com/men/bottoms-men.html'
}

men_top_urls = {
    "Jackets": 'https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html',
    "Hoodies & Sweatshirts": 'https://magento.softwaretestingboard.com/men/tops-men/hoodies-and-sweatshirts-men.html',
    "Tees": 'https://magento.softwaretestingboard.com/men/tops-men/tees-men.html',
    "Tanks": 'https://magento.softwaretestingboard.com/men/tops-men/tanks-men.html'
}

men_bottoms_urls = {
    "Pants": 'https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html',
    "Shorts": 'https://magento.softwaretestingboard.com/men/bottoms-men/shorts-men.html'
}


men_link = s('#ui-id-5')
men_tops = s('#ui-id-17')
men_bottoms = s('#ui-id-18')
header = s("#page-title-heading")
submenus = s("li[class='level1 nav-3-1 category-item first parent ui-menu-item']")
submenus_bottom = s("li[class='level1 nav-3-2 category-item last parent ui-menu-item']")
men_tops_submenu_hrefs = ss(".nav-3-1 > ul  > li > a")
men_bottoms_submenu_hrefs = ss(".nav-3-2 > ul  > li > a")


def is_have_text(locator, value):
    locator.should(have.text(value))


def goto_men_page():
    men_link.click()


def click_to(locator):
    s("//li[contains(@class, 'nav-3')]/a[@role='menuitem']/span[text()='{}']".format(locator)).click()


def is_clickable(locator: Element, url: str):
    locator.should(be.clickable)
    locator.should(have.attribute("href").value(url))


def is_have_header(text):
    header.should(have.text(text))


def verify_sub_men_tops():
    submenus.should(be.visible)
    for expected_element in list(men_top_urls.keys()):
        submenus.should(have.text(expected_element))


def verify_sub_men_bottoms():
    submenus_bottom.should(be.visible)
    for expected_element in list(men_bottoms_urls.keys()):
        submenus_bottom.should(have.text(expected_element))


def verify_dropdown_menu():
    verify_nav_mens_tops()
    verify_nav_mens_bottoms()


def verify_nav_men():
    verify_nav(men_link, 'Men')
    is_clickable(men_link, men_page_url)


def verify_nav_mens_tops():
    verify_nav(men_tops, 'Tops')
    is_clickable(men_tops, men_sub_urls['Tops'])


def verify_nav_mens_bottoms():
    verify_nav_mens(men_bottoms, 'Bottoms')
    is_clickable(men_bottoms, men_sub_urls['Bottoms'])


def verify_nav_mens(element, nav):
    verify_nav(element, nav)
    is_clickable(element, men_sub_urls[nav])


def verify_nav(element: Element, title: str):
    element.should(be.present)
    element.should(be.visible)
    is_have_text(element, title)


def verify_sub_men_tops_href_elements():
    for i, element in enumerate(men_tops_submenu_hrefs):
        verify_nav(element, list(men_top_urls.keys())[i])
        is_clickable(element, list(men_top_urls.values())[i])


def verify_sub_men_bottoms_href_elements():
    for i, element in enumerate(men_bottoms_submenu_hrefs):
        verify_nav(element, list(men_bottoms_urls.keys())[i])
        is_clickable(element, list(men_bottoms_urls.values())[i])
