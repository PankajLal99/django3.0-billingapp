from django.db import models

# Create your models here.
class Invoi(models.Model):
    inv=models.IntegerField()

class Cal(models.Model):
    num = models.ForeignKey(Invoi,on_delete=models.CASCADE)
    a=models.IntegerField(null=True)
    b=models.IntegerField(null=True)