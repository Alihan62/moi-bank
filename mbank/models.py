from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    balance = models.FloatField(default=0)
    password = models.TextField()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()