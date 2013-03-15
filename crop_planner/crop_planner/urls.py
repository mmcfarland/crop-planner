from django.conf.urls import patterns, include, url
from planner.api import CropResource

crop_resource = CropResource()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^/', include('planner.urls')),
    url(r'^api/', include(crop_resource.urls))
)
