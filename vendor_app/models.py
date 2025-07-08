from django.db import models

from amazon_app.models import Order
class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    actual_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)

  # New field

    @property
    def merchant_share(self):
        return self.actual_amount - self.commission

    def to_customer_json(self):
        return {
            "transaction_id": self.transaction_id,
            "amount_paid": str(self.actual_amount),
            "address": self.order.customer.address,
            "ordered": self.order.product.product_name
        }

    def to_amazon_json(self):
        return {
            "cid": self.order.customer.cid,
            "transaction_id": self.transaction_id,
            "amount_received": str(self.commission),
            "order_id": self.order.oid
        }

    def to_merchant_json(self):
        return {
            "mid": self.order.product.pid,
            "transaction_id": self.transaction_id,
            "amount_received": str(self.merchant_share),
            "order_id": self.order.oid
        }

from django.core.exceptions import ValidationError

def clean(self):
    if self.commission > self.actual_amount:
        raise ValidationError("Commission cannot be greater than actual amount.")


