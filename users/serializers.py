from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from django.contrib.auth import authenticate
from otp.models import OTP
from .models import User

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    verification_code = serializers.CharField(max_length=6)
    password = serializers.CharField()

    def validate(self, data):
        otp = OTP.objects.filter(email=data["email"], verification_code = data["verification_code"]).order_by("-created_at").first()
        if not otp or not otp.is_valid():
            raise ValidationError("OTP is invalid.")
        return data
    
    def create(self, validated_data):
        user = User.objects.create(
            name = validated_data["name"],
            email = validated_data["email"]
        )
        user.set_password(validated_data["password"])

        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise AuthenticationFailed("User not found.")
        data["user"] = user
        return data