from selene import command, be, query
from selene import have
from selene.support.shared.jquery_style import s, ss
from pages.locators import Compare


def choose_to_compare_item_nr(nr):
    s(f'li:nth-child({nr}) a.action.tocompare').perform(command.js.click)


def collect_item_names_to_be_compared():
    lst = []
    item1 = s('li:nth-child(1) strong > a')
    lst.append(item1.get(query.attribute("text")).strip())
    item2 = s('li:nth-child(2) strong > a')
    lst.append(item2.get(query.attribute("text")).strip())
    item3 = s('li:nth-child(3) strong > a')
    lst.append(item3.get(query.attribute("text")).strip())
    return lst


def should_be_3_items_to_compare():
    s(Compare.QTY_IN_COMPARE_LIST).should(be.visible).perform(command.js.scroll_into_view)
    s(Compare.QTY_IN_COMPARE_LIST).should(have.text('3 items'))


def button_compare_is_clickable():
    s(Compare.BUTTON_PUT_TO_COMPARE).should(be.clickable).perform(command.js.scroll_into_view)
    s(Compare.BUTTON_PUT_TO_COMPARE).should(have.text('Compare'))


def link_clearall_is_clickable():
    s(Compare.BUTTON_CLEAR_FROM_COMPARE).should(be.visible).perform(command.js.scroll_into_view)
    s(Compare.BUTTON_CLEAR_FROM_COMPARE).should(have.text('Clear All'))


def collect_items_list_compare():
    collection_to_compare = ss(Compare.PRODUCT_ITEM)
    list_to_compare = []
    for item in collection_to_compare:
        list_to_compare.append(item.get(query.attribute("text")))
    lst = list_to_compare[::-1]
    # print(lst)
    return lst
