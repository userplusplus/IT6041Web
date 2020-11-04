from django.contrib import admin
from .models import Products


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name',
                    'category',
                    'description',
                    'price',
                    'sku',
                    'stock_level',
                    'image',
                    )

    def product_name(self, obj):
        return obj.product_name


admin.site.register(Products, ProductsAdmin)
