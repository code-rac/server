from django.db import models
from django.contrib.auth.models import User as TemplateUser
from .Code import Code

class User(TemplateUser):

    code = models.CharField(max_length=200)
    # readable = models.BooleanField(default=True)
    # writable = models.BooleanField(default=True)
    
	

