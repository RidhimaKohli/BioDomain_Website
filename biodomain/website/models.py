from os import name
from django.db import models

# Create your models here.
# equipment name
# category
# institute
# City/region


# gmail accounts
# institute provide


class Category_Description(models.Model):
    Category = models.CharField(max_length=15)
    Category_Description = models.CharField(max_length=30)

class Institute(models.Model):
    Institute= models.CharField(primary_key=True,max_length=50)
    Email=models.EmailField()
    Phone=models.CharField(max_length=10)
    State=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    District=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=6)
    Website_link=models.CharField(max_length=30)
class Meta:
        model   =  Institute
        exclude = ('id',)

class Instruments(models.Model):
    Instrument_ID = models.IntegerField(unique=True)
    Name = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Manufacturer = models.CharField(max_length=30)
    Category = models.ForeignKey('Category_Description', on_delete=models.CASCADE,null=True)
    Availability = models.IntegerField()
    Institute = models.ForeignKey('Institute',on_delete=models.CASCADE,null=True)
# got some matching query doesn't exist error for Institute here , on commenting it , got id got visual error

class Instrument_Description(models.Model):
    Instrument_ID = models.ForeignKey('Instruments',on_delete=models.CASCADE,default="", editable=False)
    Instrument_Description = models.CharField(max_length=100)
    Origin = models.CharField(max_length=15)


   
    
    
