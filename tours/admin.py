from django.contrib import admin
from .models import Tour, TourCategory, TourInfo, TourPlan, TourQuestion, TourPicture, TourReview


class TourInfoInline(admin.StackedInline):
    model = TourInfo
    extra = 1


class TourPlanInline(admin.StackedInline):
    model = TourPlan
    extra = 1


class TourQuestionInline(admin.StackedInline):
    model = TourQuestion
    extra = 1


class TourPictureInline(admin.StackedInline):
    model = TourPicture
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'duration', 'destination']
    list_filter = ['category', 'destination']
    search_fields = ['title', 'destination']
    inlines = [TourInfoInline, TourPlanInline, TourQuestionInline, TourPictureInline]


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(TourReview)
class TourReviewAdmin(admin.ModelAdmin):
    list_display = ['tour', 'user', 'rating', 'content']
    list_filter = ['tour', 'rating']
    search_fields = ['tour', 'user']
