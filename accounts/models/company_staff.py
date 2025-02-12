from django.db import models


class CompanyStaff(models.Model):
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="company_staff",
    )
    company = models.ForeignKey(
        "CompanyFounder",
        on_delete=models.CASCADE,
        related_name="staff_members",
    )
    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"{self.user.full_name} - {self.company.company_name}"
