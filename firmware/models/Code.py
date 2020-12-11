from django.db import models

class Code(models.Model):

    name = models.CharField(max_length=200, unique=True)
    is_used = models.BooleanField(default=False)
    
