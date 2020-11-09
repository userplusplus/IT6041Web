from django.contrib import admin
from .models import Products, Customer, Order, OrderItem, ShippingAddress


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


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'name',
                    'email',
                    )

    def user(self, obj):
        return obj.user


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'date_ordered',
                    'complete',
                    'transaction_id',
                    )

    def order(self, obj):
        return obj.order


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'order',
                    'quantity',
                    'date_added',
                    )

    def orderitem(self, obj):
        return obj.orderitem


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'order',
                    'address',
                    'city',
                    'post_code',
                    'date_added',
                    )

    def shippingitem(self, obj):
        return obj.shippingitem


admin.site.register(Products, ProductsAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)