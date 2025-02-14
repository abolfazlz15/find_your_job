from django.db import models


class CollaborationTypeEnum(models.TextChoices):
    FULL_TIME = "0", "full_time"
    PART_TIME = "1", "part_time"
    REMOTE = "2", "remote"
    HYBRID = "3", "hybrid"


class EducationEnum(models.TextChoices):
    DIPLOMA = "0", "diploma"
    ASSOCIATE_DEGREE = "1", "associate_degree"
    BACHELORS = "2", "bachelors"
    MASTERS = "3", "masters"
    PHD = "4", "phd"


class JobDutySystemEnum(models.TextChoices):
    FINISHED = "0", "finished"
    EXEMPT = "1", "exempt"
    INDUCTEE = "2", "inductee"
    ACADEMIC_EXEMPTION = "3", "academic_exemption"


class SalaryTypeEnum(models.TextChoices):
    FIXED = "0", "fixed salary"
    RANGE = "1", "salary range"
    NEGOTIABLE = "2", "negotiable"


class JobAppliedStatusEnum(models.TextChoices):
    PENDING = "0", "pending"
    SEEN = "1", "seen"
    INTERVIEW = "2", "interview"
    HIRED = "3", "hired"
    REJECTED = "4", "rejected"
