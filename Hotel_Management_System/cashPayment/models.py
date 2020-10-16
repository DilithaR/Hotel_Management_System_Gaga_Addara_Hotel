from django.db import models

class cashPayment(models.Model):
    Year = models.CharField(max_length=20)
    Month = models.CharField(max_length=20)
    Item_type = models.CharField(max_length=100)
    Item_number = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)
    Net_amount = models.FloatField(max_length=100)

    def _str_(self):
        return self.Year + ' ' + self.Month + ' ' + self.Item_type + ' ' + self.Item_number + ' ' + self.Quantity + ' ' + self.Net_amount
    