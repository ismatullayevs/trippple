from django.db import models


class Destination(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city


class DestinationInfo(models.Model):
    languages = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    population = models.IntegerField()
    timezone = models.CharField(max_length=16)
    time_to_travel = models.CharField(max_length=100)
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE, related_name='info')

    def __str__(self):
        return f"{self.destination.city} Info"
