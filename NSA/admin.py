from django.contrib import admin
from NSA.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('sport', 'players', 'info', 'address', 'latitude', 'longitude')

# Register your models here.
admin.site.register(Event)
