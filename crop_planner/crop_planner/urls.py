from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from planner.api import CropResource, VarietyResource, UserResource, \
    PlantingGuideResource, GardenResource

api = Api(api_name='v0.1')
api.register(CropResource())
api.register(VarietyResource())
api.register(UserResource())
api.register(PlantingGuideResource())
api.register(GardenResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('planner.urls')),
    url(r'^api/', include(api.urls)),
)