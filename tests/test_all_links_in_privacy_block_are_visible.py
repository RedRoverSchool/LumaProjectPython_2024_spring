import allure

from pages import privacy_policy_page

url_navigate = "https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode"

text = ["Luma Security", "Luma Privacy Policy", "The Information We Collect",
        "How We Use The Information We Collect", "Security",
        "Others With Whom We Share Your Information.", "Your Choices Regarding Use Of The Information We Collect",
        "Your California Privacy Rights", "Cookies, Web Beacons, and How We Use Them",
        "List of cookies we collect", "Online Account Registration", "Emails", "Acceptance", "Questions for Luma?"]


@allure.feature("Privacy and Cookie Policy > Main Content >")
@allure.title('All links in the block on the left are visible')
@allure.link('https://trello.com/c/sRAofRDe')
def test_all_links_in_privacy_left_block_are_visible():
    privacy_policy_page.open_page_with_navigate_block(url_navigate)
    privacy_policy_page.move_to_elements(text)
