from django.db import models
from django.db import models

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False,unique=True)
