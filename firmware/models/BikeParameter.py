from django.db import models

class BikeParameter(models.Model):

    bike_id = models.IntegerField()
    parameter_id = models.IntegerField()
    row = models.IntegerField()
    column = models.IntegerField()
    expression = models.CharField(max_length=200, default='') # default = parameter.name
