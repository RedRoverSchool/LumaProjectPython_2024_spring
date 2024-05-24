import allure
from pages import women_page, product, cart, wish_list


@allure.link('https://trello.com/c/fhLdyS1l')
def test_011_016_001_women_tees_breadcrumbs_is_correct():
    women_page.visit_women_tee()
    women_page.check_if_breadcrumbs_have_all_parts()


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_nr_of_links_from_women_tees():
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs()


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_nr_of_links_from_women_tees_var2():
    # test another method
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs_by_count()


@allure.link('https://trello.com/c/B29UMcGd')
def test_011_016_002_breadcrumbs_redirection_from_women_tees_var3():
    women_page.visit_women_tee()
    women_page.check_nr_of_links_from_women_tee_by_breadcrumbs_by_get_attr()


@allure.suite('US_002.001 | Page of any product')
@allure.title('TC_002.001.002 | Radiant Tee product page > Add to cart > Adding the product to cart')
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


@allure.suite('US_002.001 | Page of any product')
@allure.title('TC_002.001.001 | Radiant Tee product page > Visibility of product name, price and photo')
@allure.link('https://trello.com/c/SKLAh5ku/')
def test_product_name_price_img_visibility(login):
    product.open('radiant-tee')
    product.title_should_have_text('Radiant Tee')
    product.price_should_be_equal('22')
    product.img_should_have_name('Radiant Tee')


@allure.suite('US_002.001 | Page of any product')
@allure.link('https://trello.com/c/mtsK5CPx')
@allure.title('TC_002.001.003 | Radiant Tee product page > Quantity of items> Quantity of items added to cart')
def test_product_quantity_added_to_cart(login):
    cart.clear_cart()
    product.open('radiant-tee')
    product.add_to_cart_with_qty("M", "Blue", "2")
    cart.click_cart_icon()
    cart.minicart_quantity_should_be_equal('2')
    cart.counter_should_be_equal('2')
    cart.minicart_subtotal_should_be_calculated_with_qty_equal('2')
    cart.delete_product_from_cart()


@allure.suite('US_002.001 | Page of any product')
@allure.link('https://trello.com/c/EXhjde1P')
@allure.title(
    'TC_002.001.004 | Radiant Tee product page > Visibility of the product description and detailed information')
def test_visibility_of_product_description(login):
    product.open('radiant-tee')
    product.details_should_contain_text('Radiant Tee')
    product.more_information_tab_should_contain_text('Tee', 'Cotton', 'Solid', 'Indoor')


@allure.suite('US_002.001 | Page of any product')
@allure.link('https://trello.com/c/5xoWR2Ef/')
@allure.title('TC_002.001.007 | Radiant Tee product page > Product parameters > Changing the product size')
def test_changing_product_size(login):
    product.open('radiant-tee')
    product.select_size('XS')
    product.select_size('M')
    product.size_should_be_selected('M', 'true')
    product.size_label_should_have_frame_with_color('M', '#ff5501')
    product.size_indicator_should_have_text('M')


@allure.suite('US_002.001 | Page of any product')
@allure.link('https://trello.com/c/IR9y4zwY/')
@allure.title('TC_002.001.009 | Radiant Tee product page > Adding the product to the wish list')
def test_adding_product_to_wish_list(login):
    product.open('radiant-tee')
    product.add_to_wish_list()
    wish_list.url_should_contain('wishlist')
    wish_list.success_adding_msg_should_have_text('Radiant Tee')
    wish_list.product_should_have_title('Radiant Tee')

@allure.suite('US_002.001 | Page of any product')
@allure.link('https://trello.com/c/PChP2lY4')
@allure.title('TC_002.001.005 | Radiant Tee product page > Reviews > Reviews visibility')
def test_product_reviews_visibility(login):
    product.open('radiant-tee')
    product.click_reviews_tab()
    product.reviews_should_have_title('Customer Reviews', 'Radiant Tee')
