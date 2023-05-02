from django.db import models


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    receipt = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment # {self.id} for customer {self.customer_name}"
