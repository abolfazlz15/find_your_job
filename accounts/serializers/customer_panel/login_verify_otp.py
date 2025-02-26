from rest_framework import serializers

class CustomerVerifyOtpLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=4)