# Generated by Django 5.0 on 2024-01-05 19:41

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts_auth", "0002_user_points"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="points",
            field=models.DecimalField(decimal_places=2, default="1.00", max_digits=5),
        ),
    ]
