from django.db import models


# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()
    sku = models.CharField(max_length=20)
    stock_level = models.IntegerField()

    class Meta:
        ordering = ('-product_name',)

    def __str__(self):
        return self.product_name

class Staff(models.Model):
    staff_full_name = models.CharField(max_length=200)
    work_email = models.EmailField(max_length=200)
    work_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    department_role = models.CharField(max_length=200)

    # Note that as in the WDD, Staff.department is effectively 3 different roles
    # that can be represented by the choice of 3 strings. We will have
    # to ensure filtered input to these strings however. 

    class Meta:
        ordering = ('-staff_name',)

    def __str__(self):
        return self.staff_name
