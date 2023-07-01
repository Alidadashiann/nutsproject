from django.db import models

from product.models import Product
from account.models import User


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class SellStatus(models.Model):
    STATUS_CHOICES = (
        ('P', 'payed'),
        ('S', 'sended'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
