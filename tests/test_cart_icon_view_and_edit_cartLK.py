from pages import redirect_inside_cart_LK


def test_cart_icon_view_and_edit_cart():
    redirect_inside_cart_LK.open_main_page()
    redirect_inside_cart_LK.click_title_item()
    redirect_inside_cart_LK.click_size_button()
    redirect_inside_cart_LK.click_color_button()
    redirect_inside_cart_LK.click_add_to_cart_button()
    redirect_inside_cart_LK.click_cart_icon2()
    redirect_inside_cart_LK.assert_view_and_edit_cart_blue_text_visibility()

