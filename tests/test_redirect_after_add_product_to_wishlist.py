import allure
from selene import browser
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.action_chains import ActionChains

url = "https://magento.softwaretestingboard.com/what-is-new.html"

@allure.link('https://trello.com/c/jgLmzBZX/296-tc006004005-whats-new-eco-collection-new')
def test_add_product_to_wishlist_as_non_logged_in_user():

    browser.open(url)
    button = s("span.more.button")
    button.should(be.visible)
    button.click()
    product = ss('.product-item-info').first()
    browser.driver.execute_script("arguments[0].scrollIntoView(true);", product)
    ActionChains(browser.driver).move_to_element(product).perform()
    s("[aria-label='Add to Wish List']").click()

    s("span.base[data-ui-id='page-title-wrapper']").should(have.text("Customer Login"))
    s("div[data-bind='html: $parent.prepareMessageForHtml(message.text)']").should(have.text("You must login or register to add items to your wishlist."))
