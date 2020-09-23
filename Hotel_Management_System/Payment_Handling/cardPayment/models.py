from django.db import models

class cardPayment(models.Model):
    Year = models.CharField(max_length=20)
    Month = models.CharField(max_length=20)
    Card_number = models.CharField(max_length=100)
    Exp_date = models.CharField(max_length=100)
    CRC = models.CharField(max_length=100)
    Amount = models.FloatField(max_length=100)

    def _str_(self):
        return self.Year + ' ' + self.Month + ' ' + self.Card_number + ' ' + self.Exp_date + ' ' + self.CRC + ' ' + self.Amount