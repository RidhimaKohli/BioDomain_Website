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
    id=models.AutoField(primary_key=True)
    Category = models.CharField(max_length=15,unique=True)
    Description = models.CharField(max_length=30,default="")

class Institute(models.Model):
    id=models.AutoField(primary_key=True)
    Institute= models.CharField(max_length=50)
    Email=models.EmailField()
    Phone=models.CharField(max_length=10)
    State=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    District=models.CharField(max_length=20)
    Pincode=models.CharField(max_length=6)
    Website_link=models.CharField(max_length=30 , default="")


class Instruments(models.Model):
    id=models.AutoField(primary_key=True)
    Instrument_ID = models.IntegerField(unique=True)
    Name = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    Manufacturer = models.CharField(max_length=30)
    #Category = models.ForeignKey('Category_Description', on_delete=models.CASCADE)
    Availability = models.IntegerField()
    Instrument_Description = models.TextField(max_length=50,default="")
    Origin = models.CharField(max_length=30,default="")
    #Institute = models.ForeignKey('Institute',on_delete=models.CASCADE)
# got some matching query doesn't exist error for Institute here , on commenting it , got id got visual error

# class Instrument_Description(models.Model):
#     id=models.AutoField(primary_key=True)
#     Instrument_ID = models.ForeignKey('Instruments',on_delete=models.CASCADE,default="", editable=False)
#     Instrument_Description = models.CharField(max_length=100)
#     Origin = models.CharField(max_length=15)


   
    
    
