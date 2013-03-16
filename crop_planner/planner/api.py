from tastypie.resources import ModelResource
from tastypie.authentication import SessionAuthentication

from planner.models import Crop, GardenSite, SiteUser, Variety, PlantingGuide
from django.contrib.auth.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = SessionAuthentication()
        allowed_methods = ['get']

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)

class CropResource(ModelResource):
    class Meta:
        queryset = Crop.objects.all()
        resource_name = 'crop'
        authentication = SessionAuthentication()

class VarietyResource(ModelResource):
    class Meta:
        queryset = Variety.objects.all()
        resource_name = 'variety'
        authentication = SessionAuthentication()

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(site=request.session.garden_site)

