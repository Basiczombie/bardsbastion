from django.contrib import admin
from .models import Color

# Register your models here.
class ColorAdmin(admin.ModelAdmin):
    list_display = ('pigment', 'hexcode', 'activity_user', 'activity_date', 'activity_user')

admin.site.register(Color, ColorAdmin)