from selene import browser


class SalePageLocators:
    GEAR_DEALS_TITLE = "//*[text()='Gear Deals']"
    BAGS_LINK = "//a[text()='Bags']"
    FITNESS_EQUIPMENT_LINK = "//a[text()='Fitness Equipment']"
    LINK_SALE = "https://magento.softwaretestingboard.com/sale.html"
    LINK_WOMEN_SALE = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
    LINK_TEES_WOMEN = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"

    BREADCRUMBS_LINKS_ON_PAGE_TEES = ['https://magento.softwaretestingboard.com/',
                                      'https://magento.softwaretestingboard.com/women.html',
                                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE = ['https://magento.softwaretestingboard.com/',
                                            'https://magento.softwaretestingboard.com/sale.html']

    SALE_TAB = "//*[@id='ui-id-8']"
    BLOCK_PROMO_SALE_20_OFF_TITLE = "a[class='block-promo sale-20-off'] strong[class='title']"
    BLOCK_PROMO_SALE_20_OFF_INFO = "a[class='block-promo sale-20-off'] span[class='info']"
    BLOCK_PROMO_SALE_FREE_SHIPPING_TITLE = "a[class='block-promo sale-free-shipping'] strong[class='title']"
    BLOCK_PROMO_SALE_FREE_SHIPPING_INFO = "a[class='block-promo sale-free-shipping'] span[class='info']"
    BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_TITLE = "a[class='block-promo sale-womens-t-shirts'] strong[class='title']"
    BLOCK_PROMO_SALE_WOMENS_T_SHIRTS_INFO = "a[class='block-promo sale-womens-t-shirts'] span[class='info']"


class ProductLocators:
    RADIANT_TEE_URL = 'https://magento.softwaretestingboard.com/radiant-tee.html'
    RADIANT_TEE_SIZE = '[option-label="XS"]'
    RADIANT_TEE_COLOR = '[option-label="Orange"]'
    RADIANT_TEE_QTY = '#qty'
    ADD_TO_CART_BUTTON = '#product-addtocart-button'
    ADD_TO_CART_BUTTON_FROM_MAINPAGE = 'form[data-product-sku="WS12"] button'

    ARGUS_All_WEATHER_TANK = '[alt="Argus All-Weather Tank"]'
    ARGUS_All_WEATHER_TANK_SIZE = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="M"]'
    ARGUS_All_WEATHER_TANK_COLOR = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="Gray"]'
    ARGUS_All_WEATHER_TANK_ADD_TO_CARD = '//*[@title="Argus All-Weather Tank"]/../..//*[@title="Add to Cart"]'
    MINI_BASKET_WINDOW = '[class="action showcart"]'
    VIEW_AND_EDIT_CART_LINK = "//*[text()='View and Edit Cart']"
    VIEW_AND_EDIT_CART_HREF = "[class='action viewcart']"
    SEE_DETAILS = '[data-role="title"]'
    SIZE_M = '//*[@class="product options list"]//*[text()="M"]'
    COLOR_GRAY = '//*[@class="product options list"]//*[text()="Gray"]'
    NAME_ITEM = '//*[text()="Argus All-Weather Tank"]'
    PRICE_ITEM = '//*[@class="minicart-price"]//*[@class="price"]'
    CART_SUBTOTAL = '.subtotal .price'
    QTY_FIELD = ".details-qty input"
    UPDATE = '[title="Update"]'

    NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART = '//*[@id="shopping-cart-table"] //*[text()="Argus All-Weather Tank"]'
    SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART = '// *[contains(text(), "M")]/../..// *[ @ id = "shopping-cart-table"]'
    COLOR_GRAY_ARGUS_CHECKOUT_CART = '//*[@id="shopping-cart-table"]//*[contains(text(),"Gray")]'
    PRICE_ITEM_CHECKOUT_CART = '//*[@class="col price"] //*[text()="$22.00"]'
    CART_SUBTOTAL_CHECKOUT_CART = '//*[@class="col subtotal"] //*[text()="$22.00"]'
    QTY_FIELD_CHECKOUT_CART = '[class="field qty"] input'

    RADIANT_TEE_LINK = "//a[contains(text(), 'Radiant Tee ')]"
    RADIANT_TEE_IMG = '//div[1]/div[3]/div[1]/img[@alt="Radiant Tee"]'
    RADIANT_TEE_TITLE = 'span[data-ui-id="page-title-wrapper"]'
    RADIANT_TEE_PRICE = '#product-price-1556'
    PRODUCT_PRICE = '//div[2]/main/div[2]/div/div[2]/div[3]/div/span/span/span[2]/span'
    ADDING_TO_CART_SUCCESSFULL_MSG = "//div[contains(text(), 'You added')]"
    SIZE_XS = '#option-label-size-143-item-166'
    COLOR_BLUE = '#option-label-color-93-item-50'
    SHOULD_CHOOSE_SIZE_AND_COLOR = '.swatch-input super-attribute-select'
    TEXT_REQUIRED_FIELD = 'This is a required field.'


