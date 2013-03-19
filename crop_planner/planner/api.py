from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import SessionAuthentication
from tastypie.exceptions import Unauthorized
from tastypie import fields

from planner.models import Crop, GardenSite, SiteUser, Variety, PlantingGuide, \
    IntervalHarvestPlan, IntervalHarvest, IntervalVariety

from django.contrib.auth.models import User

class ScopedGardenAuth(Authorization):

    def read_list(self, object_list, bundle):
        return object_list.filter(site=bundle.request.session['garden_site'])

    def read_detail(self, object_list, bundle):
        # bundle obj is the resource being requested
        if not bundle.obj.site == bundle.request.session['garden_site']:
            raise Unauthorized()
        return True

    def create_list(self, object_list, bundle):
        print 'cl'
        return object_list

    def create_detail(self, object_list, bundle):
        # Everything a user creates will be scoped to their site
        bundle.obj.site = bundle.request.session['garden_site']
        return True

    def update_list(self, object_list, bundle):
        print 'ul'
        allowed = []

        # Since they may not all be saved, iterate over them.
        for obj in object_list:
            if obj.user == bundle.request.user:
                allowed.append(obj)

        return allowed

    def update_detail(self, object_list, bundle):
        print 'ud'
        return bundle.obj.user == bundle.request.user

    def delete_list(self, object_list, bundle):
        # Sorry user, no deletes for you!
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

class GardenResource(ModelResource):
    class Meta:
        queryset = GardenSite.query.all()
        resource_name = 'garden-site'
        authentication = SessionAuthentication()


class BaseGardenScopeResource(ModelResource):
    site = fields.ForeignKey(GardenResource, 'site')

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


class VarietyResource(BaseGardenScopeResource):
    crop = fields.ForeignKey(CropResource, 'crop')

    class Meta:
        queryset = Variety.objects.all()
        resource_name = 'variety'
        allowed_methods = ['get', 'post']
        authentication = SessionAuthentication()
        authorization = ScopedGardenAuth()


class PlantingGuideResource(BaseGardenScopeResource):
    variety = fields.ForeignKey(VarietyResource, 'variety')

    class Meta:
        queryset = PlantingGuide.objects.all()
        resource_name = 'guide'
        authentication = SessionAuthentication()
        authorization = ScopedGardenAuth()

class IntervalHarvestResource(BaseGardenScopeResource):
    #plan = fields.ForeignKey(IntervalHarvestPlanResource, 'plan')
    varieties = fields.ToManyField('planner.api.IntervalHarvestVarietyResource',
        'varieties', full=True)
    class Meta:
        queryset = IntervalHarvest.objects.all()
        resource_name = 'ih'
        authentication = SessionAuthentication()
        authorization = ScopedGardenAuth()

class IntervalHarvestPlanResource(BaseGardenScopeResource):
    harvests = fields.ToManyField('planner.api.IntervalHarvestResource',
        'intervalharvest_set', full=True)

    class Meta:
        queryset = IntervalHarvestPlan.objects.all()
        resource_name = 'ih-plan'
        authentication = SessionAuthentication()
        authorization = ScopedGardenAuth()


class IntervalHarvestVarietyResource(BaseGardenScopeResource):
    variety = fields.ForeignKey(VarietyResource, 'variety')
    harvest = fields.ForeignKey(IntervalHarvestResource, 'harvest')

    class Meta:
        queryset = IntervalVariety.objects.all()
        resource_name = 'ih-variety'
        authentication = SessionAuthentication()
        authorization = ScopedGardenAuth()
