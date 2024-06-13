import allure
from pages import women_page, product, cart, wish_list, compare_items


@allure.feature('Sale > Tees-women')
@allure.title('Breadcrumbs are visible and correct')
@allure.link('https://trello.com/c/fhLdyS1l')
def test_women_tees_breadcrumbs_is_correct():
    women_page.visit_women_tee()
    women_page.check_if_breadcrumbs_have_all_parts()


@allure.feature('Sale > Tees-women')
@allure.title('Breadcrumbs redirects to the correct page')
@allure.link('https://trello.com/c/B29UMcGd')
def test_breadcrumbs_nr_of_links_from_women_tees():
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs()


@allure.feature('Sale > Tees-women')
@allure.title('Breadcrumbs redirects to the correct page')
@allure.link('https://trello.com/c/B29UMcGd')
def test_breadcrumbs_nr_of_links_from_women_tees_var2():
    # test another method
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs_by_count()


@allure.feature('Sale > Tees-women')
@allure.title('Breadcrumbs redirects to the correct page ')
@allure.link('https://trello.com/c/B29UMcGd')
def test_breadcrumbs_redirection_from_women_tees_var3():
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr()


# @pytest.mark.skip
@allure.feature('Radiant Tee product page > Add to cart')
@allure.title('Adding the product to cart')
@allure.link('https://trello.com/c/xGtHnQaq/')
def test_adding_product_to_cart(login):
    cart.clear_cart()
    product.open('radiant-tee')
    product.add_to_cart_with_qty("M", "Blue", "2")
    cart.click_cart_icon()
    cart.product_in_minicart_should_have_name('Radiant Tee')
    cart.minicart_quantity_should_be_equal('2')
    cart.minicart_subtotal_should_be_calculated_with_qty_equal('2')
    cart.delete_product_from_cart()


@allure.feature('Radiant Tee product page')
@allure.title('Visibility of product name, price and photo')
@allure.link('https://trello.com/c/SKLAh5ku/')
def test_product_name_price_img_visibility(login):
    product.open('radiant-tee')
    product.title_should_have_text('Radiant Tee')
    product.price_should_be_equal('22')
    product.img_should_have_name('Radiant Tee')


@allure.feature('Radiant Tee product page')
@allure.link('https://trello.com/c/mtsK5CPx')
@allure.title('Quantity of items added to cart')
def test_product_quantity_added_to_cart(login):
    cart.clear_cart()
    product.open('radiant-tee')
    product.add_to_cart_with_qty("M", "Blue", "2")
    cart.click_cart_icon()
    cart.minicart_quantity_should_be_equal('2')
    cart.counter_should_be_equal('2')
    cart.minicart_subtotal_should_be_calculated_with_qty_equal('2')
    cart.delete_product_from_cart()


@allure.feature('Radiant Tee product page')
@allure.link('https://trello.com/c/EXhjde1P')
@allure.title('Visibility of the product description and detailed information')
def test_visibility_of_product_description(login):
    product.open('radiant-tee')
    product.details_should_contain_text('Radiant Tee')
    product.more_information_tab_should_contain_text('Tee', 'Cotton', 'Solid', 'Indoor')


@allure.feature('Radiant Tee product page')
@allure.link('https://trello.com/c/5xoWR2Ef/')
@allure.title('Changing the product size')
def test_changing_product_size(login):
    product.open('radiant-tee')
    product.select_size('XS')
    product.select_size('M')
    product.size_should_be_selected('M', 'true')
    product.size_label_should_have_frame_with_color('M', '#ff5501')
    product.size_indicator_should_have_text('M')


@allure.feature('Radiant Tee product page')
@allure.link('https://trello.com/c/IR9y4zwY/')
@allure.title('Adding the product to the wish list')
def test_adding_product_to_wish_list(login):
    product.open('radiant-tee')
    product.add_to_wish_list()
    wish_list.url_should_contain('wishlist')
    wish_list.success_adding_msg_should_have_text('Radiant Tee')
    wish_list.product_should_have_title('Radiant Tee')


@allure.feature('Radiant Tee product page > Reviews')
@allure.link('https://trello.com/c/PChP2lY4')
@allure.title('Reviews visibility')
def test_product_reviews_visibility(login):
    product.open('radiant-tee')
    product.click_reviews_tab()
    product.reviews_should_have_title('Customer Reviews', 'Radiant Tee')


@allure.feature('Radiant Tee product page')
@allure.link('https://trello.com/c/7Mn9d8Z4/')
@allure.title('Adding the product to the comparison list')
def test_adding_product_to_comparison_list(login):
    product.open('radiant-tee')
    product.add_to_comparison_list()
    product.add_to_compare_success_msg_should_gave_text('Radiant Tee')
    product.click_to_comparison_list_link()
    compare_items.should_be_redirected_to_url_containing('product_compare')
    compare_items.should_display_product_name('Radiant Tee')
    compare_items.clear_comparison_list()


@allure.feature('Radiant Tee product page > Reviews')
@allure.link('https://trello.com/c/R6TsIcuW')
@allure.title('Writing the product review')
def test_product_reviews_writing(login):
    product.open('radiant-tee')
    product.click_reviews_tab()
    product.put_review_stars('4')
    product.fill_nickname_field_with_text('Lena')
    product.fill_summary_field_with_text('Very comfortable')
    product.fill_review_field_with_text('Great! Soft and beautiful')
    product.submit_review()
    product.success_msg_should_have_text('You submitted your review for moderation.')


@allure.feature('Radiant Tee product page > Product parameters')
@allure.link('https://trello.com/c/Ik5u2Zsm')
@allure.title('Changing the product color')
def test_changing_product_color(login):
    product.open('radiant-tee')
    product.select_color('Blue')
    product.select_color('Orange')
    product.color_should_be_selected('Orange', 'true')
    product.color_label_should_have_frame_with_color('Orange', '#ff5501')
    product.color_indicator_should_have_text('Orange')
    product.image_should_have_color('orange')