class HomeLocators:
    CONSENT_COOKIES_BTN = '(//p[@class="fc-button-label"])[1]'
    COOKIES_MSG = '//h1[@class="fc-dialog-headline"]'
    STORE_LOGO = 'a.logo'
    CART_ICON = 'a.showcart'
    MINICART = '#ui-id-1'
    EMPTY_MINICART_MSG = 'strong[class="subtitle empty"]'
    MINICART_RADIANT_TEE_NAME = "//*[@id='mini-cart']/li/div/div/strong/a[contains(text(), 'Radiant Tee')]"
    MINICART_PRODUCT_QTY = 'input[class="item-qty cart-item-qty"]'
    MINICART_SUBTOTAL = '//*[@id="minicart-content-wrapper"]/div[2]/div[2]/div/span/span'
    MINICART_DELETE_BUTTONS = "a[class='action delete']"
    DELETE_ITEM_CONFIRM_OK = 'button[class="action-primary action-accept"]'
    MINICART_CLOSE = '#btn-minicart-close'
    CART_COUNTER = 'span[class="counter-number"]'
    MINICART_VIEW = '.action.viewcart'
    MINICART_COUNTER = '.counter-label'
    MINI_CART_PRICE = '.price-wrapper'
    AMOUNT_PRICE = ".amount.price-container"
    TO_CART_BUTTON = "button.action.tocart.primary"
    SIZES = ".swatch-attribute.size .swatch-option"
    COLORS = ".swatch-attribute.color .swatch-option"
    TOTALS = 'tr.totals .amount .price'
    SUB_TOTAL = 'tr.totals.sub .amount .price'
    TAX_AMOUNT = 'tr.totals-tax .amount .price'
    GRAND_TOTALS = 'tr.grand.totals .amount .price'


class NavigatorLocators:
    NAV_NEW = '#ui-id-3'
    NAV_WOMEN = '#ui-id-4'
    NAV_MEN = '#ui-id-5'
    NAV_GEAR = '#ui-id-6'
    NAV_TRAINING = '#ui-id-7'
    NAV_SALE = '#ui-id-8'
    NAV_MENU = '#ui-id-2'
    NAV_MEN_TOPS = '#ui-id-17'
    NAV_MEN_BOTTOMS = '#ui-id-18'
    NAV_MEN_TOPS_JACKET = '#ui-id-19'
    NAV_MEN_TOPS_HOODIES = '#ui-id-20'
    NAV_MEN_TOPS_TEES = '#ui-id-21'
    NAV_MEN_TOPS_TANKS = '#ui-id-22'
    NAV_MEN_SUBMENU = "li[class='level1 nav-3-1 category-item first parent ui-menu-item']"
    NAV_MEN_BOTTOMS_SUBMENU = "li[class='level1 nav-3-2 category-item last parent ui-menu-item']"
    NAV_MEN_TOPS_SUBMENU_HREFS = ".nav-3-1 > ul  > li > a"
    NAV_MEN_BOTTOMS_SUBMENU_HREFS = ".nav-3-2 > ul  > li > a"


class SideBarLocators:
    BREADCRUMBS = '.breadcrumbs'
    ITEM_HOME = '.item.home a'
    SIDEBAR_MAIN = '.sidebar.sidebar-main'
    CATEGORIES_MENU = '.categories-menu'
    FILTER = '.block.filter'


