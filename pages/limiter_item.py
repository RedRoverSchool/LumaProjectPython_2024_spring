from selene import browser, have, be
from selene.support.shared.jquery_style import s

url = 'https://magento.softwaretestingboard.com/customer/account/login'
wish_list = 'https://magento.softwaretestingboard.com/wishlist/'
user_email = s("div.login-container #email")
user_password = s("div.login-container #pass")
sign_in_button = s("div.login-container #send2")
limiter = '//*[@id="limiter"]'
limit_20 = '//*[@id="limiter"]/option[2]'
limit_10 = '//*[@id="limiter"]/option[1]'
toolbar_number = '//*[@class="toolbar-number"]'
next_page = '//*[@class="action  next"]'
item = '//*[@class="product-item"][1]'

user = "alexx.shigaev@gmail.com"
password = "B2a6ig_a9Hb3cz@"

def preconditions():
    browser.open(url)
    user_email.type(user)
    user_password.type(password)
    sign_in_button.click()
    browser.open(wish_list)

def change_limit_to_20():
    s(limiter).click()
    s(limit_20).click()

def change_limit_to_10():
    s(limiter).click()
    s(limit_10).click()

def items_number():
    s(toolbar_number).should(have.text('11 Item(s)'))

def items_amount():
    s(toolbar_number).should(have.text('Items 11 to 11 of 11 total'))

def item_page_item_next():
    s(next_page).click()
    s(item).should(be.visible)

