# Generated by Django 4.2 on 2023-05-02 08:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payement_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='receipt_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
