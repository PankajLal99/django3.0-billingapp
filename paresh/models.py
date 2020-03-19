from django.db import models
from datetime import datetime
# Create your models here.
class Buyer(models.Model):
    buyer_name=models.TextField()

    def __str__(self):
        return self.buyer_name

class Seller(models.Model):
    seller_name=models.TextField()

    def __str__(self):
        return self.seller_name

class Billing(models.Model):
    invoice=models.IntegerField(primary_key=True)
    buyer=models.ForeignKey('Buyer',on_delete=models.CASCADE)
    seller=models.ForeignKey('Seller',on_delete=models.CASCADE)
    challan_no=models.IntegerField(null=True)
    buyer_order_no=models.IntegerField(null=True)
    invoice_date=models.DateField(default=datetime.now, blank=True)
    delivery_date=models.DateField(default=datetime.now, blank=True)
    order_date=models.DateField(default=datetime.now, blank=True)
    notes=models.TextField(blank=True,null=True)

class Products(models.Model):
    invoice=models.ForeignKey('Billing',on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    quantity=models.FloatField(null=True)
    rate=models.FloatField(null=True)
    unit=models.CharField(max_length=50)
    

class Amount(models.Model):
    invoice=models.ForeignKey('Products',on_delete=models.CASCADE)
    gst=models.FloatField(null=True)
    discount=models.FloatField(null=True)
    sub_total=models.FloatField(null=True)
    total=models.FloatField(null=True)
    words=models.CharField(max_length=100,blank=True,null=True)
