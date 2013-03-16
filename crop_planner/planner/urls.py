from planner.views import route
from django.conf.urls import patterns, url
from planner.views import *

urlpatterns = patterns('',
    url(r'^login/', route(GET=get_login, POST=auth )),
)