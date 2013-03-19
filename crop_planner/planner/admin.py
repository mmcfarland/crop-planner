
from django.contrib import admin
from planner.models import GardenSite, Crop, SiteUser, Variety, PlantingGuide,\
    IntervalHarvestPlan, IntervalHarvest, IntervalVariety

admin.site.register(GardenSite)
admin.site.register(Crop)
admin.site.register(SiteUser)
admin.site.register(Variety)
admin.site.register(PlantingGuide)
admin.site.register(IntervalHarvestPlan)
admin.site.register(IntervalHarvest)
admin.site.register(IntervalVariety)
