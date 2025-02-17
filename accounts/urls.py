from django.urls import path

from accounts.views.customer_panel.login import CustomerSendOtpLogin

urlpatterns = [
    path('jobseeker/login/', CustomerSendOtpLogin.as_view(), name='jobseeker_login'),
]