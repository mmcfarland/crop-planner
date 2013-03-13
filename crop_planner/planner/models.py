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
    direct_seeded = models.BooleanField()
    # Only the month/day are important, the year should default
    # to 1900 or other generic year
    season_start = models.DateField()
    season_end = models.DateField()

class PlantingGuide(models.Model):
    """Specifications for planting scenarios of a variety"""
    variety = models.ForeignKey(Variety)
    row_spacing = models.DecimalField(help_text="Inches between rows")
    plant_spacing = models.DecimalField(help_text="Inches between plants of a single row")
    start_harvesting = models.DateField(help_text="Desired date to begin harvesting")
    end_harvesting = models.DateField(null=True, blank=True,
        help_text="Desired date to continue harvesting until")

    seed = models.DateField(help_text="Date to plant seeds")
    transplant = models.DateField(null=True, blank=True,
        help_text="Date to transplant outside")
    

