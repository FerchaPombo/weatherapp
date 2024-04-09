from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    icon_url = models.URLField()
    feels_like = models.FloatField(default=False)  # Add feels like field
    temp_min = models.FloatField(default=False)    # Add min temperature field
    temp_max = models.FloatField(default=False)    # Add max temperature field
    humidity = models.IntegerField(default=False) 

