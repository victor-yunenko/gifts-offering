# Generated by Django 5.0 on 2023-12-29 12:35

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts_auth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="points",
            field=models.DecimalField(decimal_places=2, default="1.00", max_digits=3),
        ),
    ]
