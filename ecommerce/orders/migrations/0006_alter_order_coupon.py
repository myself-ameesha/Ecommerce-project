# Generated by Django 5.0.2 on 2024-04-29 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='coupon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]