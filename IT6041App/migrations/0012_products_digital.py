# Generated by Django 3.0.5 on 2020-11-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT6041App', '0011_products_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='digital',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]