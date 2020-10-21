from django.db import models  

class Booking(models.Model):  
    bpacname = models.CharField(max_length=100,null=True)
    bfname = models.CharField(max_length=100)  
    blname = models.CharField(max_length=100)
    bdate = models.DateField()
    badults = models.CharField(max_length=20) 
    bchild = models.CharField(max_length=20)
    bemail =  models.EmailField()
    

    
    
    class Meta:  
        db_table = "booking"


class Packages(models.Model):  
    
    ptitle = models.CharField(max_length=100)  
    ptype = models.CharField(max_length=100)
    pprice = models.CharField(max_length=100)
    pdays = models.CharField(max_length=20) 
    pdes = models.CharField(max_length=1000)
    image = models.ImageField(null=True, blank=True)
    
    class Meta:  
        db_table = "packages" 



class Offers(models.Model):  
    
    offertitle = models.CharField(max_length=100,null=True)  
    offerprice = models.CharField(max_length=100,null=True)
    offerdis = models.CharField(max_length=100,null=True)
    offerdes = models.CharField(max_length=1000,null=True) 
    condition = models.CharField(max_length=1000,null=True)
    ofimage = models.ImageField(null=True, blank=True)
    
    class Meta:  
        db_table = "offers"  



 