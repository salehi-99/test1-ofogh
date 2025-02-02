# Generated by Django 5.1.1 on 2024-12-15 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_profile_old_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
    ]
