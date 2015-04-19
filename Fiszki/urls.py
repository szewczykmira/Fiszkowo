from django.conf.urls import patterns, url
from views import home, edit_fiszka, display_fiszka_for_category, save_category

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^addfiszka/$', edit_fiszka, name='add_fiszka'),
    url(r'^category/(?P<cat_id>\d+)/$', display_fiszka_for_category, name='display_cat'),
    url(r'^addcat$', save_category, name="save_category")
)
