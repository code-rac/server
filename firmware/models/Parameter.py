from django.db import models

class Parameter(models.Model):

    name = models.CharField(max_length=200, unique=True)
    name_vn = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    unit = models.CharField(max_length=200)
    upper = models.FloatField()
    lower = models.FloatField()
    recommend = models.FloatField()
    