class BaseLocators:
    SUCCESS_MESSAGE = '.message-success.success.message'
    PAGE_NAME = ".base"
    PAGE_TITLE = "h1"
    PAGE_HEADER = "#page-title-heading"
    BREADCRUMBS_LIST = ".breadcrumbs li"
    BREADCRUMBS_LINKS = '.breadcrumbs > ul  > li > a'
    BREADCRUMBS = ".breadcrumbs > ul"
    PRIVACY_COOKIE_POLICY_LOCATOR = "//a[contains(@href, 'privacy-policy-cookie')]"
    PRODUCT_ITEM_IN_CATALOG = '.product-item-info'  # каждый товар в целом на любой странице
    PRODUCT_PRICE = '.price-label'
    PRODUCT_NAME = '.product-item-link'
    PRODUCT_IMAGE = '.product-image-photo'
    ALL_URL = ["https://magento.softwaretestingboard.com/",
               "https://magento.softwaretestingboard.com/what-is-new.html",
               "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html,"
               "https://magento.softwaretestingboard.com/training.html"
               ]
    NEW_LUMA_YOGA_COLLECTION_BLOCK_LOCATOR = "//a[contains(@class,'home-main')]/span"
    NEW_LUMA_YOGA_COLLECTION_BLOCK_INFO_TEXT_LOCATOR = "//a[contains(@class,'home-main')]//span[@class='info']"
    ECO_COLLECTION_NAME = "//span[contains (text(), 'Shop Eco Friendly')]"


class SearchTermsLocators:
    LINK_SEARCH_TERMS = "https://magento.softwaretestingboard.com/search/term/popular/"
    TERMS_FOR_SEARCH_LIST_QTY = '[class="item"]'
    LIST_OF_SEARCH_TERMS = '[class="item"] a'


class WomenPageLocators:
    WOMEN_MENU = "//*[@id='ui-id-4']"
    TOPS_LINK = "//*[@id='ui-id-9']"
    TOPS_TITLE = ".page-title-wrapper"
    BOTTOMS_LINK = "//*[@id='ui-id-10']"
    BOTTOMS_TITLE = ".ui-corner-all ui-state-focus"
    DROPDOWN_BLOCK = "//*[@id='ui-id-2']/li[2]/ul"
    TEES_LINK = '//*[@id="ui-id-13"]'


class WhatsNewPageLocators:
    HEADER = 'h1>span'
    LUMAS_LATEST_LIST = '.products-grid>ol'
    LUMAS_LATEST_ITEMS = '.products-grid>ol>li'
    BUTTON_MORE = 'span.more.button'
    LUMAS_LATEST_IMAGES = '.product-image-photo'
    NEW_YOGA_LINK = "//*[text()='New Luma Yoga Collection']"
    BRAS_TANKS = '.categories-menu ul:nth-child(2) li:nth-child(4) a'
    ADD_TO_CART_BUTTON = '//*[@id="product-addtocart-button"]/span'
    ERROR_MASSAGE_UNDER_SIZE = '//*[@id="super_attribute[143]-error"]'
    ERROR_MASSAGE_UNDER_COLOR = '//*[@id="super_attribute[93]-error"]'
    BREATHE_EASY_TANK = "a.product-item-link[href*='breathe-easy-tank']"
    ADD_TO_COMPARE = '.product-social-links a:last-child'
    YOU_ADDED_PRODUCT = '.product-social-links a:last-child'
    ADD_TO_WISH_LIST_BUTTON = '.product-social-links a:first-child'
    ERROR_MASSAGE_YOU_MUST_LOGIN_OR_REGISTER = '//*[@id="maincontent"]/div[2]/div[2]/div/div/div'


class PrivacyPolicyPageLocators:
    PAGE_MAIN_HEADER_LOCATOR = "span[data-ui-id='page-title-wrapper']"


class ProductItemLocators:
    WISH_LIST = "[aria-label='Add to Wish List']"
    PRODUCTS_GRID = ".products-grid.grid"
    ITEM_INFO = ".product-item-info"
    LAYLA_TEE_PRODUCT_NAME = "a[title='Layla Tee']"
    LAYLA_TEE_TITLE = "h1.page-title span"
    LAYLA_TEE_IMG = "img[alt='Layla Tee']"


class LoginPageLocators:
    PAGE_TITLE_WRAPPER = "span.base[data-ui-id='page-title-wrapper']"
    MESSAGE_TEXT = "div[data-bind='html: $parent.prepareMessageForHtml(message.text)']"


