from rest_framework import serializers

from accounts.models.job_seeker import JobSeeker


class CustomerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = [
            "email"
        ]