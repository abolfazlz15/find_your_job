from django.db import models

class Gender(models.TextChoices):
    GENDER_FEMALE = "0", "Female"
    GENDER_MALE = "1", "Male"
    GENDER_UNKNOWN = "2", "Unknown"