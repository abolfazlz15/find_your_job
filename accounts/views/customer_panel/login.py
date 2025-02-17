from rest_framework import status
from rest_framework.views import APIView

from accounts.repositories.job_seeker import JobSeekerRepository
from accounts.serializers.customer_panel.login import CustomerLoginSerializer
from common.otp import set_otp
from common.response import response


class CustomerSendOtpLogin(APIView):
    serializer_class = CustomerLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not JobSeekerRepository.get_by_email(email=serializer.validated_data["email"]):
            return response(error="User not found", status=status.HTTP_400_BAD_REQUEST)
        return response(
            data={"code": set_otp(key=serializer.validated_data["email"])},
            status=status.HTTP_200_OK
        )