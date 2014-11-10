from django.conf.urls import patterns, url
from views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='dictionary_home'),
)
