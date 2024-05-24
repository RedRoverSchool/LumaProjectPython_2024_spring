from selene import query, have
from selene.support.conditions import be
from selene.support.shared.jquery_style import s





def assert_reviews_title_is_visible():
    s("#tab-label-reviews-title").should(be.visible)
