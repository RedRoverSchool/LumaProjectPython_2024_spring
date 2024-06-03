import time

import allure
from pages import compare_side_panel
import pytest


# @pytest.mark.skip
@allure.link("https://trello.com/c/hSe3gPsx")
def test_11_005_003_check_items_in_list_for_compare():
    compare_side_panel.visit_women_jackets()
    items_to_be_compared = compare_side_panel.collect_item_names_to_be_compared()
    compare_side_panel.choose_to_compare_item_nr(1)
    compare_side_panel.choose_to_compare_item_nr(2)
    compare_side_panel.choose_to_compare_item_nr(3)
    compare_side_panel.visit_sale()
    time.sleep(2)
    compare_side_panel.should_be_3_items_to_compare()
    compare_side_panel.button_compare_is_clickable()
    compare_side_panel.link_clearall_is_clickable()
    compared_items = compare_side_panel.collect_items_list_compare()
    assert items_to_be_compared == compared_items

