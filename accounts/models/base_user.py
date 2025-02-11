from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

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
    
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",  # FIXED: Prevents reverse accessor conflict
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",  # FIXED
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        abstract = True
        db_table = "users"  # Explicit table name to avoid conflicts
        verbose_name = "User"
        verbose_name_plural = "Users"
        
    def __str__(self):
        return self.email
        