class LoginLocators:
    LINK_LOGIN = 'https://magento.softwaretestingboard.com/customer/account/login'
    FIELD_NAME = 'div.login-container #email'
    FIELD_PASSWORD = 'div.login-container #pass'
    BUTTON_SUBMIT = 'div.login-container #send2'
    MESSAGE_UNSUCCESSFUL = '#pass-error'
    USER_NAME_IN_WELCOME = '.logged-in'
    AUTHORIZATION_LINK = 'authorization-link'
    LINK_ACCOUNT = 'https://magento.softwaretestingboard.com/customer/account/'


class FooterLocators:
    FOOTER_LINKS = ('xpath', '//footer[@class="page-footer"]//li')


class ContactUsLocators:
    CONTACT_US_LINK = "//*[text()='Contact Us']"


class PrivacyPolicy:
    GO_BACK_LINK = "//*[@id='maincontent']/div[3]/div[1]/dl[2]/dd[2]/ul/li[1]/a"
    PRIVACY_POLICY_TITLE = "span[data-ui-id='page-title-wrapper']"


class SaleWomenDealsLocators:
    JACKETS = "//*[@id='maincontent']/div[4]/div[2]/div/div/ul[1]/li[2]/a"
    ADD_TO_COMPARE_BTN_ONE = ".actions-secondary a[data-post*='1396']:nth-child(2)"
    ADD_TO_COMPARE_BTN_ONE_TWO = ".actions-secondary a[data-post*='1380']:nth-child(2)"
    ELEMENT_ONE = "img[alt='Olivia 1/4 Zip Light Jacket']"
    ELEMENT_TWO = "img[alt='Juno Jacket']"
    QUANTITY_ITEMS = "div[class='block-title'] span[class='counter qty']"


class CreateAccountLocators:
    CREATE_AN_ACCOUNT_LINK = "(//a[.='Create an Account'])[1]"


class ErinRecommendLocators:
    HOME_ERIN_BLOCK = "//a[@class='block-promo home-erin']"
    PAGE_HEADER = "//span[@data-ui-id='page-title-wrapper']"
    FOOTER = "//footer[@class='page-footer']"
    PAGINATION_CONTROL = "//div[@class='pages']"
    PAGE_NEXT = "(//a[@title='Next'])[2]"
    PAGE_DROPDOWN = "(//select[@data-role='limiter'])[2]"
    PRODUCTS = browser.all(".product-item")
    LIST_VIEW_BUTTON = "//a[@id='mode-list']"
    PRODUCT_LIST = "//div[@class='products wrapper list products-list']"
    ITEM_JADE_YOGA_JACKET = "//a[contains(text(), 'Jade Yoga Jacket')]"
    ADD_TO_COMPARE = ".actions-secondary a[data-post*='1332']:nth-child(2)"
    MESSAGE_ADD_TO_COMPARE = "//div[contains(text(), 'You added product Jade Yoga Jacket to the ')]"
    TEXT_COMPARE_ITEMS = "//a[@title='Compare Products']"


class PerformanceSportswear:
    LINK_SPORT = "https://magento.softwaretestingboard.com/collections/performance-new.html"
    BUTTON_ADD_ITEM2 = '#maincontent li:nth-child(2) button'
    SUCCESS_MESSAGE = '#maincontent > div.page.messages > div:nth-child(2) > div > div > div'
    TEXT_SUCCESS_MESSAGE = 'You added Helios Endurance Tank to your shopping cart'
    IMAGE_2 = '#maincontent ol > li:nth-child(2) .product-image-container'
    ITEM_2_IN_GENERAL = 'li.product-item:nth-child(2)'


class WishListLocators:
    EMPTY_MESSAGE = '.message.info.empty span'
    DELETE_BUCKET = '.btn-remove.action.delete'
    PRODUCT_ITEM = '.products-grid.wishlist .product-item'
    ITEM_ACTIONS = ".product-item-actions"
    QUALITY = "input[name='qty']"
    COLORS = "div.swatch-attribute.color .swatch-option.color"
    SIZES = "div.swatch-attribute.size .swatch-option.text"
    UPDATED = "a.action.towishlist.updated"


class CartLocators:
    QTY = '.input-text.qty'
    UPDATE_SHOPPING_CART_BUTTON = '.action.update'
    REMOVE_ITEM_ICON = '.action.action-delete'
    NO_ITEMS_MESSAGE = '//p[text()="You have no items in your shopping cart."]'
    CLICK_MESSAGE = '//p[contains(text(), "Click")]'


