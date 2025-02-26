from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers.customer_panel.login_send_otp import CustomerLoginSerializer
from accounts.repositories.job_seeker import JobSeekerRepository
from common.otp import set_otp
from common.response import response
from rest_framework.permissions import AllowAny

class CustomerSendOtpLogin(APIView):
    serializer_class = CustomerLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not JobSeekerRepository.get_by_email(email=serializer.validated_data["email"]):
            return response(error="User not found", status=status.HTTP_400_BAD_REQUEST)
        return response(
            data={"code": set_otp(key=serializer.validated_data["email"])},
            status=status.HTTP_200_OK,
        )