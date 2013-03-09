from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    first_frost = models.DateField()
    last_frost = models.DateField()

class SiteUser(models.Model):
    site = models.ForeignKey(Site, related_name="users")
    user = models.ForeignKey(User)

class Crop(models.Model):
    name = models.CharField(max_length=255)

class Variety(models.Model):
    """A crop instance for a site"""
    crop = models.ForeignKey(Crop)
    site = models.ForeignKey(Site, related_name="users")
    name = models.CharField(max_length=255)
    dtm = models.IntegerField(verbose_name="Days to Maturity")

class PlantingGuide(models.Model):
    variety = models.ForeignKey(Variety)
    row_spacing = models.DecimalField()
    plant_spacing = models.DecimalField()
    