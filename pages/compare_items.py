from pages.locators import *
from pages import sign_in
from selene import browser, be, have, by, query
from selene.support.shared.jquery_style import s, ss
from data.page_data import *

login_url = LoginLocators()
user_email = SignInData()
user_password = SignInData()
sale_page_section = SalePageLocators()
jacket_sale_women_section = SaleWomenDealsLocators()


def compare_items_values_in_empty_compare_items_section():
    browser.open(LoginLocators.LINK_LOGIN)
    sign_in.login(SignInData.email, SignInData.password)
    browser.element(SalePageLocators.SALE_TAB).click()
    s(by.text("You have no items to compare.")).should(be.visible)
    s(SaleWomenDealsLocators.JACKETS).click()
    s(SaleWomenDealsLocators.ELEMENT_ONE).hover()
    s(SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE).hover().click()
    s(SaleWomenDealsLocators.ELEMENT_TWO).should(be.visible)
    s(SaleWomenDealsLocators.ELEMENT_TWO).hover()
    s(SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).should(be.visible)
    s(SaleWomenDealsLocators.ADD_TO_COMPARE_BTN_ONE_TWO).should(be.clickable).hover().click()
    s(SaleWomenDealsLocators.QUANTITY_ITEMS).should(have.text("2 items"))


def clear_compare_product_section_after_test():
    s(by.id("compare-clear-all")).should(be.visible).click()
    s(by.css("button[class='action-primary action-accept']")).should(be.visible)
    s(by.css("button[class='action-primary action-accept']")).click()
    s(by.text("You cleared the comparison list.")).should(be.visible)
    s(by.text("You cleared the comparison list.")).should(have.text("You cleared the comparison list."))


def should_be_redirected_to_url_containing(text):
    browser.should(have.url_containing(text))


def should_display_product_name(title):
    try:
        s(f"//a[contains(text(), 'title')]").should(be.visible)
        return True
    except Exception:
        return False


def clear_comparison_list():
    try:
        s('.action.delete').should(be.visible)
        while True:
            s('.action.delete').click()
            s('.action-primary.action-accept').wait_until(be.visible)
            s('.action-primary.action-accept').click()
            s('.message-success.success message').wait_until(be.visible)
            if s('a.action.compare span.counter.qty').get(query.text) == '0 items':
                break
    except Exception:
        pass



    #         product_lst = ss('.action.delete')
    # for btn in product_lst:
    #     btn.click()
    #     s('.action-primary.action-accept').wait_until(be.visible)
    #     s('.action-primary.action-accept').click()
    #     s('.message-success.success message').wait_until(be.visible)

