from common.base_model import BaseModel
from django.db import models

from jobs.enums import JobAppliedStatusEnum

class AppliedJob(BaseModel):
    status = models.CharField(
        max_length=32,
        choices=JobAppliedStatusEnum.choices,
        default=JobAppliedStatusEnum.PENDING,
    )
    job_seeker = models.ForeignKey(
        to="accounts.JobSeeker",
        on_delete=models.CASCADE,
        related_name="applied_jobs",
    )
    job = models.ForeignKey(
        to="jobs.Job",
        on_delete=models.CASCADE,
        related_name="applied_job",
    )
    
    class Meta:
        unique_together = ["job_seeker", "job"]

    def __str__(self):
        return f"{self.job_seeker} - {self.job}"