# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField('Email', max_length=255, blank=True)
    # Add custom fields here, if needed

    def __str__(self):
        return self.email

