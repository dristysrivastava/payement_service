# Generated by Django 4.2 on 2023-05-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payement_app', '0002_payment_receipt_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='receipt_id',
        ),
    ]