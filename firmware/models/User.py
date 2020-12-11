from django.db import models
from django.contrib.auth.models import User as TemplateUser
from .Code import Code

class User(TemplateUser):

    code = models.ForeignKey(Code, on_delete=models.DO_NOTHING)
	

