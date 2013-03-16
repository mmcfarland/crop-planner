from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import SessionAuthentication
from tastypie.exceptions import Unauthorized

from planner.models import Crop, GardenSite, SiteUser, Variety, PlantingGuide
from django.contrib.auth.models import User

class ScopedGardenAuth(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(site=bundle.request.session['garden_site'])

    def read_detail(self, object_list, bundle):
        # bundle obj is the resource being requested
        if bundle.obj.site != bundle.request.session['garden_site']:
            raise Unauthorized()
        return True

    def create_list(self, object_list, bundle):
        return object_list

    def create_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def update_list(self, object_list, bundle):
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_staff', 'is_superuser']
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
        authorization = ScopedGardenAuth()

class PlantingGuideResource(ModelResource):
    class Meta:
        queryset = PlantingGuide.objects.all()
        resource_name = 'guide'
        authentication = SessionAuthentication()
        authorization = ScopedGardenAuth()


