from django.contrib.postgres.fields import ArrayField, IntegerRangeField
from django.db import models

from accounts.enums import Gender
from common.base_model import BaseModel
from jobs.enums import (
    CollaborationTypeEnum,
    EducationEnum,
    JobDutySystemEnum,
    SalaryTypeEnum,
    )


class Job(BaseModel):
    city = models.CharField(
        max_length=128,
    )
    collaboration_type = models.CharField(
        max_length=128,
        choices=CollaborationTypeEnum.choices,
    )
    description = models.TextField()
    title = models.CharField(
        max_length=128,
    )
    immediate = models.BooleanField(
        default=False,
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    education = models.CharField(
        max_length=32,
        choices=EducationEnum.choices,
    )
    duty_system = ArrayField(
        models.CharField(max_length=50, choices=JobDutySystemEnum.choices),
        null=True,
        blank=True,
    )
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
    )
    salary_type = models.CharField(
        max_length=32,
        choices=SalaryTypeEnum.choices,
        default=SalaryTypeEnum.NEGOTIABLE,
    )
    salary_fixed = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    salary_range = IntegerRangeField(
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        to="accounts.CompanyFounder",
        on_delete=models.CASCADE,
        related_name="jobs",
    )
    
    def __str__(self):
        return self.title
