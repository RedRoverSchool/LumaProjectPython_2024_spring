import pytest
from selene import browser
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
import allure
import data.links
from pages.locators import FooterLocators, BaseLocators


@pytest.mark.skip
@allure.link('https://trello.com/c/PMzBgZUn')
@allure.title('Verifying a footer links from all of the site pages')
def test_012_001_001_verify_footer_links():
    def visit(url):
        return browser.open(url)

    def check_header(header):
        return s(BaseLocators.PAGE_TITLE).should(have.text(header))

    def check_links_texts():
        ss(FooterLocators.FOOTER_LINKS).should(have.exact_texts(
            "Notes ",
            "Practice API Testing using Magento 2",
            "Write for us",
            "Subscribe",
            "Search Terms",
            "Privacy and Cookie Policy",
            "Advanced Search",
            "Orders and Returns"
        ))

    visit(data.links.BASE_URL)
    check_header("Home Page")
    check_links_texts()

    visit(data.links.WHATS_NEW_PAGE_LINK)
    check_header("What's New")
    check_links_texts()

    visit(data.links.WOMEN_PAGE_LINK)
    check_header("Women")
    check_links_texts()

    visit(data.links.TOPS_WOMEN_PAGE_LINK)
    check_header("Tops")
    check_links_texts()

    visit(data.links.BOTTOMS_WOMEN_PAGE_LINK)
    check_header("Bottoms")
    check_links_texts()

    visit(data.links.MEN_PAGE_URL)
    check_header("Men")
    check_links_texts()

    visit(data.links.MEN_TOPS_PAGE_URL)
    check_header("Tops")
    check_links_texts()

    visit(data.links.MEN_BOTTOMS_PAGE_URL)
    check_header("Bottoms")
    check_links_texts()

    visit(data.links.GEAR_PAGE_URL)
    check_header("Gear")
    check_links_texts()

    visit(data.links.GEAR_BAGS_URL)
    check_header("Bags")
    check_links_texts()

    visit(data.links.GEAR_FITNESS_URL)
    check_header("Fitness Equipment")
    check_links_texts()

    visit(data.links.GEAR_WATCHES_URL)
    check_header("Watches")
    check_links_texts()

    visit(data.links.TRAINING_URL)
    check_header("Training")
    check_links_texts()

    visit(data.links.VIDEO_DOWNLOAD_URL)
    check_header("Video Download")
    check_links_texts()

    visit(data.links.SALE_PAGE_URL)
    check_header("Sale")
    check_links_texts()
