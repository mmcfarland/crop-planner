from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crop_planner.views.home', name='home'),
    # url(r'^crop_planner/', include('crop_planner.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
