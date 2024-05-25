# Generated by Django 5.0.2 on 2024-03-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_image_productimage_images_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]