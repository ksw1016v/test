from django.db import models
from django.utils import timezone

# Create your models here.
class Business(models.Model):
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.number
