from django.db import models

class BikeParameter(models.Model):

    name = models.CharField(max_length=200, default='')
    bike_id = models.IntegerField()
    parameter_id = models.IntegerField()
    row = models.IntegerField()
    column = models.IntegerField()
    is_used = models.BooleanField()
    
    class Meta:
        unique_together = ('bike_id', 'row', 'column')
