from selene.support.shared.jquery_style import s


class MainPage:
    url = "https://magento.softwaretestingboard.com/"

    PRIVACY_COOKIE_POLICY_LOCATOR = "//a[contains(@href, 'privacy-policy-cookie')]"

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.open(self.url)

    @property
    def privacy_cookie_policy_link(self):
        return s(self.PRIVACY_COOKIE_POLICY_LOCATOR)

    def scroll_to_privacy_cookie_policy_link(self):
        element = self.privacy_cookie_policy_link()
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
