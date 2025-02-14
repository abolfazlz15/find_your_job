from django.db import models

from common.base_model import BaseModel


class SavedJob(BaseModel):
    job = models.ForeignKey(
        to="jobs.Job",
        on_delete=models.CASCADE,
        related_name="saved_job",
    )
    job_seeker = models.ForeignKey(
        to="accounts.JobSeeker",
        on_delete=models.CASCADE,
        related_name="saved_jobs",
    )
    note = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        unique_together = ["job", "job_seeker"]

    def __str__(self):
        return f"{self.job_seeker} - {self.job.title}"