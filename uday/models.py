from django.db import models

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
    challan_no=models.IntegerField()
    buyer_order_no=models.IntegerField()
    invoice_date=models.DateField()
    delivery_date=models.DateField()
    order_date=models.DateField()
    notes=models.TextField()

class Products(models.Model):
    invoice=models.ForeignKey('Billing',on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    quantity=models.FloatField()
    rate=models.FloatField()
    unit=models.CharField(max_length=50)
    gst=models.FloatField()
    discount=models.FloatField()
    sub_total=models.FloatField()
    total=models.FloatField()
    words=models.CharField(max_length=100)
