from selene.support.shared.jquery_style import ss
from selene.support.conditions import have

footer_links = ss('//footer[@class="page-footer"]//li')


def check_links_texts():
    footer_links.should(have.exact_texts(
        "Notes ",
        "Practice API Testing using Magento 2",
        "Write for us",
        "Subscribe",
        "Search Terms",
        "Privacy and Cookie Policy",
        "Advanced Search",
        "Orders and Returns"
    ))
