from django.db import models

from accounts.models.base_user import User
from common.validations import validate_file_size


class JobSeeker(User):
    city = models.CharField(
        max_length=128,
    )
    resume = models.FileField(
        validators=[
            validate_file_size,
        ],
    )

    def __str__(self):
        return self.email