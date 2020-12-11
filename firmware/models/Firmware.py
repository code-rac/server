from django.db import models
from .Code import Code

class Firmware(models.Model):

    name = models.CharField(max_length=300)
    file = models.FileField(upload_to='')
    offset = models.CharField(max_length=8)

    class Meta:
        ordering = ['-id']

        # TODO: unique name