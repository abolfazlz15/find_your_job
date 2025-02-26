from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from typing import Any
from accounts.jwt import get_user_jwt_token
from accounts.models.job_seeker import JobSeeker
from accounts.repositories.job_seeker import JobSeekerRepository
from accounts.serializers.customer_panel.login_verify_otp import CustomerVerifyOtpLoginSerializer
from common.otp import is_otp_valid
from common.response import response


class CustomerVerifyOtpLoginApiView(APIView):
    serializer_class = CustomerVerifyOtpLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if jobseeker := JobSeekerRepository.get_by_email(email=serializer.validated_data["email"], is_active=True):
            if not is_otp_valid(
                key=serializer.validated_data["email"],
                otp=serializer.validated_data["otp"],
            ):
                return response(error="Invalid OTP", status=status.HTTP_400_BAD_REQUEST)
            return response(
                data=self.get_user_data(jobseeker),
                status=status.HTTP_200_OK,
            )

        return response(error="User not found", status=status.HTTP_400_BAD_REQUEST)

    def get_user_data(self, jobseeker: JobSeeker) -> dict[str, Any]:
        access_token, refresh_token = get_user_jwt_token(jobseeker)
        return {
            "id": jobseeker.id,
            "email": jobseeker.email,
            "full_name": jobseeker.full_name,
            "city": jobseeker.city,
            "access_token": access_token,
            "refresh_token": refresh_token, 
    
        }