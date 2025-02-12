from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import UserManager
from common.base_model import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(
        db_index=True,
        unique=True,
    )
    full_name = models.CharField(
        max_length=128,
    )
    is_active = models.BooleanField(
        default=True,
    )
    gender = models.CharField(
        max_length=1,
        default="2",
    )
    is_staff = models.BooleanField(
        default=False,
    ) 
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

        
    def __str__(self):
        return self.email
        