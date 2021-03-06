# Generated by Django 3.0.5 on 2020-11-10 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IT6041App', '0005_auto_20201109_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
