from django.db import models

from city.models import City
from account.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product/")
    price = models.IntegerField()
    quantity = models.IntegerField()
    type = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    product_owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


# TODO where we have to use this?!
class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    quantity = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"product {self.product.name}, name {self.name}"
