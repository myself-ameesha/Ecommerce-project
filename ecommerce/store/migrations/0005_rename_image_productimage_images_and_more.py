# Generated by Django 5.0.2 on 2024-03-14 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_images_productimage_image_product_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimage',
            old_name='image',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.product'),
        ),
    ]