from django.contrib import admin
from .models import Tour, TourCategory, TourInclusion, TourExclusion, TourHighlight, TourInfo


class TourInfoInline(admin.StackedInline):
    model = TourInfo
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'duration', 'destination']
    list_filter = ['category', 'destination']
    search_fields = ['title', 'destination']
    inlines = [TourInfoInline]


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(TourInclusion)
class TourInclusionAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']


@admin.register(TourExclusion)
class TourExclusionAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']


@admin.register(TourHighlight)
class TourHighlightAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
