# Generated by Django 5.1.1 on 2024-12-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_alter_shippingaddress_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='country',
            new_name='shipping_country',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='shipping_full_name',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='old_cart',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_address2',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_email',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_state',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_zipcode',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
