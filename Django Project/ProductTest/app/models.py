from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)                   # Product name
    description = models.TextField(blank=True)                # Detailed description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 99999.99
    stock = models.IntegerField()                             # Number of items available
    image = models.URLField(blank=True, null=True)  # Product image
    is_available = models.BooleanField(default=True)          # In stock or not

    def __str__(self):
        return self.name
