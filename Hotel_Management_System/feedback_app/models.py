from django.db import models

# Create your models here.


class Feedback(models.Model):
    feedbackId      = models.IntegerField(primary_key=True)
    category        = models.CharField(max_length=20)
    rate            = models.IntegerField()
    description     = models.CharField(max_length=250)
    ansDescription  = models.CharField(max_length=250)
    date            = models.DateTimeField()

    class Meta:
        db_table = "Feedback"

class Customer_Feed(models.Model): 
    cusId           = models.CharField(max_length=10)
    feedbackId      = models.IntegerField()

    class Meta:
        db_table = "Customer_Feed"


class attraction(models.Model): 
    attractionID    = models.IntegerField(primary_key=True)
    img             = models.CharField(max_length=1000)
    Discription     = models.CharField(max_length=350)
    distance        = models.FloatField()

    class Meta:
        db_table = "attraction"