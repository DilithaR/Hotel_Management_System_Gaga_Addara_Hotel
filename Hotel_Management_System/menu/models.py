from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    image = models.ImageField(upload_to='menu/images/')
    price = models.IntegerField()

    def __str__(self):
         return self.title
