from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from users.managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    user_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'

    def __str__(self):
        return self.email

