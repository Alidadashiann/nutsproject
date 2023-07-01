import random, string

from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICE = (
        ('B', 'BUYER'),
        ('S', 'SELLER'),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICE, default='B', blank=True)
    city = models.ForeignKey('city.City', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def rest_password(self, *args, **kwargs):
        characters = string.ascii_letters + string.digits
        new_password = ''.join(random.choice(characters) for _ in range(8))
        self.password = make_password(new_password)
        self.save()
        return new_password


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f"name {self.name}, contact {self.contact_info}"
