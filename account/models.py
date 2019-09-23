from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name
