from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    detial = models.CharField(max_length=100)
    bedcount = models.CharField(max_length=10)
    avalidbed = models.CharField(max_length=10)
    outbed = models.CharField(max_length=10)
    def __str__(self):
        return self.name