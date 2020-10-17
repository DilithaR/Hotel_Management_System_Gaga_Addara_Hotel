from django.db import models

class revokedPayments(models.Model):
    Payment_type = models.CharField(max_length=100)
    Paid_amount = models.FloatField(max_length=100)
    Rev_amount = models.FloatField(max_length=100)

    def _str_(self):
        return self.Payment_type + ' ' + self.Paid_amount + ' ' + self.Rev_amount
