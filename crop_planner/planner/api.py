from tastypie.resources import ModelResource
from planner.models import Crop


class CropResource(ModelResource):
    class Meta:
        queryset = Crop.objects.all()
        resource_name = 'crop'
