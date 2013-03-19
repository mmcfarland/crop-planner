from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import PassThroughManager

class GardenSiteQuerySet(models.query.QuerySet):
    def scope(self, model):
        return  model.objects.filter(site=self)


class GardenSite(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    first_frost = models.DateField()
    last_frost = models.DateField()

    query = PassThroughManager.for_queryset_class(GardenSiteQuerySet)()

    def __unicode__(self):
        return unicode(self.name)

class ScopedGardenModel(models.Model):
    site = models.ForeignKey(GardenSite, related_name="related_%(class)s")

    class Meta:
        abstract = True


class SiteUserQuerySet(models.query.QuerySet):
    def by(self, user):
        return  self.get(user=user)


class SiteUser(models.Model):
    site = models.ForeignKey(GardenSite, related_name="users")
    user = models.ForeignKey(User)

    query = PassThroughManager.for_queryset_class(SiteUserQuerySet)()

    def __unicode__(self):
        return unicode("%s (%s)" % (self.user.username, self.site.name))


class Note(models.Model):
    date = models.DateField(auto_created=True)
    text = models.TextField()
    user = models.ForeignKey(User)


class Crop(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Variety(ScopedGardenModel):
    """A crop instance for a site"""
    crop = models.ForeignKey(Crop)
    name = models.CharField(max_length=255)
    dtm = models.IntegerField(verbose_name="Days to Maturity")
    direct_seeded = models.BooleanField()
    # Only the month/day are important, the year should default
    # to 1900 or other generic year
    season_start = models.DateField()
    season_end = models.DateField()

    def __unicode__(self):
        return unicode("%s - %s" % (self.name, self.crop))


class PlantingGuide(ScopedGardenModel):
    """Specifications for planting scenarios of a variety.
        Able to answer the questions:
            - How much space will be desired amount take
            - How much will my required space produce
            - How much should I start
            - What schedule should I propagate and plant
    """
    name = models.CharField(max_length=255)
    variety = models.ForeignKey(Variety)
    row_spacing = models.DecimalField(max_digits=5, decimal_places=2,
        help_text="Inches between rows")
    plant_spacing = models.DecimalField(max_digits=5, decimal_places=2,
        help_text="Inches between plants of a single row")
    thin_to_spacing = models.DecimalField(max_digits=5, decimal_places=2,
        help_text="Inches between plants of a single row, after thinning",
        null=True, blank=True)
    start_harvesting = models.DateField(help_text="Desired date to begin harvesting")
    end_harvesting = models.DateField(null=True, blank=True,
        help_text="Desired date to continue harvesting until")

    seed = models.DateField(help_text="Date to plant seeds")
    transplant = models.DateField(null=True, blank=True,
        help_text="Date to transplant outside")

    buffer = models.DecimalField(max_digits=2, decimal_places=2,
        help_text="Percent expected to fail (germination, etc)")

    def __unicode__(self):
        return unicode("%s %s" % (self.variety , self.pk))

class PlantingGuideNote(Note):
    guide =  models.ForeignKey(PlantingGuide, related_name='notes')

class VarietyNote(Note):
    variety = models.ForeignKey(Variety, related_name='notes')
