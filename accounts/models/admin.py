from django.db import models
from accounts.models.base_user import User


class Admin(User):
    phone_number = models.CharField(max_length=10)


    def __str__(self):
        return self.full_name