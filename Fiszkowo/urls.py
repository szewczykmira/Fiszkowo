from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Fiszki.views.home', name='home'),
    url(r'^addcategory/$', 'Fiszki.views.add_category', name='add_category'),
    url(r'^addfiszka/$', 'Fiszki.views.edit_fiszka', name='add_fiszka'),
    url(r'^about/$', 'Fiszki.views.about_author', name='about_author'),
    url(r'^details/(?P<fiszka_id>\d+)/$', 'Fiszki.views.display_fiszka', name='details'),
    url(r'^deletecategory/(?P<cat_id>\d+)/$', 'Fiszki.views.delete_category', name='delete_category'),
    url(r'^deletefiszka/(?P<fiszka_id>\d+)/$', 'Fiszki.views.display_fiszka', name='delete_fiszka'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
