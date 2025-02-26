from django.urls import path

from accounts.views.customer_panel.login_send_otp import CustomerSendOtpLogin
from accounts.views.customer_panel.login_verify_otp import CustomerVerifyOtpLoginApiView

app_name = "accounts"
urlpatterns = [
    path("jobseeker/login/send/otp/", CustomerSendOtpLogin.as_view(), name="jobseeker_login_send_otp"),
    path("jobseeker/login/verify/otp/", CustomerVerifyOtpLoginApiView.as_view(), name="jobseeker_login_verify_otp"),
]