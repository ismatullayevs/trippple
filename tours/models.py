from django.db import models
from destinations.models import Destination


class TourCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tour categories'
    

class TourHighlight(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class TourInclusion(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
    

class TourExclusion(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description
    

class TourInfo(models.Model):
    departure = models.CharField(max_length=128)
    departure_time = models.TimeField()
    return_time = models.TimeField()
    inclusions = models.ManyToManyField(TourInclusion, blank=True)
    exclusions = models.ManyToManyField(TourExclusion, blank=True)
    tour = models.OneToOneField('Tour', on_delete=models.CASCADE, related_name='info')

    def __str__(self):
        return self.tour.name


class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    highlights = models.ManyToManyField(TourHighlight)
    image = models.ImageField(upload_to='tours/', blank=True, null=True)
    category = models.ForeignKey(
        TourCategory, on_delete=models.SET_NULL, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField()
    max_participants = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
