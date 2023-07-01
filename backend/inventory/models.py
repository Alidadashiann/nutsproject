from django.db import models

from city.models import City
from product.models import Product


class Inventory(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"inventory {self.city}"


class InventoryProduct(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"inventory {self.inventory}, product {self.product}, quantity {self.quantity}"
