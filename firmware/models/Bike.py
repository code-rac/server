from django.db import models

class Bike(models.Model):

    name = models.CharField(max_length=200, unique=True)
    ecu_id = models.CharField(max_length=20)
    generation = models.IntegerField()
    code = models.CharField(max_length=20)
    start_at = models.DateField()
    is_used = models.BooleanField(default=False)
    cc = models.IntegerField()
