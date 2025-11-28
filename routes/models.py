from django.db import models

class AirportRoute(models.Model):
    airport_code = models.CharField(max_length=10) # e.g., 'JFK', 'LAX'
    position = models.IntegerField()  # represents left/right order
    duration = models.IntegerField(help_text="Duration in minutes") # duration of the route in minutes

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.airport_code} ({self.position})" #"JFK (1)"