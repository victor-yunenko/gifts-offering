# Generated by Django 5.0 on 2024-01-05 19:40

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts", "0004_add_field_gift_order_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gift",
            name="points",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name="historicalgift",
            name="points",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]