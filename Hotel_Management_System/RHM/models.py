#from django.forms import ModelForm,Textarea
from django.db import models

#Reception Hall Package class

class ReceptionHallPackage(models.Model):
    RH_packageID    = models.IntegerField(primary_key=True)
    theme           = models.CharField(max_length=20)
    price           = models.FloatField(max_length=10)
    description     = models.CharField(max_length=30)
    
    class Meta:
        db_table = "ReceptionHallPackage"   
        

#Reception Hall reservation class

class ReceptionHallBook(models.Model):
    RH_reserveID    = models.IntegerField(primary_key=True)
    cusId           = models.CharField(max_length=10)
    theme           = models.CharField(max_length=20)
    date            = models.DateField()
    timeFrom        = models.TimeField()
    timeTo          = models.TimeField()

    class Meta:
        db_table = "ReceptionHallBooking"   

   

