from pages import add_to_cartLK



def test_cart_icon_view_and_edit_cart():
    add_to_cartLK.open_main_page()
    add_to_cartLK.click_title_item()
    add_to_cartLK.click_size_button()
    add_to_cartLK.click_color_button()
    add_to_cartLK.click_add_to_cart_button()
    add_to_cartLK.click_cart_icon2()
    add_to_cartLK.assert_view_and_edit_cart_blue_text_visibility()
