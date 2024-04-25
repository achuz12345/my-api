# models.py

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="No description available")

    def __str__(self):
        return self.name

class Experience(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.location.name} - {self.date}"
