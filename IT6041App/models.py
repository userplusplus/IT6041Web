from django.db import models


# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    sku = models.CharField(max_length=20)
    stock_level = models.IntegerField()

    class Meta:
        ordering = ('-product_name',)

    def __str__(self):
        return self.product_name


