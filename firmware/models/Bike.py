from django.db import models

class Bike(models.Model):

    name = models.CharField(max_length=200, unique=True)
    
