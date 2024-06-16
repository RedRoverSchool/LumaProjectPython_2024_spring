import allure

from pages import main_page, whats_new, women_page, men_page, gear_page, training_page, sale, footer

base_url = 'https://magento.softwaretestingboard.com/'
gear_page_url = base_url + 'gear.html'
gear_bags_url = base_url + 'gear/bags.html'
gear_fitness_url = base_url + 'gear/fitness-equipment.html'
gear_watches_url = base_url + 'gear/watches.html'


@allure.feature('Footer > Visibility, Clickability, Redirect')
@allure.title('Verifying a footer links from all of the site pages')
@allure.link('https://trello.com/c/PMzBgZUn')
def test_verify_footer_links():
    main_page.open_page()
    main_page.check_header("Home Page")
    footer.check_links_texts()

    whats_new.open_page()
    main_page.check_header("What's New")
    footer.check_links_texts()

    women_page.visit()
    main_page.check_header("Women")
    footer.check_links_texts()

    women_page.visit_tops_women()
    main_page.check_header("Tops")
    footer.check_links_texts()

    women_page.visit_bottoms_women()
    main_page.check_header("Bottoms")
    footer.check_links_texts()

    men_page.open_page()
    main_page.check_header("Men")
    footer.check_links_texts()

    men_page.visit_men_top_page()
    main_page.check_header("Tops")
    footer.check_links_texts()

    men_page.visit_bottoms_page()
    main_page.check_header("Bottoms")
    footer.check_links_texts()

    gear_page.open_page()
    main_page.check_header("Gear")
    footer.check_links_texts()

    gear_page.open_gear_bags_page()
    main_page.check_header("Bags")
    footer.check_links_texts()

    gear_page.visit(gear_fitness_url)
    main_page.check_header("Fitness Equipment")
    footer.check_links_texts()

    gear_page.visit(gear_watches_url)
    main_page.check_header("Watches")
    footer.check_links_texts()

    training_page.open()
    main_page.check_header("Training")
    footer.check_links_texts()

    training_page.visit_download_page()
    main_page.check_header("Video Download")
    footer.check_links_texts()

    sale.open_page()
    main_page.check_header("Sale")
    footer.check_links_texts()
