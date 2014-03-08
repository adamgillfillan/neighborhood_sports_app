from django.contrib import admin
from NSA.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('sport', 'players', 'info', 'address')

# Register your models here.
admin.site.register(Event)
