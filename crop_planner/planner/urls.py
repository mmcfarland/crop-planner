from planner.views import *
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/', route(GET=get_login, POST=auth )),
    url(r'^home/', route(GET=home)),
)