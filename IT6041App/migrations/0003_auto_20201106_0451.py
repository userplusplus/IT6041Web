# Generated by Django 3.0.5 on 2020-11-05 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IT6041App', '0002_products_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('-product_name',), 'verbose_name_plural': 'Products'},
        ),
    ]