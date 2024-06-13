import allure

from pages import redirect_inside_cart


@allure.feature('Main page > Cart')
@allure.title('User redirected inside the cart')
@allure.link('https://trello.com/c/BCAxPhUO')
def test_redirect_inside_cart():
    redirect_inside_cart.open_main_page()
    redirect_inside_cart.click_title_item()
    redirect_inside_cart.click_size_button()
    redirect_inside_cart.click_color_button()
    redirect_inside_cart.click_add_to_cart_button()
    redirect_inside_cart.click_cart_icon2()
    redirect_inside_cart.assert_view_and_edit_cart_blue_text()
    redirect_inside_cart.should_be_have_current_url()
