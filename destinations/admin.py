from django.contrib import admin
from .models import Destination, DestinationInfo


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['city', 'country', 'description']
    search_fields = ['city', 'country']


@admin.register(DestinationInfo)
class DestinationInfoAdmin(admin.ModelAdmin):
    list_display = ['languages', 'currency', 'area', 'population', 'timezone', 'time_to_travel', 'destination']
    search_fields = ['destination']
