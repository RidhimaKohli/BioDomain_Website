from os import name
from django.db import models

# Create your models here.
# equipment name
# category
# institute
# City/region


class Equipments(models.Model):
    id = models.IntegerField(primary_key=True)
    e_name = models.CharField(max_length=30)
    category = models.CharField(max_length=15)
    institute = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    
