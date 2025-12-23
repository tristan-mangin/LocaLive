from django.db import models

# Sample model for web scraped place
class ScrapedPlace(models.Model):
    source = models.CharField(max_length=50)         # e.g. "songkick"
    external_id = models.CharField(max_length=200)   # id on remote site
    name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    raw = models.JSONField(null=True, blank=True)    # raw scraped payload
    last_scraped = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("source", "external_id")

# Custom written model (likely to be changed later)
class ScrapedEvent(models.Model):
    source = models.CharField(max_length=50)         # e.g. "songkick"
    external_id = models.CharField(max_length=200)   # id on remote site
    title = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    venue_name = models.CharField(max_length=255, null=True, blank=True)
    venue_address = models.CharField(max_length=500, null=True, blank=True)
    performer = models.CharField(max_length=255, null=True, blank=True)
    raw = models.JSONField(null=True, blank=True)    # raw scraped payload
    last_scraped = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("source", "external_id")