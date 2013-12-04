from django.db import models


class Hut(models.Model):
    CATEGORY = (
        ('standard', 'Standard Hut'),
        ('serviced', 'Serviced Hut'),
        ('great', 'Great Walk Hut'),
        ('bivvy', 'Basic Hut (Bivvy)'),
        ('alpine', 'Serviced Alpine Hut'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY)
    lat = models.DecimalField(max_digits=15, decimal_places=9)
    long = models.DecimalField(max_digits=15, decimal_places=9)
