# Generated by Django 4.2.7 on 2023-12-03 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
    ]
