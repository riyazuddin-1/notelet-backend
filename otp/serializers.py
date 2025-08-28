from rest_framework import serializers
from django.core.exceptions import ValidationError
import os
from .models import OTP

class SendSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        if not validated_data['verification_code']:
            raise ValidationError("Server error: Verification code missing.")
        instance = OTP.objects.create(email=validated_data["email"], verification_code = validated_data['verification_code'])
        return instance