from django.conf.urls import patterns, url
from views import home, add_category, edit_fiszka, about_author, delete_category, display_fiszka

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^addcategory/$', add_category, name='add_category'),
    url(r'^addfiszka/$', edit_fiszka, name='add_fiszka'),
    url(r'^about/$', about_author, name='about_author'),
    url(r'^details/(?P<fiszka_id>\d+)/$', display_fiszka, name='details'),
    url(r'^deletecategory/(?P<cat_id>\d+)/$', delete_category, name='delete_category'),
    url(r'^deletefiszka/(?P<fiszka_id>\d+)/$', display_fiszka, name='delete_fiszka')
)
