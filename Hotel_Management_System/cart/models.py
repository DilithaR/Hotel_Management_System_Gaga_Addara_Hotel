from django.contrib.auth.models import User
from django.db import models
from menu.models import Project
from django.forms import ModelForm

# Create your models here.

class shopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    item = models.ForeignKey(Project, on_delete=models.SET_NULL, null = True)
    quantity = models.IntegerField()

    def __str__(self):
         return self.item.title

    @property
    def price(self):
        return(self.item.price)

    @property
    def amount(self):
        return((self.item.price) * self.quantity )

class shopCartForm(ModelForm):
    class Meta:
        model = shopCart
        fields = ['quantity']
