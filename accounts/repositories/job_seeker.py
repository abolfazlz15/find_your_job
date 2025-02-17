from django.db.models import QuerySet

from accounts.models.job_seeker import JobSeeker


class JobSeekerRepository:
    @staticmethod
    def get_by_id(user_id: int) -> JobSeeker | None:
        return JobSeeker.objects.filter(id=user_id).first()

    @staticmethod
    def get_by_email(email: str) -> JobSeeker | None:
        return JobSeeker.objects.filter(email=email).first()

    @staticmethod
    def create_user(**kwargs) -> JobSeeker:
        return JobSeeker.objects.create(**kwargs)

    @staticmethod
    def update_user(user: JobSeeker, **kwargs) -> JobSeeker:
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user: JobSeeker) -> None:
        user.delete()

    @staticmethod
    def get_all_users() -> QuerySet:
        return JobSeeker.objects.all()

    @staticmethod
    def filter_users(**filters) -> QuerySet[JobSeeker]:
        return JobSeeker.objects.filter(**filters)
