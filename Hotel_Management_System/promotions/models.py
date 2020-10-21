from django.db import models

class Promo(models.Model):
    promoTitle = models.CharField(max_length=30)
    promoDescription = models.CharField(max_length=80)
    promoImage = models.ImageField(upload_to='promotions/images/')
    promoPrice = models.IntegerField()
    expiredate =models.DateTimeField(null=True)
