from django.db import models

class BikeParameterExpression(models.Model):

    bike_id = models.IntegerField()
    parameter_id = models.IntegerField()
    expression = models.CharField(max_length=200, default='') # default = parameter.name
    is_used = models.BooleanField()

    class Meta:
        unique_together = ('bike_id', 'parameter_id')
