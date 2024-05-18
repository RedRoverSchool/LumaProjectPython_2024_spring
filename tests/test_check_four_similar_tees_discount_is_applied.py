from pages import tees_page
import pytest


@pytest.mark.skip
def test_four_tees_discount_is_apply_for_similar_tees(browser_management):
    tees_page.check_four_similar_tees_discount_is_applies()
