from django.db import models

class Merchant(models.Model):
    mid = models.AutoField(primary_key=True)
    merchant_name = models.CharField(max_length=100)

class MerchantProduct(models.Model):
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    inventory_count = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
