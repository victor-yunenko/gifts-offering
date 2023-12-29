import strawberry
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices




class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return str(self.email)
