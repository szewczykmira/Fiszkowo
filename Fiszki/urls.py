from django.conf.urls import patterns, url
from views import home, add_category, edit_fiszka, about_author, display_fiszka_for_category

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^addcategory/$', add_category, name='add_category'),
    url(r'^addfiszka/$', edit_fiszka, name='add_fiszka'),
    url(r'^about/$', about_author, name='about_author'),
    url(r'^category/(?P<cat_id>\d+)/$', display_fiszka_for_category, name='display_cat'),
)
