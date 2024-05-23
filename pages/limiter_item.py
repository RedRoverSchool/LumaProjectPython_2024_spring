from selene import browser, have
from selene.support.shared.jquery_style import s

url = 'https://magento.softwaretestingboard.com/customer/account/login'
wish_list = 'https://magento.softwaretestingboard.com/wishlist/'
user_email = s("div.login-container #email")
user_password = s("div.login-container #pass")
sign_in_button = s("div.login-container #send2")
limiter = '//*[@id="limiter"]'
limit = '//*[@id="limiter"]/option[2]'
items = '//*[@id="maincontent"]/div[2]/div[1]/div[3]/div/p/span'

user = "alexx.shigaev@gmail.com"
password = "B2a6ig_a9Hb3cz@"

def preconditions():
    browser.open(url)
    user_email.type(user)
    user_password.type(password)
    sign_in_button.click()
    browser.open(wish_list)

def change_limiter():
    s(limiter).click()
    s(limit).click()

def change_verification():
    s(items).should(have.text('11 Item(s)'))