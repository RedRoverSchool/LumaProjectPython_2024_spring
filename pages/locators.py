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
    RADIANT_TEE_LINK = "//*[contains(text(), 'Radiant Tee')]"
    RADIANT_TEE_IMG = 'img[alt="Radiant Tee"]'
    RADIANT_TEE_TITLE = 'span[data-ui-id="page-title-wrapper"]'
    RADIANT_TEE_PRICE = '#product-price-1556'
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
    MINICART_VIEW = '.action.viewcart'
    MINICART_COUNTER = '.counter-label'


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
    # locators for all pages
    PAGE_NAME = ".base"
    PAGE_TITLE = "h1"
    PAGE_HEADER = "#page-title-heading"
    BREADCRUMBS_LIST = ".breadcrumbs li"
    BREADCRUMBS_LINKS = '.breadcrumbs > ul  > li > a'
    BREADCRUMBS = ".breadcrumbs > ul"
    PRIVACY_COOKIE_POLICY_LOCATOR = "//a[contains(@href, 'privacy-policy-cookie')]"
    PRODUCT_ITEM_IN_CATALOG = 'li.product-item'  # каждый товар на любой странице в каталоге
    PRODUCT_PRICE = 'price-label'
    PRODUCT_NAME = 'product-item-link'
    PRODUCT_IMAGE = 'product-image-photo'
    ALL_URL = ["https://magento.softwaretestingboard.com/",
               "https://magento.softwaretestingboard.com/what-is-new.html",
               "https://magento.softwaretestingboard.com/women/tops-women/jackets-women.html,"
               "https://magento.softwaretestingboard.com/training.html"
                ]
    NEW_LUMA_YOGA_COLLECTION_BLOCK_LOCATOR = "//a[contains(@class,'home-main')]/span"
    NEW_LUMA_YOGA_COLLECTION_BLOCK_INFO_TEXT_LOCATOR = "//a[contains(@class,'home-main')]//span[@class='info']"


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


class PrivacyPolicyPageLocators:
    PAGE_MAIN_HEADER_LOCATOR = "span[data-ui-id='page-title-wrapper']"


class ProductItemLocators:
    WISH_LIST = "[aria-label='Add to Wish List']"
    ITEM_INFO = ".product-item-info"


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
    CONTACT_US_LINK = "//*[@id='maincontent']/div[3]/div/div[3]/div[1]/p[33]/a"


class PrivacyPolicy:
    GO_BACK_LINK = "//*[@id='maincontent']/div[3]/div[1]/dl[2]/dd[2]/ul/li[1]/a"
    PRIVACY_POLICY_TITLE = "span[data-ui-id='page-title-wrapper']"


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


class PerformanceSportswear:
    LINK_SPORT = "https://magento.softwaretestingboard.com/collections/performance-new.html"


class WishListLocators:
    EMPTY_MESSAGE = '.message.info.empty span'
    DELETE_BUCKET = '.btn-remove.action.delete'
    SUCCESS_MESSAGE = '.message-success.success.message'
    PRODUCT_ITEM = '.products-grid.wishlist .product-item'
    ITEM_ACTIONS = ".product-item-actions"
    QUALITY = "input[name='qty']"
    COLORS = "div.swatch-attribute.color .swatch-option.color"
    SIZES = "div.swatch-attribute.size .swatch-option.text"
    UPDATED = "a.action.towishlist.updated"

class CartLocators:
    QTY = '.input-text.qty'
    UPDATE_SHOPPING_CART_BUTTON = '.action.update'

class TrainingPageLocators:
    VIDEO_DOWNLOAD_LINK = '#narrow-by-list2 li a'
    VIDEO_DOWNLOAD_TRAINING_TITLE = 'span[data-ui-id="page-title-wrapper"'

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


class SetYogaStrapsLocators:
    SPRITE_YOGA_STRAP_10_FOOT = '//input[@data-selector = "super_group[35]"]'
    NOT_AVAILABLE_MESSAGE = '//div[contains(text(),"The requested qty is not available")]'