class TrainingPageLocators:
    VIDEO_DOWNLOAD_LINK = '#narrow-by-list2 li a'
    VIDEO_DOWNLOAD_TRAINING_TITLE = 'span[data-ui-id="page-title-wrapper"'
    BLOCK_1 = '.blocks-promo a:first-child'
    CONTENT_BLOCK_1 = '.blocks-promo a:first-child .title'
    IMG_BLOCK_1 = 'a[class="block-promo training-main"] img'


class PerformanceSportswear:
    LINK_SPORT = "https://magento.softwaretestingboard.com/collections/performance-new.html"
    BUTTON_ADD_ITEM2 = '#maincontent li:nth-child(2) button'
    SUCCESS_MESSAGE = '#maincontent > div.page.messages > div:nth-child(2) > div > div > div'
    TEXT_SUCCESS_MESSAGE = 'You added Helios Endurance Tank to your shopping cart'
    IMAGE_2 = '#maincontent ol > li:nth-child(2) .product-image-container'
    ITEM_2_IN_GENERAL = 'li.product-item:nth-child(2)'


class YogaPageLocators:
    PAGE_TITLE = '#page-title-heading > span'
    LIST_BUTTON = '.modes-mode.mode-list'
    WRAPPER_LIST_VIEW = '.products.wrapper.list'
    GRID_BUTTON = '.modes-mode.mode-grid'
    WRAPPER_GRID_VIEW = '.products.wrapper.grid'


class MenSaleLocators:
    PAGE_TITLE = "[data-ui-id='page-title-wrapper']"
    LIST_ITEM = "li.product-item"
    TOOLBAR_NUMBER = "#toolbar-amount>span"


class SetYogaStrapsLocators:
    SPRITE_YOGA_STRAP_10_FOOT = '//input[@data-selector = "super_group[35]"]'
    NOT_AVAILABLE_MESSAGE = '//div[contains(text(),"The requested qty is not available")]'


class PopularSearchTermsLocators:
    HOODIE_LINK = '//a[contains(text(),"HOODIE")]'
    SEARCH_RESULTS_HEADER = '//h1/span[@data-ui-id="page-title-wrapper"]'


class TeesPageLocators:
    FOUR_TEES_DISCOUNT_TAB = '//span[contains(text(),"4 tees for the price of 3. Right now")]'
    TEES = 'img[alt="Desiree Fitness Tee"]'
    TEES_SIZE = '#option-label-size-143-item-166'
    TEES_COLORS = '#option-label-color-93-item-49'
    TEES_QTY = "#qty"
    VIEW_AND_EDIT_CART_LINK = '//span[contains(text(),"View and Edit Cart")]'
    DISCOUNT_SUMM = 'td[data-th="Discount"] span.price'
    REMOVE_TEES_BTN_FROM_CART_AFTER_TEST = 'a[class="action action-delete"]'
    COUNT_NUMBER = 'span.counter-number'


class WomenLocators:
    TANK_SIZE = '//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="M"]'
    TANK_COLOR = '//*[@title="Breathe-Easy Tank"]/../..//*[@option-label="Yellow"]'
    TANK_BUTTON_ADD = '//*[@title="Breathe-Easy Tank"]/../..//*[@title="Add to Cart"]'
    MESSAGE_SUCCESS_ADD = "div.messages [data-bind ^='html']"
    SHOW_BASKET = ".action.showcart"
    CHECKOUT_BUTTON = '#top-cart-btn-checkout'


class Shipping:
    FIELD_EMAIL = '#customer-email-fieldset #customer-email'
    FIELD_FIRST_NAME = '[name="firstname"]'
    FIELD_LAST_NAME = '[name="lastname"]'
    FIELD_STREET = '[name="street[0]"]'
    FIELD_CITY = '[name="city"]'
    FIELD_REGION = '[name="region_id"]'
    FIELD_COUNTRY = '[name="country_id"]'
    FIELD_ZIPCODE = '[name="postcode"]'
    FIELD_PHONE = '[name="telephone"]'
    SHIPPING_METHOD = '#checkout-shipping-method-load input'
    CONTINUE_BUTTON = '.continue'


class Order:
    BUTTON_PLACE_ORDER = '.primary.checkout'
    MESSAGE_SUCCEES = '.checkout-success'
    ORDER_PAGE_TITLE = '.page-title'
