from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import IntegerRangeField

from accounts.models.base_user import User
from common.validations import generate_filename, validate_file_size

class CompanyFounder(User):
    company_name = models.CharField(
        max_length=128,
    )
    company_logo = models.ImageField(
        upload_to=generate_filename,
        validators=[
            FileExtensionValidator(["png", "jpg", "jpeg"]),
            validate_file_size,
        ],
        default="defaults/user/default.jpg",
    )
    city = models.CharField(
        max_length=128,
    )
    website = models.URLField(
        null=True,
        blank=True,
    )
    employee_count = IntegerRangeField()
    description = models.TextField(
        null=True,
        blank=True,
    )


    def __str__(self):
        return self.company_name