from django.db import models

# Base Models for the site
class Audit(models.Model):
    activity_user = models.CharField(max_length=255, editable=False)
    activity_date = models.DateTimeField(auto_now=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

class Color(Audit):
    pigment = models.TextField(max_length=255, help_text="The color")
    hexcode = models.TextField(max_length=7, help_text="The hexcode")

    class Meta:
        verbose_name_plural = 'colors'