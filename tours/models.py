from django.db import models
from destinations.models import Destination
from django_prose_editor.fields import ProseEditorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class TourCategory(models.Model):
    name = models.CharField(max_length=100)
    background_image = models.ImageField(
        upload_to='tour_categories/', blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tour categories'


class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = ProseEditorField()
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    category = models.ForeignKey(
        TourCategory, on_delete=models.SET_NULL, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField()
    max_participants = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TourInfo(models.Model):
    departure = models.CharField(max_length=128)
    departure_time = models.TimeField()
    return_time = models.TimeField()
    inclusions = ProseEditorField()
    exclusions = ProseEditorField()
    tour = models.OneToOneField(
        Tour, on_delete=models.CASCADE, related_name='info')

    def __str__(self):
        return self.tour.name


class TourPlan(models.Model):
    day = models.IntegerField()
    title = models.CharField(max_length=100)
    description = ProseEditorField()
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='plans')


class TourQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.question


class TourPicture(models.Model):
    image = models.ImageField(upload_to='tour_pictures/')
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='pictures')


class TourReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.user.email} - {self.created_at}"
