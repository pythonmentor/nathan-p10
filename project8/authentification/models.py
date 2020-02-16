from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.EmailField(max_length=254, unique=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []